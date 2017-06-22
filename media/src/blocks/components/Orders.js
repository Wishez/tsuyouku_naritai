import React, { Component } from 'react';
import FadeIn from 'react-fade-in';
import ListEntities from './ListEntities';
import ListSelectEntitiesButtons from './ListSelectEntitiesButtons';
/* Plan:
Events
	completedEvents: object
	customers: object
	artists: object
	places: object
	halls: object(for places) 
	employers: object
	
ListEntities is list with entities are below.
  entities: Array
  onEntityClick: (id: number)
Customer
	  customer: Object
Artist
	  artist: Object
Employer
	  employer: Object
Place
	  place: Object
Hall
	  hall: Object
Visa
	  visa: Object
CustomersList is list with cutomers. Differance is in checkboxes(later)
  entities: Array
  onEntityClick: (id: number) */


const Orders = ({
		selectedEntities,
		loadedEntities,
		isFetching,
		lastUpdated,
		dispatch,
		updateEntities,
		selectAndUpdateEntities,
		selectNeededEntity
}) => {
	console.log(loadedEntities);

	let listMetaData = {
		placeholder: '',
		name: ''
	};
	switch (selectedEntities) {
		case 'events':
			listMetaData.placeholder = 'Выберете мероприятие';
			listMetaData.name = 'event_name';
			break;
		case 'adventures':
			listMetaData.name = 'adventure_number';
			listMetaData.placeholder = 'Выберете тур-путешествие';
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
						hour: 'numeric', 
						minute: 'numeric', 
						second: 'numeric'
					})}
				</small> 
			</div>
			<ListSelectEntitiesButtons isFetching={isFetching}
				selectAndUpdateEntities={selectAndUpdateEntities}
				
			/>
			<ListEntities {...listMetaData}
				entities={{...loadedEntities[selectedEntities]}} />
		</FadeIn>
	);
}

export default Orders;