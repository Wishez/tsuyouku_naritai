import { RECEIVE_ORDERS, SELECT_ORDERS, REQUEST_ORDERS,
 	INVALIDATE_ORDERS, SELECT_ENTITY } from './../constants/actionTypes.js';
import { selectOrders, invalidateOrders,
 requestOrders, receiveOrders } from './../actions/OrderActions.js';

const initState = {
	isFetching: false,
	didInvalidate: false,
	entities: {
		employers: {},
		customers: {},
		artists: {},
		places: {},
		contractors: {},
		visa: {},
		events: {},
		adventures: {},
		partners: {},
		halls: {}
	}
};
// Обработчик состояния заказов
export const orders = (
	state = initState,
	action
) => {
	switch (action.type) {
		case INVALIDATE_ORDERS:
			return {
				...state,
				didInvalidate: true
			};
		case REQUEST_ORDERS:
			return {
				...state,
				isFetching: true,
				didInvalidate: false
			};
		case RECEIVE_ORDERS:
			console.log(action.orderEntities);
			console.log(action.items);
			return {
				...state,
				isFetching: false,
				didInvalidate: false,
				entities: {
					...state.entities,
					// Синтаксис ES6, позволяет создавать внутри объекта 
					// имя свойсва с помощью переменной. Великолепно!
					[action.orderEntities]: action.items 
				},
				lastUpdated: action.receivedAt
			};
		default:
			return state;
	}
};
// Фильтер для смены заказов.
// 2 types of orders
// 1: events
// 2: adventures
export const selectedOrders = (
		state = 'events',
		action
) => {
	switch(action.type) {
		case SELECT_ORDERS:
			return action.orders;
		default:
			return state;
	}
};
// Фильтер для отображения определенных сущностей.

const filterInitState = {
	employers: null,
	customers: null,
	artists: null,
	places: null,
	contractors: null,
	visa: null,
	events: null,
	adventures: null,
	partners: null,
	halls: null
};

export const selectedEntities = (
	state = filterInitState,
	action
) => {
	switch (action.type) {
		case SELECT_ENTITY:
			return {
				...state,
				[action.entity]: action.id
			}
		default:
			return state;
	}
};
// Фильтер для извлечения одной сущности
// ...
// Есть два типа данных готовые заказы и не готовые заказы,
// путешествий и мероприятий
export const ordersByData = (
	state = {},
	action
) => {
	switch (action.type) {
		case SELECT_ORDERS:
		case REQUEST_ORDERS:
		case RECEIVE_ORDERS:
			return {
				...state,
				// Запаковываю в хранилище заказы с относящимися к ним сущностями.
				[action.orders]: orders(state[action.orders], action)
			}
		default:
			return state;
	}
};

// export const selectedSubreddit = (
// 	state = 'reactjs',
// 	 action
// ) => {
// 	switch(action.type) {
// 		case SELECT_SUBREDDIT:
// 			return action.subreddit;
// 		default:
// 			return state;
// 	}

// };

// export const posts = (
// 	state = {
// 		isFetching: false,
// 		didInvalidate: false,
// 		items: []
// 	},
// 	action
// ) => {
// 	switch (action.type) {
// 		case INVALIDATE_SUBREDDIT:
// 			return {
// 				...state,
// 				didInvalidate: true
// 			};
// 		case REQUEST_POSTS:
// 			return {
// 				...state,
// 				isFetching: true,
// 				didInvalidate: false
// 			};
// 		case RECEIVE_POSTS:
// 			return {
// 				...state,
// 				didInvalidate: false,
// 				isFetching: false,
// 				items: action.posts,
// 				lastUpdated: action.receivedAt
// 			};
// 		default:
// 			return state;
// 	}
// };

// export  const postsBySubreddit = (
// 	state = {},
// 	action
// ) => {
// 	switch (action.type) {
// 		case INVALIDATE_SUBREDDIT:
// 		case RECEIVE_POSTS:
// 		case REQUEST_POSTS:
// 			return {
// 				...state,
// 				[action.subreddit]: posts(state[action.subreddit], action)
// 			};
// 		default:
// 			return state;
// 	}
// }
