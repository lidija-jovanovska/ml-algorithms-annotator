import React, {useState} from "react";
import ReactDOM from "react-dom";
import {
    Button,
    createTheme,
    Grid,
    makeStyles,
    MuiThemeProvider,
    Typography
} from "@material-ui/core";
import {BrowserRouter, Link, Route, Switch} from "react-router-dom";
import HomePage_v4 from "./HomePage_v4";
import Browse from "./Browse";

const theme = createTheme({
    palette: {
        type: 'light',
        primary: {
            main: '#268372',
        },
        secondary: {
            main: '#903454',
        },
    },
});

const useStyles = makeStyles((theme) => ({
    position: {
        position: "absolute",
        top: "50%",
        left: "50%",
        transform: "translate(-50%, -50%)",
        width: "70%",
        color: "white",
        textAlign: "justify",
    },
    button: {
        width: 200,
        height: 50,
        margin: theme.spacing(2),
    },
    typography: {
        color: '#272c2b'
    },
}));

function About() {
    const classes = useStyles();
    return (
        <div className={classes.position}>
            <Grid container justify={"center"}>
                <Typography component="h4" variant="h4" className={classes.typography}>
                    Welcome to The DM/ML Algorithm Annotation Tool!
                </Typography>
                <Typography component="h6" variant="h6" className={classes.typography}>
                    You can use the tool to create new annotations of Data Science and Machine Learning Algorithms
                    by navigating to the 'Annotate' page, or query a database of algorithm annotations via the 'Search'
                    page.
                </Typography>
                <Button size={"large"}
                        color={'primary'}
                        variant={"contained"}
                        component={Link}
                        to={'/annotate'}
                        className={classes.button}>
                    Annotate
                </Button>
                <Button
                    size={"large"}
                    color={'primary'}
                    variant={"contained"}
                    component={Link}
                    to={'/search'}
                    className={classes.button}>
                    Search
                </Button>
            </Grid>
        </div>
    );
}

export default function App() {
    return (
        <MuiThemeProvider theme={theme}>
            <BrowserRouter>
                <Switch>
                    <Route exact path="/" component={About}/>
                </Switch>
                <Switch>
                    <Route exact path="/annotate" component={HomePage_v4}/>
                </Switch>
                <Switch>
                    <Route exact path="/search" component={Browse}/>
                </Switch>
            </BrowserRouter>
        </MuiThemeProvider>
    );
}

ReactDOM.render(<App/>, document.getElementById("app"));
