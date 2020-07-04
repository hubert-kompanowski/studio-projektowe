import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import React, { useEffect, useState } from 'react';
import Auth from './Auth';
import Schedule from './mainPanel/Schedule';
import ListOfSubjects from './mainPanel/ListOfSubjects';
import MyPlannedSubjects from './mainPanel/MyPlannedSubjects';

import TopNavBar from './TopNavBar';
import { Link, Route, Switch } from "react-router-dom";
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import CardMedia from '@material-ui/core/CardMedia';
import aghPlannerLogo from '../assets/agh_logo.jpg';

import { styled } from '@material-ui/core/styles';
import FinalShedule from './mainPanel/FinalShedule';
import OfficialRegistration from './mainPanel/OfficialRegistration';




const exampleText =
    <CardMedia>
        <img src={aghPlannerLogo} alt="" />
    </CardMedia>;

const StyledList = styled(List)({
    background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',

});

const HomePage = (props) => {
    const [toRender, setToRender] = useState(exampleText);
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
            <TopNavBar name={user.name} last_name={user.lastname} id={user.id} signout={signout} reloadHome={reloadHome} />
            <Box>
                <div class="sidebar">
                    <Grid>
                        <List>
                            {/* global schedule */}
                            <ListItem button onClick={() => setToRender(<Schedule />)}>
                                Global Shedule
                                    </ListItem>
                            <ListItem button onClick={() => setToRender(<ListOfSubjects />)}>
                                Plan Your Subjects
                                    </ListItem>
                            {/* planned schedule */}
                            <ListItem button onClick={() => setToRender(<MyPlannedSubjects />)}>
                                My Planned Subjects
                                    </ListItem>
                            {/* forms iframe */}
                            <ListItem button onClick={() => setToRender(<OfficialRegistration />)}>
                                Official registration for classes
                                    </ListItem>
                            {/* final schedule after g forms */}
                            <ListItem button onClick={() => setToRender(<FinalShedule />)}>
                                My Final Schedule
                                    </ListItem>

                        </List>
                    </Grid>
                </div>
                <div class="landing_page">
                    <Grid item>
                        {toRender}
                    </Grid>
                </div>
            </Box>

        </div>
    );
}

export default HomePage;