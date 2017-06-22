import { RECEIVE_ENTITIES, REQUEST_ENTITIES, INVALIDATE_ENTITIES } from './../constants/actionTypes.js';
import { entitiesPattern } from './../constants/entities.js';
const entitiesState = {
	...entitiesPattern
};
const entities = (
	state=entitiesState,
	action
) => {
	switch (action.type) {
		case INVALIDATE_ENTITIES:
			return {
				...state,
				didInvalidate: true
			};
		case REQUEST_ENTITIES:
			return {
				...state,
				isFetching: true,
				didInvalidate: false
			};
		case RECEIVE_ENTITIES:
			return {
				...state,
				isFetching: false,
				didInvalidate: false,
				lastUpdated: action.receivedAt,
				...action.entities
			};
		default:
			return state;
	}
};

export default entities;
// Обработчик состояния заказов
// const initState = {
// 	isFetching: false,
// 	didInvalidate: false
// };
// const orders = (
// 	state = initState,
// 	action
// ) => {
// 	switch (action.type) {
// 		case INVALIDATE_ORDERS:
// 			return {
// 				...state,
// 				didInvalidate: true
// 			};
// 		case REQUEST_ORDERS:
// 			return {
// 				...state,
// 				isFetching: true,
// 				didInvalidate: false
// 			};
// 		case RECEIVE_ORDERS:
// 			return {
// 				...state,
// 				isFetching: false,
// 				didInvalidate: false,
// 				lastUpdated: action.receivedAt
// 			};
// 		default:
// 			return state;
// 	}
// };

// Фильтер для извлечения одной сущности
// ...
// Есть два типа данных готовые заказы и не готовые заказы,
// путешествий и мероприятий
// export const entitiesByData = (
// 	state = {},
// 	action
// ) => {
// 	switch (action.type) {
// 		case SELECT_ORDERS:
// 		case REQUEST_ORDERS:
// 		case RECEIVE_ORDERS:
// 			return {
// 				...state,
// 				// Запаковываю в хранилище заказы с относящимися к ним сущностями.
// 				...entities(state, action)
// 			}
// 		default:
// 			return state;
// 	}
// };

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
