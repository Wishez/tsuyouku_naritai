import React from 'react';
import { Button } from 'semantic-ui-react';

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

export default SelectOrdersButton;