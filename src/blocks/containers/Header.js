import React, { Component } from 'react';
import Logo from './../components/Logo';
import Navigation from './../components/Navigation'; 
 
const Header = () => (
  <header className='header'>
      <div className='container'>
        <Navigation />
      </div>
  </header>
);

export default Header;