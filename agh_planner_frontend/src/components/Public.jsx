import * as React from 'react';
import '../App.css';
import Button from '@material-ui/core/Button';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Icon from '@material-ui/core/Icon';



const Public = () => {
    
    return (
        <div className = "container" >
            <ButtonGroup variant="contained" color="primary" size="large" fullWidth ="true">
                <Button id="sign_in_button" href="/sign-in" endIcon={<Icon>account_circle</Icon>} >
                    Log in
                </Button>
                <Button id="sign_up_button" href="/sign-up" endIcon={<Icon>person_add</Icon>}>
                    Register
                </Button>
            </ButtonGroup>
        </div>
    );
}

export default Public;
