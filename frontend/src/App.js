import React from 'react';
import {Route, Switch} from "react-router-dom";
import Home from './components/home/Home'
import Login from './components/login/Login'

import './App.css';

function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/login" component={Login} />
      </Switch>
    </div>
  );
}

export default App;
