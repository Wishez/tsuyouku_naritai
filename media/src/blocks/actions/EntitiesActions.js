import { RECEIVE_ENTITIES, REQUEST_ENTITIES,
	INVALIDATE_ENTITIES, SELECT_ENTITY, SELECT_ENTITIES } from './../constants/actionTypes.js';
import { createAction } from 'redux-actions';
import { entitiesPattern } from './../constants/entities.js';
import expect from 'expect';

// Выбор сущности, которую нужно отобразить.
export const selectEntity = (entity, id) => ({
	type: SELECT_ENTITY,
	entity,
	id
});


// Выбор сущности, которые будут отображаться в списке.
export const selectEntities = entities => ({
	type: SELECT_ENTITIES,
	entities
});

export const invalidateEntities = () => ({ 
	type: INVALIDATE_ENTITIES
});

// Компонуем действие для обработки состояние обработчиком состояния
const receiveEntities = (entities, json) => ({
	type: RECEIVE_ENTITIES,
	entities,
	receivedAt: Date.now()
});

const requestEntities = () => ({
	type: REQUEST_ENTITIES
});

const extractEntities = entities => (
	entities.reduce((accumulatedData, data) => (
		{
			...accumulatedData,
			[data.id]: data
		}// return updated accumulatedData
	), {}) // end reduce
);

const makeStateEntitiesAndDispatch = (state, dispatch) => {
	const stateEntites = {
		...state
	};
	// Извлекаем каждый ключ из состояния существ.
	const keys = Object.keys(stateEntites);
	console.log(keys, 'array of entities');
	let i = 0;
	// Универсальная функция получающая ключи,
	// компонующая состояние и перенаправляющая компоновонное
	// состояние в обработчик состояния.
	const fetchMakeDispatchEntities = (entitiesKeys, i) => {
		console.log(entitiesKeys[i], 'key' );
		// Проврка на необходимость дальше самовызываться.
		// Базис рекурсии.
		if (!entitiesKeys[i]) {
			// Перенаправляем в обработчик состояния.
			return dispatch(receiveEntities(stateEntites));
		}

		return fetch(`/api/v0/${entitiesKeys[i]}/`)
			.then(response=>response.json())
			// Отправляем их через диспатчер к обработчику состояния
			.then(json => {
				// Извлекаем данные и присваиваем их по ключу объекту с сущностями.
				stateEntites[entitiesKeys[i]] = extractEntities(json);
				// Вызываю ещё раз для того, чтобы запросить следующие сущности.
				fetchMakeDispatchEntities(entitiesKeys, i+=1);
			}); 
	}
	// Запускаю универсальную функцию.
	return fetchMakeDispatchEntities(keys, i);
} 
// Заказываем данные с сервера.
const fetchEntities = entities => dispatch => {
	// Показываем загрузку. 
	// requestOrders компонует действие, с определённым типом заказов
	// сменяя в обработчие закзов(reudcer-e) состояние этих заказов
	dispatch(requestEntities(entities));

	// При первой загрузки, когда выбранные сущности не установленны
	// Загружаются все данные.
	if (!entities) {
		// Устанавливается состояние выбранных заказов на 'events' по умолчанию.
		dispatch(selectEntities('events'));
		// Заполняемые данными сущности.
		const newStateEntites = {
			...entitiesPattern
		};
		// Запрашиваем все данные, компонуем состояние и устанавливаем его
		// через обработчик состояния.
		return makeStateEntitiesAndDispatch(newStateEntites, dispatch);
	} else {
		// Выбираем сущности.
		dispatch(selectEntities(entities));
		// Делаем единичный запрос к данным.
		return fetch(`/api/v0/${entities}/`)
			.then(response=>response.json())
			.then(json => {
				
				// Отправляем данные в обработчик состояние.
				// Этот объект распыляется внутри состояния
				// и заменяет устаревшие данные.
				dispatch(receiveEntities({
					[entities]: extractEntities(json)
				}));
			}); 
	}


};


const shouldFetchEntities = (state, entities) => {
	// Проверяем существующий тип заказа
	// Также определённые сущности внутри типа заказа.
	// Если типа заказа нет, то нужно получить его!
	const { isFetching, didInvalidate } = state.entities;
	// Загруженны ли данные?
	if (!state.entities[entities]) 
		return true;
	// Сущности не нужно запрашивать, посколько они уже запрошенны
	// и обрабатываются обработчиком состояния.
	if (isFetching)
		return false;
	// Елси же ничего из того, что выше не подошло
	// значит их нужно либо обновить, либо нет.
	// didInvalidate - переменная управляемая обработчиком
	// события клика для обновления данных. 
	return didInvalidate;

};

export const fetchEntitiesIfNeeded = entities => (dispatch, getState) => {
	// Делаем проверку существующих или нет сущностей в состояние.
	// Запрашиваем то, что нужно.
	if (shouldFetchEntities(getState(), entities)) {
		return dispatch(fetchEntities(entities));
	} else　{
		// Возвращает управление компоненту.
		return false;
	}
};