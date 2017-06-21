import React, { Component } from 'react'; 
import { Switch, Route } from 'react-router-dom'
import NotFound from './../components/NotFound';
import OrdersContainer from './OrdersContainer';
import FadeIn from 'react-fade-in';

const FadingRoute = ({component: Component, ...rest }) => (
	<Route {...rest} render={props => (
		<FadeIn>
			<Component {...props} />
		</FadeIn>
	)}/>
);

const Home = () => (
	<FadeIn>
		<div>Home page!</div>
	</FadeIn>
);

const Adventures = () => (
	<FadeIn>
		<div>Adventures page!</div>
	</FadeIn>
);

const VisaForm = () => (
	<FadeIn>
		<div>Adventures page!</div>
	</FadeIn>
);
// render={props => <Orders {...props} />} />
		  		// <Route path='/orders' component={Orders} />
const Main = ({
	selectedOrders,
	selectedEntities,
	entities,
	isFetching,
	lastUpdated,
	dispatch
}) => (
   <main> 
   		<div className='container'>  
	   	   	<Switch>
		  		<Route exact path='/' component={Home} />
		  		<Route path='/orders' component={OrdersContainer} />
		  		<Route path='/adventures' component={Adventures} />
		  		<Route path='/register_visa' component={VisaForm} />
		  		<Route component={NotFound} />
		  	</Switch>
	  	</div>
   </main>
);

export default Main;