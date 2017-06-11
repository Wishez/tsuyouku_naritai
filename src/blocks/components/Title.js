import React, { Component } from 'react';
import ReactHtmlParser from 'react-html-parser';

export default class Title extends Component{
	render() {
		const { text, block } = this.props;
		return (
			<h2 className={block + '__title title'}>
				{ ReactHtmlParser(text) }
			</h2>
		);
	}
}