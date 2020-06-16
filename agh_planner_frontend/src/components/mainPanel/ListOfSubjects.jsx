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


const ListOfSubjects = (props) => {

    
    var self = props;

    Axios.get("/api/courses")
        .then(response => {
            //TODO

        })

    // var self = this;
    // axios.get('/url')
    //     .then(function (response) {
    //         console.log(response);
    //         self.setState({ events: response.data })
    //     })
    //     .catch(function (error) {
    //         console.log(error);
    //     });
    // //the rest of the code
    // var a = 'i might be executed before the server responds'


    return (
        <div>
            test
        </div>
    );
}
export default ListOfSubjects
