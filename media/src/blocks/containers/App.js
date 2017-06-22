import React, { Component } from 'react';
import Header from './Header';
import Footer from './Footer';
import Main from './Main';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { fetchEntitiesIfNeeded } from './../actions/EntitiesActions.js';  


class App extends Component {
	static PropTypes = {
		selectedEntities: PropTypes.string.isRequired,
		dispatch: PropTypes.func.isRequired	
	};

	componentDidMount() {
		const { selectedEntities, dispatch } = this.props;

		dispatch(fetchEntitiesIfNeeded(selectedEntities));
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
	const { selectedEntities } = state;

	return { selectedEntities };
};


export default withRouter(connect(mapStateToProps)(App));

