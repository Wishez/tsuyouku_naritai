import { SELECT_ENTITIES } from './../constants/actionTypes.js';

/* Фильтер для смены заказов.
types of entities
1: events
2: adventures
3: employers
4: customers
5: artists
6: places
7: contractors
8: visa
9: partners
10: halls
11: barters */
// По умолчанию ничего не выбрано, потому что нет данных, которые следует выбирать.
const selectedEntities = (
	state = false,
	action
) => {
	switch (action.type) {
		case SELECT_ENTITIES:
			return action.entities;
		default:
			return state;
	}
};

export default selectedEntities;