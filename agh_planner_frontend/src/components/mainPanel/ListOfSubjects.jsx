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
        // courses: [],
    }

    componentDidMount() {
        this.getSubjects()

    }

    getSubjects() {
        Axios.get('/api/courses')
            .then(res => {
                const courses = res.data
                this.setState({ courses })
                console.log(courses)
            })

    }

    render() {
        return (
            <ul>
                {this.state.courses.map(course =>
                    <li key={course.name}>
                        {
                            course.name
                                // course.map(event =>
                                // <li key={event.id}>
                                //     {event.info}
                                // </li>)
                        }
                    </li>
                )}
            </ul>

        );
    }
}

export default ListOfSubjects
// JSON.parse(localStorage.getItem('user')).id}