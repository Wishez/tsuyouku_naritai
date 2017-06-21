import React, { Component } from 'react';
import FadeIn from 'react-fade-in';
import { Link } from 'react-router-dom';
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
const FilterLink = ({
 	dispatch, 
 	handleChangeOrders,
 	neededOrders,
 	text
}) => (
	<Link to={`/orders/${neededOrders}`}
		onClick={() => {
			handleChangeOrders(neededOrders);
		}}>
		{text}
	</Link>
); 

const Orders = ({
		selectedOrders,
		selectedEntities,
		entities,
		isFetching,
		lastUpdated,
		dispatch,
		handleChangeOrders
}) => {
	console.log(entities);
	// console.log(lastUpdated);
	// console.log(selectedOrders);
	// console.log(selectedEntities);
	return (
		<FadeIn>
			Order's section!
		</FadeIn>
	);
};



export default Orders;