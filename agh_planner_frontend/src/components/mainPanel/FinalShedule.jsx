import React, {Component} from 'react';
import Axios from "axios";
import {
    Appointments,
    CurrentTimeIndicator,
    Scheduler,
    WeekView
} from "@devexpress/dx-react-scheduler-material-ui";
import {ViewState} from "@devexpress/dx-react-scheduler";


var today = new Date();
var currentDate = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + (today.getDate());
var schedulerData = [
    {
        startDate: '2020-07-04T09:00:00',
        endDate: '2020-07-04T11:00',
        title: 'Labki z Gierdziem',
        test: 'test'
    },
    {
        startDate: '2020-07-04T14:00',
        endDate: '2020-07-04T15:30',
        title: 'Labki z Nabagłem'
    },
    {
        startDate: '2020-07-04T14:00:00',
        endDate: '2020-07-04T15:30:00',
        title: 'Teoria kompilacji i kompilatory, Sala: B-1 316, Prowadzący: Radosław Klimek dr hab. inż., Grupa: 3, '
    }
];

class FinalShedule extends Component {

    state = {
        user: localStorage.getItem('user'),
        schedule: []  // TODO: add here scheduler and uncomment below things
    }

    constructor() {
        super()
        this.getSchedule()
    }

    getSchedule() { // TODO: update api endpoint
      Axios.get('/api/get_plan')
            .then(res => {
                this.setState({schedule: res.data.data})
                console.log(schedulerData)
                console.log(this.state.schedule)

            })


    }


    render() {
        return (
            <Scheduler
                // data={schedulerData}
                data={this.state.schedule}
            >

                <ViewState
                    currentDate={currentDate}
                />
                <WeekView
                    startDayHour={8}
                    endDayHour={20}
                    cellDuration={90}
                />
                <Appointments/>

                <CurrentTimeIndicator
                    updateInterval={1000}
                />
                {/* <Toolbar />
    <TodayButton /><DateNavigator /> */}
            </Scheduler>

        )
    }
}

export default FinalShedule;