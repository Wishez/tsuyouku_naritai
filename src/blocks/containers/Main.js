import React, { Component } from 'react'; 
import { Route } from 'react-router-dom'
import NotFound from './../components/NotFound';

const Main = () => (
  <main>         
  	<Route exact path='/' component={NotFound} />
  	<Route path='/second' component={NotFound} />
  	<Route path='/third' component={NotFound} />
  	<Route path='/fourth' component={NotFound} />
	</main>
);

export default Main;