import * as React from 'react';
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
import { Component } from 'react';

var today = new Date();
var currentDate = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
var schedulerData = [
  { startDate: '2020-06-12T09:00:00', endDate: '2020-06-12T11:00', title: 'Labki z Gierdziem', test: 'test' },
  { startDate: '2020-06-12T14:00', endDate: '2020-06-12T15:30', title: 'Labki z Nabagłem' },
  { startDate: '2020-06-12T14:00:00', endDate: '2020-06-12T15:30:00', title: 'Teoria kompilacji i kompilatory, Sala: B-1 316, Prowadzący: Radosław Klimek dr hab. inż., Grupa: 3, ' }
];

class Schedule extends Component{

  state = {
    user: localStorage.getItem('user')
  }

  render() {
    return (
        <Scheduler
      data={schedulerData}
    >

      <ViewState
        currentDate={currentDate}
      />
      <WeekView
        startDayHour={8}
        endDayHour={20}
        cellDuration={90}
      />
      <Appointments />
      <CurrentTimeIndicator
        updateInterval={1000}
      />
      {/* <Toolbar />
    <TodayButton /><DateNavigator /> */}
    </Scheduler>

    )
  }
}

export default Schedule;


// const Schedule = (props) => {

//   var today = new Date();
//   var currentDate = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
//   var schedulerData = [
//     { startDate: '2020-06-12T09:00:00', endDate: '2020-06-12T11:00', title: 'Labki z Gierdziem', test: 'test' },
//     { startDate: '2020-06-12T14:00', endDate: '2020-06-12T15:30', title: 'Labki z Nabagłem' },
//     { startDate: '2020-06-12T14:00:00', endDate: '2020-06-12T15:30:00', title: 'Teoria kompilacji i kompilatory, Sala: B-1 316, Prowadzący: Radosław Klimek dr hab. inż., Grupa: 3, ' }
//   ];

//   return (
//     <Scheduler
//       data={schedulerData}
//     >

//       <ViewState
//         currentDate={currentDate}
//       />
//       <WeekView
//         startDayHour={8}
//         endDayHour={20}
//         cellDuration={90}
//       />
//       <Appointments />
//       <CurrentTimeIndicator
//         updateInterval={1000}
//       />
//       {/* <Toolbar />
//     <TodayButton /><DateNavigator /> */}
//     </Scheduler>
//   );
// }
// export default Schedule
