import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';
import Orders from './../components/Orders';
import { 
	selectEntities,
	fetchEntitiesIfNeeded,
	selectEntity,
	invalidateEntities 
} from './../actions/EntitiesActions.js';
import { entitiesPattern } from './../constants/entities.js';

class OrdersContainer extends Component {
	static PropTypes = {
		selectByEntity: PropTypes.object.isRequired,
		selectedEntities: PropTypes.string.isRequired,
		entities: PropTypes.object.isRequired,
		isFetching: PropTypes.bool.isRequired,
		lastUpdated: PropTypes.number,
		dispatch: PropTypes.func.isRequired	
	};
	componentDidMount() {
		const { selectedEntities, dispatch } = this.props;

		dispatch(fetchEntitiesIfNeeded(selectedEntities));
	}

	selectNeededEntity = (entity, id) => {
		const { dispatch }  = this.props;
		dispatch(selectEntity(entity, id));
	};

	selectAndUpdateEntities = entities => {
		const { dispatch }  = this.props;

		dispatch(invalidateEntities());
		// Выбранные сущности обновляются внутри.
		dispatch(fetchEntitiesIfNeeded(entities));		
	};

	render () {
		return (
			<Orders {...this.props}
				selectNeededEntity={this.selectNeededEntity}
				fetchEntities={this.fetchEntities}
				selectAndUpdateEntities={this.selectAndUpdateEntities}
			/>
		);	
	}
}

const mapStateToProps = state => {
	const { 
		selectByEntity,
		selectedEntities,
		entities
	} = state;

	const {
		employers,
		customers,
		artists,
		places,
		contractors,
		visa,
		events,
		adventures,
		partners,
		halls,
		barters
	} = entities;

	const loadedEntities = {
		employers: {...employers},
		customers: {...customers},
		artists: {...artists},
		places: {...places},
		contractors: {...contractors},
		visa: {...visa},
		events: {...events},
		adventures: {...adventures},
		partners: {...partners},
		halls: {...halls},
		barters: {...barters}
	};

	const {
		isFetching,
		lastUpdated
	} = entities || {
		isFetching: true,
		loadedEntities: {
			...entitiesPattern
		}
	};

	console.log(state);
	return {
		selectByEntity,
		selectedEntities,
		isFetching,
		loadedEntities,
		lastUpdated
	}
};

export default withRouter(connect(mapStateToProps)(OrdersContainer));