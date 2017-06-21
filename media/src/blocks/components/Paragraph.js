import React, { Component } from 'react';
import ReactHtmlParser from 'react-html-parser';

export default class Paragraph extends  Component {
	render() {
		const { text, block } = this.props;
		return (
			<p className={block + '__paragraph paragraph'}>
				{ ReactHtmlParser(text) }
			</p>
		);
	}
}