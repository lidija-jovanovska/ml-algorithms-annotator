import React, {useState} from "react";
import {Card, FormControl, Grid, InputLabel, MenuItem, Paper, Select, TextField, Typography} from "@material-ui/core";
import Container from "./DropdownContainer";
import optimization_problems from "../../static/annotation-schema/optimization_problems.json";

const complexities = [
    'None',
    'constant time - O(1)',
    'inverse Ackermann time - O(α(n))',
    'iterated logarithmic time - O(log* n)',
    'log-logarithmic time - O(log log n)',
    'logarithmic time - O(log n)',
    'polylogarithmic time - poly(log n)',
    'fractional power - O(n^c)',
    'linear time - O(n)',
    'n log-star n time - O(n log* n)',
    'linearithmic time - O(n log n)',
    'quasilinear time - n poly(log n)',
    'quadratic time - O(n^2)',
    'cubic time - O(n^3)',
    'polynomial time - 2^(O(log n)) = poly(n)',
    'quasi-polynomial time - 2^(poly(log n))',
    'sub-exponential time - O(2^n^ε)',
    'exponential time (with linear exponent) - 2^O(n)',
    'exponential time - 2^poly(n)',
    'factorial time - O(n!)',
    'double exponential time - 2^(2^poly(n))'
];


export default function Complexity({
                                       setOpProblems,
                                       setOpProblemText,
                                       setOpProblemMaths,
                                       setTrainTimeComplexity,
                                       setTrainTimeComplexityMathsNotation}) {

    const [TrainTimeComplexity, setTrainTime] = useState('');
    // const [TestTimeComplexity, setTestTime] = useState('');
    // const [SpaceComplexity, setSpace] = useState('');

    const set_train = (train) => {
        setTrainTime(train);
        setTrainTimeComplexity(train);
    };

    const onChange = (currentNode, selectedNodes) => {
        setOpProblems(selectedNodes);
    };

    // const set_test = (test) => {
    //     setTestTime(test);
    //     setTestTimeComplexity(test);
    // };
    // const set_space = (space) => {
    //     setSpace(space);
    //     setSpaceComplexity(space);
    // };

    return (
        <Card>
            <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 30}}>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Objective Function
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <Container
                        data={optimization_problems}
                        onChange={onChange}
                        texts={{placeholder: 'Objective Function'}}
                        className="mdl-demo"
                        mode={"radioSelect"}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Objective Function Text Description'}
                        InputLabelProps={{shrink: true}}
                        helperText={"Describe the algorithm objective function with text."}
                        variant={"outlined"}
                        onChange={e => setOpProblemText(e.target.value)}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Objective Function Maths Description (latex)'}
                        InputLabelProps={{shrink: true}}
                        helperText={"Describe the algorithm objective function with maths notation (latex)."}
                        variant={"outlined"}
                        onChange={e => setOpProblemMaths(e.target.value)}
                    />
                </Grid>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Time Complexity
                    </Typography>
                </Grid>
                <Grid item xs={12} style={{minHeight: 80, minWidth: 500}}>
                    <FormControl fullWidth size="small" variant="outlined">
                        <InputLabel shrink >Train Time Complexity</InputLabel>
                        <Select
                            onChange={e => set_train(e.target.value)}>
                            {complexities.map((TrainTimeComplexity) => (
                                <MenuItem key={TrainTimeComplexity} value={TrainTimeComplexity}>
                                    {TrainTimeComplexity}
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Maths Notation (latex)'}
                        InputLabelProps={{shrink: true}}
                        helperText={"Add the more specific time complexity representation using latex."}
                        variant={"outlined"}
                        onChange={e => setTrainTimeComplexityMathsNotation(e.target.value)}
                    />
                </Grid>
                {/*<Grid item xs={12} style={{minHeight: 80, minWidth: 500}}>*/}
                {/*    <FormControl fullWidth size="small" variant="outlined">*/}
                {/*        <InputLabel shrink>Test\Run Time Complexity</InputLabel>*/}
                {/*        <Select onChange={e => set_test(e.target.value)}>*/}
                {/*            {complexities.map((TestTimeComplexity) => (*/}
                {/*                <MenuItem key={TestTimeComplexity} value={TestTimeComplexity}>*/}
                {/*                    {TestTimeComplexity}*/}
                {/*                </MenuItem>*/}
                {/*            ))}*/}
                {/*        </Select>*/}
                {/*    </FormControl>*/}
                {/*</Grid>*/}
                {/*<Grid item xs={12} style={{minHeight: 80, minWidth: 500}}>*/}
                {/*    <FormControl fullWidth size="small" variant="outlined">*/}
                {/*        <InputLabel shrink>Space Complexity</InputLabel>*/}
                {/*        <Select onChange={e => set_space(e.target.value)}>*/}
                {/*            {complexities.map((SpaceComplexity) => (*/}
                {/*                <MenuItem key={SpaceComplexity} value={SpaceComplexity}>*/}
                {/*                    {SpaceComplexity}*/}
                {/*                </MenuItem>*/}
                {/*            ))}*/}
                {/*        </Select>*/}
                {/*    </FormControl>*/}
                {/*</Grid>*/}
            </Grid>
        </Card>
    );
}