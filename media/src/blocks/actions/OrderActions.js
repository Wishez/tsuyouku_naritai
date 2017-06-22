import { RECEIVE_ORDERS, REQUEST_ORDERS, 
	INVALIDATE_ORDERS, SELECT_ENTITY, SELECT_ORDERS } from './../constants/actionTypes.js';
import { createAction } from 'redux-actions';
import expect from 'expect';


// export const selectOrders = createAction(
// 	SELECT_ORDERS,
// 	orders => orders
// );
export const selectEntity = (entity, index) => ({
	type: SELECT_ENTITY,
	entity,
	id: index
});
export const selectOrders = orders => ({ 
	type: SELECT_ORDERS,
	orders
});

const testSelectOrders = () => {
	const stateAfter = {
		type: SELECT_ORDERS,
		orders: 'events'		
	};
	expect(selectOrders('events')).toEqual(stateAfter);
	console.log('testSelectOrders=>true');
}

export const invalidateOrders = orders => ({ 
	type: SELECT_ORDERS,
	orders
});
// export const invalidateOrders = createAction(
// 	INVALIDATE_ORDERS,
// 	orders => orders
// );
const testInvalidateOrders = () => {
	const stateAfter = {
		type: SELECT_ORDERS,
		orders: 'events'		
	};
	expect(invalidateOrders('events')).toEqual(stateAfter);
	console.log('testInvalidateOrders=>true');
}

export const requestOrders = orders => ({
	type: REQUEST_ORDERS,
	orders
});

// Компонуем действие для обработки состояние обработчиком состояния
export const receiveOrders = (orders, orderEntities, json) => ({
	type: RECEIVE_ORDERS,
	orders,
	orderEntities,
	items: json.reduce((accumulatedData, data) => {
		return {
			...accumulatedData,
			[data.id]: data
		};
	}, {}),
	receivedAt: Date.now()
});
// Заказываем данные с сервера.
const fetchEntities = (orders, entities) => dispatch => {
	// Показываем загрузку. 
	// requestOrders компонует действие, с определённым типом заказов
	// сменяя в обработчие закзов(reudcer-e) состояние этих заказов
	dispatch(selectOrders(orders));
	dispatch(requestOrders(orders));
	// Запрашиваем нужные сущности.
	return fetch(`/api/v0/${entities}/`)
		.then(respond=>respond.json())
		// Отправляем их через диспатчер к обработчику состояния
		.then(json => {
			// if (json.length !== 0)
				dispatch(receiveOrders(orders, entities, json))
		}); 
};


const shouldFetchEntities = (state, orders, entities) => {
	// Проверяем существующий тип заказа
	const ordersType = state.ordersByData[orders];
	// Также определённые сущности внутри типа заказа.
	// Если типа заказа нет, то нужно получить его!
	const stateEntities = ordersType ? ordersType.entities[entities] :false;
	// Если нет сущности внутри типа, получаем их.
	if (!stateEntities) 
		return true;
	// Сущности не нужно запрашивать, посколько они уже запрошенны
	// и обрабатываются обработчиком состояния.
	if (ordersType.isFetching)
		return false;
	// Елси же ничего из того, что выше не подошло
	// значит их нужно либо обновить, либо нет.
	// didInvalidate - переменная управляемая обработчиком
	// события клика для обновления данных. 
	return ordersType.didInvalidate;

};

export const fetchEntitiesIfNeeded = (orders, entities) => (dispatch, getState) => {
	// Делаем проверку существующих или нет сущностей в состояние.
	// Запрашиваем то, что нужно.
	if (shouldFetchEntities(getState(), orders, entities)) {
		return dispatch(fetchEntities(orders, entities));
	} else　{
		// Возвращает управление компоненту, чтобы сменить значение в фильтре заказов.
		return false;
	}
};