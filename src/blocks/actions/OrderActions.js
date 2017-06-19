import { RECEIVE_ORDERS, SELECT_ORDERS, REQUEST_ORDERS } from './../constants/actionTypes.js';

export const ordersOrders = orders => ({ 
	type: SELECT_ORDERS,
	orders
})

export const invalidateOrders = orders => ({ 
	type: SELECT_ORDERS,
	orders
})

export const requestOrders = orders => ({
	type: REQUEST_ORDERS,
	orders
});

// Компонуем действие для обработки состояние обработчиком состояния
export const receiveOrders = (orders, orderEntities, json) => ({
	type: RECEIVE_ORDERS,
	orders,
	orderEntities,
	items: json.reduce(accumulatedData, data => {
		accumulatedData[data.id] = data;
		return accumuletedData;
	}, {}),
	receivedAt: Date.now()
});
// Заказываем данные с сервера.
const fetchEntities = (orders, entities) => dispatch => {
	// Показываем загрузку. 
	// requestOrders компонует действие, с определённым типом заказов
	// сменяя в обработчие закзов(reudcer-e) состояние этих заказов
	dispatch(requestOrders(orders));
	// Запрашиваем нужные сущности.
	return fetch(`/api/v0/${entities}/`)
		.then(respond=>respond.json())
		// Отправляем их через диспатчер к обработчику состояния
		.then(json => recevieOrders(orders, entities, json)) 
};


const shouldFetchEntities = (state, orders, entities) => {
	// Проверяем существующий тип заказа
	const ordersType = state.ordersByData[orders];
	// Также определённые сущности внутри типа заказа.
	// Если типа заказа нет, то нужно получить его!
	const stateEntities = ordersType ? false : ordersType.entities[entities];
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
	if (shouldFetchEntities(getState(), orders, entities))
		return dispatch(fetchEntities(orders, entities));
};

export const SELECT_SUBREDDIT = 'SELECT_SUBREDDIT'

export function selectSubreddit(subreddit) {
  return {
    type: SELECT_SUBREDDIT,
    subreddit
  }
}
export const INVALIDATE_SUBREDDIT = 'INVALIDATE_SUBREDDIT'

export function invalidateSubreddit(subreddit) {
  return {
    type: INVALIDATE_SUBREDDIT,
    subreddit
  }
}

export const REQUEST_POSTS = 'REQUEST_POSTS'

function requestPosts(subreddit) {
  return {
    type: REQUEST_POSTS,
    subreddit
  }
}

export const RECEIVE_POSTS = 'RECEIVE_POSTS'

function receivePosts(subreddit, json) {
  return {
    type: RECEIVE_POSTS,
    subreddit,
    posts: json.data.children.map(child => child.data),
    receivedAt: Date.now()
  }
}