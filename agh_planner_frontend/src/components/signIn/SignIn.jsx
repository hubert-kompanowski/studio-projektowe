import React, {useState} from 'react';
import SignInForm from './SignInForm';
import { userService } from '../../services/userService';
import Axios from 'axios';

const SignIn = (props) => {

    const [state, setState] = useState({
        login: null,
        password: null
    });
    
    const handleSubmit = (e) => {
        e.preventDefault();
        Axios.post('/api/login', {
            email: state.email,
            password: state.password
        })
        .then(response => {
            userService.handleNewUserResponse(response);
            props.history.push("/home-page");
        })
        .catch(error => {
            userService.handleError(error);
        });
    };

    function handleChange(e) {
        const value = e.target.value;
        setState({
          ...state,
          [e.target.name]: value
        });
      }
    
    return (
        <SignInForm handleSubmit = {handleSubmit} handleChange = {handleChange} />
    );
}

export default SignIn;