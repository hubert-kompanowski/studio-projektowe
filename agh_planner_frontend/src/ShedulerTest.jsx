import * as React from 'react';
import Paper from '@material-ui/core/Paper';
import { ViewState } from '@devexpress/dx-react-scheduler';
import {
  Scheduler,
  Appointments,
  WeekView,
  CurrentTimeIndicator,
} from '@devexpress/dx-react-scheduler-material-ui';

var today = new Date();
var currentDate = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
var schedulerData = [
  { startDate: '2020-06-12T09:30', endDate: '2020-06-12T11:00', title: 'Labki z Gierdziem' },
  { startDate: '2020-06-12T14:00', endDate: '2020-06-12T15:30', title: 'Labki z Nabagłem' },
];

export default () => (
  <Paper>
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
    </Scheduler>
  </Paper>
);
