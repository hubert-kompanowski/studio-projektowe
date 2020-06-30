import * as React from 'react';
import useState from 'react'
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import { ViewState } from '@devexpress/dx-react-scheduler';
import {
    Scheduler,
    Appointments,
    WeekView,
    CurrentTimeIndicator,
    Toolbar,
    TodayButton,
    DateNavigator,
} from '@devexpress/dx-react-scheduler-material-ui';
import Axios from 'axios';
import { Component } from 'react';
import { List, ListItem } from '@material-ui/core';


class ListOfSubjects extends Component {

    state = {
        listOfSubjects: [],
    }

    componentDidMount() {
        this.getSubjects()

    }

    getSubjects() {
        Axios.get('/api/courses')
            .then(res => {
                this.setState({ listOfSubjects: res.data })
                console.log(res)
            })
            
    }

    render() {
        return (
            <div>
                test
                {/* <List>
                    <ListItem>
                    
                    </ListItem>
                </List> */}
            </div>
        );
    }
}

export default ListOfSubjects
// JSON.parse(localStorage.getItem('user')).id}