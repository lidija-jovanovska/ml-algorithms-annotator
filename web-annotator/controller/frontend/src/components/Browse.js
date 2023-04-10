import React, {useEffect, useState} from "react";
import {Button, Card, FormControl, Grid, InputLabel, makeStyles, MenuItem, Select, Typography} from "@material-ui/core";
import Container from "./DropdownContainer";
import tasks from "../../static/annotation-schema/tasks.json";
import optimization_problems from "../../static/annotation-schema/optimization_problems.json";
import MaterialTable from "material-table";

const axios = require('axios').default;

const complexities = [
    'None',
    'Constant complexity - O(1)',
    'Inverse Ackermann complexity - O(α(n))',
    'Iterated logarithmic complexity - O(log* n)',
    'Log-logarithmic complexity - O(log log n)',
    'Logarithmic complexity - O(log n)',
    'Polylogarithmic complexity - poly(log n)',
    'Fractional power complexity - O(n^c)',
    'Linear complexity - O(n)',
    'n log-star n" complexity - O(n log* n)',
    'Linearithmic complexity - O(n log n)',
    'Quasilinear complexity - n poly(log n)',
    'Quadratic complexity - O(n^2)',
    'Cubic complexity - O(n^3)',
    'Polynomial complexity - 2^(O(log n)) = poly(n)',
    'Quasi-polynomial complexity - 2^(poly(log n))',
    'Sub-exponential complexity (first definition) - O(2^n^ε)',
    'Sub-exponential complexity (second definition) - 2^o(n)',
    'Exponential complexity (with linear exponent) - 2^O(n)',
    'Exponential complexity - 2^poly(n)',
    'Factorial complexity - O(n!)',
    'Double exponential complexity - 2^(2^poly(n))'
];

const useStyles = makeStyles((theme) => ({
    main: {
        position: "absolute",
        height: "100%",
        width: "70%",
        top: "10%",
        left: "15%",
    },
}));

export default function Browse() {

    const classes = useStyles();

    const [SearchData, setSearchData] = useState([]);
    const columns = [
        {title: 'ID', field: 'id', type: 'numeric'},
        {title: 'Algorithm Name', field: 'name'},
        {title: 'Complexity', field: 'complexity'},
        {title: 'Task', field: 'task'},
        {title: 'Optimization Problem', field: 'optimization_problem'},
    ];

    const [TrainTimeComplexity, setTrainTime] = useState('');
    const [Task, setTask] = useState('');
    const [OptimizationProblem, setOptimizationProblem] = useState('');

    useEffect(() => {
        console.log(Task);
        console.log(OptimizationProblem);
        console.log(TrainTimeComplexity);
    });

    const onChange = (currentNode, selectedNodes) => {
        if (currentNode.label.includes("task")) {
            if (selectedNodes.length > 0) {
                setTask(selectedNodes[0].label);
            }
            else {
                setTask('');
            }
        } else {
            if (selectedNodes.length > 0) {
                setOptimizationProblem(selectedNodes[0].label);
            }
            else {
                setOptimizationProblem('');
            }
        }
    };

    function filterAlgorithms() {

        axios.get('api/algorithms/', {
            params: {
                complexity: TrainTimeComplexity,
                task: Task,
                optimization_problem: OptimizationProblem
            }
        }).then(response => {
            setSearchData(response.data);
            console.log(SearchData);

        });
    }

    return (
        <Card className={classes.main}>
            {/*<Typography variant="h4" align="left">*/}
            {/*    Filter Algorithms*/}
            {/*</Typography>*/}
            <Grid container spacing={3} justify={"space-evenly"}>
                <Grid item xs={12}>
                    <Container
                        data={tasks}
                        onChange={onChange}
                        texts={{placeholder: 'Task'}}
                        className="mdl-demo"
                        mode="radioSelect"
                    />
                </Grid>
                <Grid item xs={12}>
                    <Container
                        data={optimization_problems}
                        onChange={onChange}
                        texts={{placeholder: 'Optimization Problem'}}
                        className="mdl-demo"
                        mode="radioSelect"
                    />
                </Grid>
                <Grid item xs={12}>
                    <FormControl fullWidth size="small" variant="outlined">
                        <InputLabel shrink>Train Time Complexity</InputLabel>
                        <Select
                            onChange={e => setTrainTime(e.target.value)}>
                            {complexities.map((TrainTimeComplexity) => (
                                <MenuItem key={TrainTimeComplexity} value={TrainTimeComplexity}>
                                    {TrainTimeComplexity}
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </Grid>
                <Grid container alignItems="center" justifyContent="center" justify="flex-end">
                    <Grid item xs={4}>
                        <Button size={"large"}
                                color={'primary'}
                                variant={"contained"}
                                onClick={filterAlgorithms}>
                            Filter
                        </Button>
                    </Grid>
                    <Grid item xs={4}>
                        <Button size={"large"}
                                color={'secondary'}
                                variant={"contained"}
                                onClick={e => setSearchData([])}>
                            Clear
                        </Button>
                    </Grid>
                </Grid>
                <Grid item xs={12}>
                    <MaterialTable
                        title={'Algorithms'}
                        data={SearchData}
                        columns={columns}
                        options={{
                            exportButton: true,
                        }}
                    />
                </Grid>
            </Grid>
        </Card>
    );
}
