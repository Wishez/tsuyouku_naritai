import React from 'react';
import { Button } from 'semantic-ui-react';

const SelectEntitiesButton = ({
 	isFetching,
 	entities,
 	selectAndUpdateEntities,
 	updateEntities,
 	...rest
}) => (
	<Button 
		{...rest}
		loading={isFetching}
		onClick={() => {
			selectAndUpdateEntities(entities);
		}}
	/>
); 

export default SelectEntitiesButton;