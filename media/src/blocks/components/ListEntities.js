import React from 'react';
import { Dropdown } from 'semantic-ui-react';

const ListEntities = ({
	entities,
	name,
	...rest
}) => {
	// Why does {...rest} not work?s
	// name - свойство объекта, которое будет отображаться в списке.
	
	
	const listEntities = Object.assign([], entities).reduce((arrayItems, entity) => {
	
		return [
			...arrayItems,
			{
				value: entity.id,
			    key: entity.id,
			    text: entity[name]
		    }
		];
	}, []);

	return (
		<Dropdown {...rest}
			fluid multiple search selection
			options={listEntities}
		/>
	);
};

export default ListEntities;