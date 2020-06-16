import * as React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';
import Logo from './assets/aghPlannerLogo.png';
import Public from './components/Public';
import SignIn from './components/signIn/SignIn';
import SignUp from './components/signUp/SignUp';
import Schedule from './components/mainPanel/Schedule';
import Auth from './components/Auth';
import PrivateRoute from './components/PrivateRoute';
import HomePage from './components/HomePage';



const App = () => {
    return (
      <BrowserRouter>
        <div className="App">
          <div className="App-header">
            <img src={Logo} alt="logo" width={350}/>
          </div>
          
          <Switch>
            <Route path='/' exact component={Public}/>
            <Route path='/sign-in' component={SignIn}/>
            <Route path='/sign-up' component={SignUp}/>
            <PrivateRoute authenticated={Auth.getAuth()} exact path="/home-page" component={HomePage} />
          </Switch>
        </div>
      </BrowserRouter>
    );
}

export default App;
