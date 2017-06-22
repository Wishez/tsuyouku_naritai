import { createStore, combineReducers } from 'redux';
import connect_form from './connect_form.js';
import visibilityFilter from './visibilityFilter.js';
import selectedEntities from './selectedEntities';
import entities from './entities';
import selectByEntity from './selectByEntity';


const rootReducer = combineReducers({
	connect_form,
	selectedEntities,
	entities,
	selectByEntity
});


export default rootReducer;