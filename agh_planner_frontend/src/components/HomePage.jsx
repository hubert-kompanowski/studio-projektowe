import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import React, { useEffect, useState } from 'react';
import Auth from './Auth';
import MainHomeComponent from './MainHomeComponent';
import TopNavBar from './TopNavBar';

const HomePage = (props) => {

    const [user, setUser] = useState({});
    
    useEffect(() => {
        setUser(JSON.parse(localStorage.getItem('user')));
    }, [])


    const signout = () => {
        localStorage.removeItem("user");
        Auth.signout();
        props.history.push('/');
    }

    const reloadHome = () => {
        props.history.push('/home-page');
    }
   
    return (
        <div>
            <TopNavBar firstName={user.first_name} lastName={user.last_name} signout={signout} reloadHome={reloadHome}/>
            <Box>
                <Grid container spacing={0} >
                    <Grid item xs={9}>
                    <MainHomeComponent />
                    </Grid>  
                </Grid>
            </Box>
            
        </div>
    );
}

export default HomePage;