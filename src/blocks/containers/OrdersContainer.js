import React, { Component } from 'react';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import PropTypes from 'prop-types';
import Orders from './../components/Orders';
import { selectOrders } from './../actions/OrderActions.js';

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

	handleChangeOrders = orders => {
		const { dispatch }  = this.props;

		dispatch(selectOrders(orders));
	};

	render () {
		return (
			<Orders {...this.props} />
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

	return {
		selectedOrders,
		selectedEntities,
		isFetching,
		entities,
		lastUpdated
	}
};

export default connect(mapStateToProps)(OrdersContainer);