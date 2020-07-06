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
import { List, ListItem, ListItemText, Collapse, ListSubheader, ListItemSecondaryAction, Checkbox, Button } from '@material-ui/core';


class ListOfSubjects extends Component {

    state = {
        courses: [],
        choosenEvents: [],
    }

    constructor() {
        super()
        // this.state = { courses: [] }
        // this.state = {courses: [{name: "", events: []}]}
        this.getSubjects()

    }

    getSubjects() {
        Axios.get('/api/courses')
            .then(res => {
                // console.log(res.data.courses)
                const courses = res.data.courses

                this.setState({ courses: courses })
                console.log(this.state.courses)
            })

    }

    handleCheckboxChange(eventID) {
        if (this.state.choosenEvents.includes(eventID)) {
            let filteredArray = this.state.choosenEvents.filter(item => item !== eventID)
            this.setState({ choosenEvents: filteredArray });
        }
        else {
            var appendedArray = this.state.choosenEvents
            appendedArray.push(eventID)
            this.setState({ choosenEvents: appendedArray });
        }

        console.log("changed:")
        console.log(eventID)
        console.log(this.state.choosenEvents)

    }

    handleSubmit (){
        Axios.post('/api/set_plan/' + JSON.parse(localStorage.getItem('user')).id, {
            UserID : JSON.parse(localStorage.getItem('user')).id,
            EventsIDs: this.state.choosenEvents,
        })
        .then(response => {
            alert('choosen subjects send to server');
        })
        .catch(error => {
            alert('error');
        });
    };

    render() {

        return (
            <div>
                {/* {this.state.courses.map(course =>
                                                                                            course.events.map(event =>

                                                                                                <li>
                                                                                                    {event.info}, {event.id}
                                                                                                </li>
                                                                                            )
                                                                                        )} */}

                <Button variant="contained" color="primary" size="large" fullWidth ="true" onClick={() => { this.handleSubmit() }}>Submit Your choices</Button>

                {this.state.courses.map(course =>
                    <List subheader={<ListSubheader>{course.name}</ListSubheader>}>
                        {course.events.map((event) => {
                            return (
                                <ListItem key={event.info}>
                                    {/* <ListItemSecondaryAction> */}
                                    <Checkbox
                                        edge="start"
                                        // onChange={handleCheckboxChange(event.id)}
                                        onChange={() => this.handleCheckboxChange(event.id)}
                                    // checked={checked.indexOf(value) !== -1}
                                    />
                                    {/* </ListItemSecondaryAction> */}
                                    <ListItemText primary={event.info} />

                                </ListItem>
                            )
                        })}
                    </List>
                )}
            </div>
        );
    }
}

export default ListOfSubjects
// JSON.parse(localStorage.getItem('user')).id}


// {
//     "UserID": 15,
//     "EventsIDs": [1,2,3,4,5]
// }