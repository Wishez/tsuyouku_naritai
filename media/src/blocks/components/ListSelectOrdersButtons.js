import React from 'react';
import SelectOrdersButton from './SelectOrdersButton';

const ListSelectOrdersButtons = ({...rest}) => (
	<div>
		<SelectOrdersButton {...rest}
			content='Заказанные мероприятия'
		    orders='events'
		    color='grey'
		    size='medium'
		    entities='events'
		/>
		<SelectOrdersButton {...rest}
			content='Заказанные тур-путешествия'
		    orders='adventures'
		    color='grey'
		    size='medium'
		    entities='adventures'
		/>
	</div>
);

export default ListSelectOrdersButtons;
