import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import IconButton from '@material-ui/core/IconButton';
import Typography from '@material-ui/core/Typography';
import { ExitToApp, Settings } from '@material-ui/icons';


const useStyles = makeStyles(theme => ({
    root: {
      flexGrow: 1,
    },
    menuButton: {
      marginRight: theme.spacing(2),
    },
    title: {
        textAlign: 'left',
      flexGrow: 1,
      display: 'block',
    },
}));

const TopNavBar = (props) => {
    const signout = props.signout;
    const classes = useStyles();
    const name = props.name;
    const last_name = props.last_name;
    const id = props.id;
    const [anchorEl, setAnchorEl] = React.useState(null);
    const open = Boolean(anchorEl);
    
    const handleMenu = event => {
        setAnchorEl(event.currentTarget);
    };

    return (
        <AppBar position="static">
            <Toolbar>
                <Typography id = "greetings_text" variant="h6" className={classes.title}>
                Hi {name} {last_name} id [{id}]!
                </Typography>
                <IconButton color="inherit" onClick={handleMenu}>
                    <Settings/>
                </IconButton>
                <IconButton id="sign_out_button" color="inherit" onClick={signout}>
                    <ExitToApp/>
                </IconButton>
            </Toolbar>
        </AppBar>
    );
}
export default TopNavBar;