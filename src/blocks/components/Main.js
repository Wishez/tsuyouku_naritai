import React, { Component } from 'react'; 
import { Route } from 'react-router-dom'
import NotFound from './NotFound';

export default class Main extends Component {
  render() {
  	const { content } = this.props;
    return (
		  <main>         
		  	<Route exact path='/' component={NotFound} />
		  	<Route path='/second' component={NotFound} />
		  	<Route path='/third' component={NotFound} />
		  	<Route path='/fourth' component={NotFound} />
   		</main>
   	);
  }
}