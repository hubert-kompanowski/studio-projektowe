import CardMedia from '@material-ui/core/CardMedia';
import Drawer from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import { makeStyles } from '@material-ui/core/styles';
import { Calendar } from 'material-ui-pickers';
import React, { useState } from 'react';
import Scheduler from './mainPanel/Scheduler';




const drawerWidth = 240;


const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
    position: 'relative'
  },
  nested: {
    paddingLeft: theme.spacing(4),
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  toolbar: theme.mixins.toolbar,
}));

// const exampleText = 
//   <CardMedia>
//     <img src={background} alt="" width="1200px" />
//   </CardMedia>;



export default function MainHomeComponent() {
  const [toRender, setToRender] = useState();
  const classes = useStyles();
  const [open, setOpen] = React.useState(true);

  const handleClick = () => {
    setOpen(!open);
  };

  return (
    <div className={classes.root}>
      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <div className={classes.toolbar} />

        <List>
          <ListItem button onClick={() => setToRender(<Scheduler />)}>
            <ListItemIcon><Calendar /></ListItemIcon>
            <ListItemText primary="Scheduler" />
          </ListItem>
        </List>
      </Drawer>
      <main className={classes.content}>
        <div className={classes.toolbar} />
        {toRender}
      </main>
    </div>
  );
}