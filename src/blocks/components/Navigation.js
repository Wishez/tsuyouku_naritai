import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import classNames from 'classnames';
import { Icon } from 'semantic-ui-react';

export default class Navigation extends Component {
  constructor(props) {
    super(props);
    
    this.state = {
        isOpen: false,
        activAbout: false,
        activeEvents: false,
        activeAdvantures: false,
        registerVisa: false
    };

    this.getActiveClass = this.getActiveClass.bind(this);
    this.openMenu = this.openMenu.bind(this);
    this.changeActiveEvents = this.changeActiveEvents.bind(this);
    this.changeActiveMain = this.changeActiveMain.bind(this);
    this.changeActiveAdvantures = this.changeActiveAdvantures.bind(this);
    this.changeRegisterVisa = this.changeRegisterVisa.bind(this);
    this.cleanActiveState = this.cleanActiveState.bind(this);
  }
  
  openMenu() {
    let $navList = $('#navList');
    
    if (!this.state.isOpen) {
      this.setState({isOpen: true});
      $navList.show('fast');
    } else {
      this.setState({isOpen: false});
      $navList.hide('fast');
    }
  }

  cleanActiveState() {
    this.setState({
      activeMain: false,
      activeEvents: false,
      activeAdvantures: false,
      registerVisa: false
    });

  }

  changeActiveMain() {
    this.cleanActiveState();

    this.setState({activeMain: true});
  }
  changeActiveEvents() {
    this.cleanActiveState();

    this.setState({activeEvents: true});
  }
  changeActiveAdvantures() {
    this.cleanActiveState();

    this.setState({activeAdvantures: true});

  }
  changeRegisterVisa() {
    this.cleanActiveState();

    this.setState({registerVisa: true});

  }

  componentDidMount() {
    this.changeActiveMain();
  }

   
  render() {

    const { activeMain, activeEvents, activeAdvantures, registerVisa } = this.state;

    return (
        <nav className='navigaton'>
          <button id='openMenuButton'
            className='navigation__openMenuButton visible-xs'
            onClick={this.openMenu}>
            <span className='sr-only'> 
              Toggle navigation
            </span>
            <Icon name='bars' />
          </button>
          <ul className='navList'
              id='navList'>
            <li className={this.getActiveClass(activeMain)}>
              <Link to='/'
                className='navItem__refer'
                onClick={this.changeActiveMain}>
                Главная
              </Link>
            </li>
            <li className={this.getActiveClass(activeEvents)}>
              <Link to='/orders'
                className='navItem__refer'
                onClick={this.changeActiveEvents}>
                Заказы
              </Link>
            </li>
            <li className={this.getActiveClass(activeAdvantures)}>
              <Link to='/adventures'
                className='navItem__refer'
                onClick={this.changeActiveAdvantures}>
                Не Путешествия
              </Link>
            </li>
            <li className={this.getActiveClass(registerVisa)}>
              <Link to='/register_visa' 
                className='navItem__refer'
                onClick={this.changeRegisterVisa}>
                Оформить визу
              </Link>
            </li>
          </ul>
        </nav>
    );
  }


  getActiveClass(state) {
    return  classNames({
      'navItem': true,
      'active': state
    });

  }
}