import Auth from '../components/Auth';

export const userService = {
    handleError,
    handleNewUserResponse,
    handleUserChange
};

function handleError(error) {
    console.log(error.message);
    if (error.response && error.response.status === 404) {
        alert("Invalid email or password");
    } else {
        alert("5xx server error");
    }
}

function handleNewUserResponse(response) {
    const user = response.data;
    console.log(user);
    localStorage.setItem('user', JSON.stringify(user));
    // localStorage.setItem('mainUser', JSON.stringify(user));
    Auth.authenticate();
}

function handleUserChange(user) {
    localStorage.setItem('user', JSON.stringify(user));
    Auth.authenticate();
}