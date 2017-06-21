import { createStore, combineReducers } from 'redux';
import connect_form from './connect_form.js';
import visibilityFilter from './visibilityFilter.js';
import { ordersByData, selectedOrders, selectedEntities } from './order.js';

const rootReducer = combineReducers({
	connect_form,
	selectedOrders,
	ordersByData,
	selectedEntities
});


export default rootReducer;