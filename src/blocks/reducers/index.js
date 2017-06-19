import { createStore, combineReducers } from 'redux';
import connect_form from './connect_form.js';
import visibilityFilter from './visibilityFilter.js';
import { order, postsBySubreddit, selectedSubreddit } from './order.js';

const rootReducer = combineReducers(
	connect_form,
	visibilityFilter,
	order
);


export default rootReducer;