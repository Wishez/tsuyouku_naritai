import React from 'react';
import SelectEntitiesButton from './SelectEntitiesButton';

const ListSelectEntitiesButtons = ({...rest}) => (
	<div>
		<SelectEntitiesButton {...rest}
			content='Заказанные мероприятия'
		    color='grey'
		    size='medium'
		    entities='events'
		/>
		<SelectEntitiesButton {...rest}
			content='Заказанные тур-путешествия'
		    color='grey'
		    size='medium'
		    entities='adventures'
		/>
		<SelectEntitiesButton {...rest}
			content='Список Артистов'
		    color='grey'
		    size='medium'
		    entities='artists'
		/>
		<SelectEntitiesButton {...rest}
			content='Список Клиентов'
		    color='grey'
		    size='medium'
		    entities='customers'
		/>
	</div>
);

export default ListSelectEntitiesButtons;
