import React, { Component } from 'react';
import FadeIn from 'react-fade-in';
// import { Link } from 'react-router-dom';
import { Dropdown, Button } from 'semantic-ui-react';

// Events
	// completedEvents: object
	// customers: object
	// artists: object
	// places: object
	// halls: object(for places) 
	// employers: object
	// 
// ListEntities is list with entities are below.
//   entities: Array
//   onEntityClick: (id: number)
// Customer
// 	  customer: Object
// Artist
// 	  artist: Object
// Employer
// 	  employer: Object
// Place
// 	  place: Object
// Hall
// 	  hall: Object
// Visa
// 	  visa: Object
// CustomersList is list with cutomers. Differance is in checkboxes(later)
//   entities: Array
//   onEntityClick: (id: number)

const ListEntities = ({
	...rest,
	entities,
	name
}) => {
	// name - свойство объекта, которое будет отображаться в списке.
	const listEntities = [...entities].reduce((arrayItems, entity) => {
		const entityOption = {
			value: entity.id,
			key: entity.id,
			text: entity[name]
		};
		console.log(entity[name]);
		arrayItems.push(entityOption)

		return arrayItems;
	}, []);

	return (
		<Dropdown {...rest} 
			fluid multiple search selection
			options={listEntities}
		/>
	);
};
const SelectOrdersButton = ({
 	selectEntitiesInOrders,
 	orders,
 	isFetching,
 	entities,
 	selectNeededOrders,
 	...rest
}) => (
	<Button 
		{...rest}
		loading={isFetching}
		onClick={() => {
			selectEntitiesInOrders(orders, entities);
			selectNeededOrders(orders);
		}}
	/>
); 

const ListSelectOrdersButtons = ({...rest}) => (
	<div>
		<SelectOrdersButton content='Заказанные мероприятия'
		    orders='events'
		    color='grey'
		    size='medium'
		    entities='events'
		    {...rest}
		/>
		<SelectOrdersButton content='Заказанные тур-путешествия'
		    orders='adventures'
		    color='grey'
		    size='medium'
		    entities='adventures'
		    {...rest}
		/>
	</div>
);

const Orders = ({
		selectedOrders,
		selectedEntities,
		entities,
		isFetching,
		lastUpdated,
		dispatch,
		selectEntitiesInOrders,
		selectNeededOrders
}) => {
	console.log(selectedOrders);
	console.log(entities[selectedOrders]);

	let listOrders = {};
	// const arrEntities = ;
	switch (selectedOrders) {
		case 'events':
			listOrders =  <ListEntities name='event_name'
				entities={{...entities[selectedOrders]}}
				placeholder='Выберете мероприятие'
			/>;
			break;
		case 'adventures':
			listOrders = <ListEntities name='adventure_number'
				entities={{...entities[selectedOrders]}}
				placeholder='Выберете тур-путешествие'
			/>;
			break;
		default:
			break;
	}

	return (
		<FadeIn>
			<div>
				<small>
					Последнее обновление:&nbsp;
					{new Date(Date.now()).toLocaleDateString('ru-RU', { 
						hour:'numeric', 
						minute: 'numeric', 
						second: 'numeric'
					})}
				</small> 
			</div>
			<ListSelectOrdersButtons selectEntitiesInOrders={selectEntitiesInOrders}
				isFetching={isFetching}
				selectNeededOrders={selectNeededOrders}
			/>
			{listOrders}
		</FadeIn>
	);
}

export default Orders;