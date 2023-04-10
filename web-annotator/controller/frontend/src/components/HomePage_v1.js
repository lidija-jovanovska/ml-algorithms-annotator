import React, {Component, useState} from "react";
import {
    Grid,
    Button,
    Typography,
    TextField,
    Paper,
    FormHelperText, FormControl, withStyles, Switch,
    Select, MenuItem, InputLabel, Input
} from "@material-ui/core";
import 'react-dropdown-tree-select/dist/styles.css';
import DropdownTreeSelect from "react-dropdown-tree-select";
import tasks from "../../static/annotation-schema/tasks.json";
import datasets from "../../static/annotation-schema/datasets.json";
import optimization_problems from "../../static/annotation-schema/optimization_problems.json";


const assumptions = [
    "No Assumptions",
    "Linear Relationship (between independent and dependent variables)",
    "Multivariate Normality (of all the variables)",
    "Feature Independence",
    "Autocorrelation (little or none at all)",
    "Homoscedasticity (Error term is the same across all values of the independent variables",
    "Normal distribution of Error Terms",
    "Spherical Cluster Shape",
    "Similar-Size Clusters",
    "Conditional Independence",
    "Conditional Feature Independence",
    "Linear Relationship (between the logit of the outcome and each predictor variables)",
    "Stationarity (mean, variance, and autocorrelation structure do not change over time)",

]

const AntSwitch = withStyles((theme) => ({
    root: {
        width: 28,
        height: 16,
        padding: 0,
        display: 'flex',
    },
    switchBase: {
        padding: 2,
        color: theme.palette.grey[500],
        '&$checked': {
            transform: 'translateX(12px)',
            color: theme.palette.common.white,
            '& + $track': {
                opacity: 1,
                backgroundColor: theme.palette.primary.main,
                borderColor: theme.palette.primary.main,
            },
        },
    },
    thumb: {
        width: 12,
        height: 12,
        boxShadow: 'none',
    },
    track: {
        border: `1px solid ${theme.palette.grey[500]}`,
        borderRadius: 16 / 2,
        opacity: 1,
        backgroundColor: theme.palette.common.white,
    },
    checked: {},
}))(Switch);

export default class HomePage_v1 extends Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedNodes: [],
            BatchMode: "true",
            EnsembleMode: "false",
        };
        this.assignObjectPaths(tasks);
        this.assignObjectPaths(datasets);
    }

    assignObjectPaths = (obj, stack) => {
        Object.keys(obj).forEach(k => {
            const node = obj[k];
            if (typeof node === "object") {
                node.path = stack ? `${stack}.${k}` : k;
                this.assignObjectPaths(node, node.path);
            }
        });
    };

    onChange = (currentNode, selectedNodes) => {
        console.log("path: ", currentNode.path);
        console.log("Selected nodes: ", selectedNodes);
        // setState messes up the style
        // this.setState({selectedNodes: selectedNodes},
        //     () => {
        //         console.log("Currently Selected Nodes: ", this.state.selectedNodes);
        //     });
    }

    render() {
        return (
            <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 25}}>
                <Paper elevation={2}>
                    <Grid item xs={12}>
                        <Typography component={"h4"} variant={"h4"}>
                            Manual Web Tool for Semantic Annotation of DM & ML Algorithms
                        </Typography>
                    </Grid>
                    <Grid container spacing={3}>
                        <Grid item xs={12}>
                            <FormControl>
                                <TextField
                                    color={"primary"}
                                    fullWidth={true}
                                    variant={"outlined"}
                                    label={"Algorithm Name"}
                                    size={"small"}
                                    InputLabelProps={{shrink: true}}>
                                </TextField>
                                <FormHelperText>
                                    <div align={"center"}>
                                        Name of DM-Algorithm
                                    </div>
                                </FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid item xs={6}>
                            <FormControl>
                                <TextField
                                    color={"primary"}
                                    fullWidth={true}
                                    variant={"outlined"}
                                    label={"Document Name"}
                                    size={"small"}
                                    InputLabelProps={{shrink: true}}>
                                </TextField>
                                <FormHelperText>
                                    <div align={"center"}>
                                        Name of the Document where the Algorithm is described.
                                    </div>
                                </FormHelperText>
                            </FormControl>
                        </Grid>
                        <Grid item xs={6}>
                            <FormControl>
                                <TextField
                                    color={"primary"}
                                    fullWidth={true}
                                    variant={"outlined"}
                                    label={"Document ID"}
                                    size={"small"}
                                    InputLabelProps={{shrink: true}}>
                                </TextField>
                                <FormHelperText>
                                    <div align={"center"}>
                                        DOI/ISBN of the Document where the Algorithm is described.
                                    </div>
                                </FormHelperText>
                            </FormControl>
                        </Grid>
                    </Grid>
                    {/*Dataset + Mode + Task*/}
                    <Grid container direction="row" justify="space-evenly" alignItems="center">
                        <Grid item xs={4}>
                            <DropdownTreeSelect
                                data={datasets}
                                onChange={this.onChange}
                                texts={{placeholder: 'Dataset'}}
                            />
                        </Grid>
                        <Grid item xs={4}>
                            <DropdownTreeSelect
                                data={tasks}
                                onChange={this.onChange}
                                texts={{placeholder: 'Task'}}
                            />
                        </Grid>
                        <Grid item xs={4}>
                            <Typography component="div">
                                <Grid component="label" container alignItems="center" spacing={1}>
                                    <Grid item>Batch</Grid>
                                    <Grid item>
                                        <AntSwitch checked={this.state.BatchMode}
                                                   onChange={(e) => this.setState(prevState => ({
                                                       BatchMode: !prevState.BatchMode
                                                   }))}
                                                   name="OperatingMode"/>
                                    </Grid>
                                    <Grid item>Online</Grid>
                                </Grid>
                            </Typography>
                        </Grid>
                    </Grid>
                    <Grid container direction="row" justify="space-evenly" alignItems="center">
                        <Grid item xs={6}>
                            <FormControl fullWidth size="small" variant="outlined">
                                <InputLabel shrink>Generalization Language Specification</InputLabel>
                                <Select>
                                    <MenuItem value={1}>Language of Bayesian Nets</MenuItem>
                                    <MenuItem value={2}>Language of Decision Rules</MenuItem>
                                    <MenuItem value={3}>Language of Decision Trees</MenuItem>
                                    <MenuItem value={4}>Language of Graphical Models</MenuItem>
                                    <MenuItem value={5}>Language of Markov Chains</MenuItem>
                                    <MenuItem value={6}>Language of Neural Nets</MenuItem>
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item xs={4}>
                            <Typography component="div">
                                <Grid component="label" container alignItems="center" spacing={1}>
                                    <Grid item>Ensemble</Grid>
                                    <Grid item>
                                        <AntSwitch checked={this.state.EnsembleMode}
                                                   onChange={(e) => this.setState(prevState => ({
                                                       EnsembleMode: !prevState.EnsembleMode
                                                   }))}
                                                   name="EnsembleMode"/>
                                    </Grid>
                                    <Grid item>Single Generalization</Grid>
                                </Grid>
                            </Typography>
                        </Grid>
                    </Grid>
                    <Grid item xs={12}>
                        <DropdownTreeSelect
                            data={optimization_problems}
                            onChange={this.onChange}
                            texts={{placeholder: 'Optimization Problem'}}
                        />
                    </Grid>
                    {/*Generalization language spec + Ensemble toggle*/}
                    {/*<Grid container direction={"row"} justify={"space-evenly"} alignItems={"center"}>*/}
                    {/*    <FormControl className={classes.formControl}>*/}
                    {/*        <InputLabel id="demo-mutiple-checkbox-label">Tag</InputLabel>*/}
                    {/*        <Select*/}
                    {/*            labelId="demo-mutiple-checkbox-label"*/}
                    {/*            id="demo-mutiple-checkbox"*/}
                    {/*            multiple*/}
                    {/*            value={personName}*/}
                    {/*            onChange={handleChange}*/}
                    {/*            input={<Input/>}*/}
                    {/*            renderValue={(selected) => selected.join(', ')}*/}
                    {/*            MenuProps={MenuProps}*/}
                    {/*        >*/}
                    {/*            {names.map((name) => (*/}
                    {/*                <MenuItem key={name} value={name}>*/}
                    {/*                    <Checkbox checked={personName.indexOf(name) > -1}/>*/}
                    {/*                    <ListItemText primary={name}/>*/}
                    {/*                </MenuItem>*/}
                    {/*            ))}*/}
                    {/*        </Select>*/}
                    {/*    </FormControl>*/}
                    {/*</Grid>*/}
                </Paper>
            </Grid>
        )
    }
}