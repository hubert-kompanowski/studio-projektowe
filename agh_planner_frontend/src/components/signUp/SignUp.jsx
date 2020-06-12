import React, {useState} from 'react';
import '../../App.css';
import SignUpForm from './SignUpForm'
import { userService } from '../../services/userService';
import Axios from 'axios';

const SignUp = (props) => {

  const [state, setState] = useState({
    user : {
      email: null,
      password: null,
      first_name: null,
      last_name: null
    }
  });

  const handleChange = (e) => {
    const {id, value} = e.target;
    setState(prevState => ({
      ...prevState,
      user : {
        ...prevState.user,
        [id] : value
      }
    }));
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    const user = {...state.user};
    
    Axios.post('/api/register', user)
    .then(response => {
      userService.handleNewUserResponse(response);
      props.history.push("/home-page");
    })
    .catch(error => {
      userService.handleError(error);
    });
  }

  return  <SignUpForm handleChange = {handleChange} handleSubmit = {handleSubmit}/>
}

export default SignUp;

