import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';
import Orders from './../components/Orders';
import { selectOrders, fetchEntitiesIfNeeded } from './../actions/OrderActions.js';

class OrdersContainer extends Component {
	static PropTypes = {
		selectedOrders: PropTypes.string.isRequired,
		selectedEntities: PropTypes.object.isRequired,
		entities: PropTypes.object.isRequired,
		isFetching: PropTypes.bool.isRequired,
		lastUpdated: PropTypes.number,
		dispatch: PropTypes.func.isRequired	
	};

	handleChangeEntity = (entity, id) => {

	};

	selectEntitiesInOrders = (orders, entities) => {
		const { dispatch }  = this.props;
		// console.log(this.props.selectedOrders);
		dispatch(fetchEntitiesIfNeeded(orders, entities));		
	};
	selectNeededOrders = orders => {

		const { dispatch }  = this.props;

		dispatch(selectOrders(orders));
	};

	render () {
		return (
			<Orders {...this.props}
				selectEntitiesInOrders={this.selectEntitiesInOrders}
				fetchEntities={this.fetchEntities}
				selectNeededOrders={this.selectNeededOrders}
			/>
		);	
	}
}

const mapStateToProps = state => {
	const { 
		selectedOrders,
		selectedEntities,
		ordersByData
	} = state;
	const {
		isFetching,
		lastUpdated,
		entities
	} = ordersByData[selectedOrders] || {
		isFetching: true,
		entities: {
			employers: {},
			customers: {},
			artists: {},
			places: {},
			contractors: {},
			visa: {},
			events: {},
			adventures: {},
			partners: {},
			halls: {}
		}
	}
	console.log(state);
	return {
		selectedOrders,
		selectedEntities,
		isFetching,
		entities,
		lastUpdated
	}
};

export default connect(mapStateToProps)(OrdersContainer);