import React, { Component } from 'react';
import Header from './Header';
import Footer from './Footer';
import Main from './Main';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { fetchEntitiesIfNeeded } from './../actions/OrderActions.js';  


class App extends Component {
	static PropTypes = {
		selectedOrders: PropTypes.string.isRequired,
		selectedEntities: PropTypes.object.isRequired,
		entities: PropTypes.object.isRequired,
		isFetching: PropTypes.bool.isRequired,
		lastUpdated: PropTypes.number,
		dispatch: PropTypes.func.isRequired	
	};

	componentDidMount() {
		const { entities, selectedOrders, dispatch } = this.props;
		dispatch(fetchEntitiesIfNeeded(selectedOrders, 'events'));
		
	}

	componentWillReceiveProps(nextProps) {
		if (nextProps.selectedOrders !== this.props.selectedOrders){
			// const { entities, selectedOrders, dispatch } = this.props;
			// switch (nextProps.selectedOrders) {
			// 	case 'events':
			// 		dispatch(fetchEntitiesIfNeeded(selectedOrders, 'events'));
			// 	case 'adventures':
			// 		dispatch(fetchEntitiesIfNeeded(selectedOrders, 'adventures'));			
			// 		break;
			// 	default:
			// 		dispatch(fetchEntitiesIfNeeded(selectedOrders, 'events'));
			// 		break;
			// }
			
		}

	}

	render() {
		return (
			<div>
		    	<Header />
		    	<Main />	
		    	<Footer />
		    </div>
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
	};

	return {
		selectedOrders,
		selectedEntities,
		entities,
		isFetching,
		lastUpdated
	};
};


export default withRouter(connect(mapStateToProps)(App));

