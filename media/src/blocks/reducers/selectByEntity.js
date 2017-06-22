import { SELECT_ENTITY } from './../constants/actionTypes.js';

const selectByEntityInitState = {
	employer: null,
	customer: null,
	artist: null,
	place: null,
	contractor: null,
	visa: null,
	event: null,
	adventure: null,
	partner: null,
	hall: null
};
// Здесь будут выбранные сущности из списка сузности 
// для отображения единичной сущности.
const selectByEntity = (
	state = selectByEntityInitState,
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

export default selectByEntity;