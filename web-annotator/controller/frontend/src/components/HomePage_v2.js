import React, {Component, useState, useEffect, useStateWithCallback} from "react";
import {
    Button,
    Checkbox,
    FormControl,
    Grid, Input,
    InputLabel, ListItemText, makeStyles, MenuItem,
    Paper,
    Select,
    Switch,
    TextField,
    Typography, useTheme,
    withStyles,
} from "@material-ui/core";
import 'react-dropdown-tree-select/dist/styles.css';
import DropdownTreeSelect from "react-dropdown-tree-select";
import tasks from "../../static/annotation-schema/tasks.json";
import datasets from "../../static/annotation-schema/datasets.json";
import optimization_problems from "../../static/annotation-schema/optimization_problems.json";

const datatypes = ['integer', 'boolean', 'real', 'dictionary', 'discrete']

const complexities = [
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
]

const assumptions = [
    "No Assumptions",
    "Linear Relationship",
    "Multivariate Normality",
    "Feature Independence (No Multicolinearity)",
    "No Autocorrelation",
    "Homoscedasticity",
    "Normal distribution of Error Terms",
    "Spherical Cluster Shape",
    "Similar-Sized Clusters",
    "Linear relationship between the logit of the outcome and each predictor variable",
    "Conditional Independence",
    "Conditional Feature Independence",
    "Stationarity",
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

const assignObjectPaths = (obj, stack) => {
    Object.keys(obj).forEach(k => {
        const node = obj[k];
        if (typeof node === "object") {
            node.path = stack ? `${stack}.${k}` : k;
            assignObjectPaths(node, node.path);
        }
    });
};

export default function HomePage_v2() {


    const theme = useTheme();
    const [AlgorithmName, setAlgorithmName] = useState('');
    const [DocumentName, setDocumentName] = useState('');
    const [DocumentId, setDocumentId] = useState('');
    const [DatasetsList, setDataset] = useState(0);
    const [TasksList, setTask] = useState(0);
    const [BatchMode, setBatchMode] = useState(false);
    const [GeneralizationLanguage, setGeneralizationLanguage] = useState('');
    const [EnsembleMode, setEnsembleMode] = useState(false);
    const [Assumption, setAssumption] = useState([]);
    var [newAssumption, setNewAssumption] = useState('');
    const [OpProblem, setOpProblem] = useState(0);
    const [TrainTimeComplexity, setTrainTimeComplexity] = useState(0);
    const [TestTimeComplexity, setTestTimeComplexity] = useState(0);
    const [SpaceComplexity, setSpaceComplexity] = useState(0);
    var [AlgorithmParameter, setAlgorithmParameter] = useState('');
    var [AlgorithmHyperparameter, setAlgorithmHyperparameter] = useState('');
    var [ModelParameter, setModelParameter] = useState('');
    const [AlgorithmParameterDatatype, setAlgorithmParameterDatatype] = useState('');
    const [AlgorithmHyperparameterDatatype, setAlgorithmHyperparameterDatatype] = useState('');
    const [ModelParameterDatatype, setModelParameterDatatype] = useState('');
    var [AlgorithmParameters, setAlgorithmParameters] = useState([]);
    var [AlgorithmHyperparameters, setAlgorithmHyperparameters] = useState([]);
    var [ModelParameters, setModelParameters] = useState([]);


    useEffect(() => {
    });

    const onDatasetChange = (currentNode, selectedNodes) => {
        // edit to include only labels and not whole dicts
        setDataset(selectedNodes);
        console.log('onChange::', currentNode, selectedNodes);
    };

    const onTaskChange = (currentNode, selectedNodes) => {
        // edit to include only labels and not whole dicts
        setTask(selectedNodes);
        console.log('onChange::', currentNode, selectedNodes);
    };

    const onOpProblemChange = (currentNode, selectedNodes) => {
        // edit to include only labels and not whole dicts
        setTask(selectedNodes);
        console.log('onChange::', currentNode, selectedNodes);
    };

    const AddNewAssumption = () => {
        const newAssumptions = Assumption.concat(newAssumption);
        if (newAssumption.length > 0) {
            setAssumption(newAssumptions);
        }
    };

    const AddNewAlgorithmParameter = () => {
        var index = Object.keys(AlgorithmParameters).length;
        const param = {id: index, name: AlgorithmParameter, datatype: AlgorithmParameterDatatype};
        const newAlgorithmParameters = AlgorithmParameters.concat(param);
        if (AlgorithmParameter.length > 0) {
            setAlgorithmParameters(newAlgorithmParameters);
        }
    }

    const AddNewAlgorithmHyperparameter = () => {
        var index = Object.keys(AlgorithmHyperparameters).length;
        const hyperparam = {id: index, name: AlgorithmHyperparameter, datatype: AlgorithmParameterDatatype};
        const newAlgorithmHyperparameters = AlgorithmHyperparameters.concat(hyperparam);
        if (AlgorithmHyperparameter.length > 0) {
            setAlgorithmHyperparameters(newAlgorithmHyperparameters);
        }
    }

    const AddNewModelParameter = () => {
        var index = Object.keys(ModelParameters).length;
        const modelParam = {id: index, name: ModelParameter, datatype: ModelParameterDatatype};
        const newModelParameters = ModelParameters.concat(modelParam);
        if (ModelParameter.length > 0) {
            setModelParameters(newModelParameters);
        }
    }

    const GenerateAnnotation = () => {
        console.log("Algorithm name: ", AlgorithmName);
        console.log("Document name: ", DocumentName);
        console.log("Document ID: ", DocumentId);
        console.log("Datasets: ", DatasetsList);
        console.log("Tasks: ", TasksList);
        console.log("BatchMode: ", BatchMode);
        console.log("GeneralizationLanguage: ", GeneralizationLanguage);
        console.log("EnsembleMode: ", EnsembleMode);
        console.log("Assumptions: ", Assumption);
        console.log("Optimization Problems: ", OpProblem);
        console.log("TrainTimeComplexity: ", TrainTimeComplexity);
        console.log("TestTimeComplexity: ", TestTimeComplexity);
        console.log("SpaceComplexity: ", SpaceComplexity);
        console.log("Algorithm Parameters", AlgorithmParameters);
        console.log("Model Parameters: ", ModelParameters);
        console.log("Algorithm Hyperparameters: ", AlgorithmHyperparameters);
    }

    return (
        <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 25}}>
            <Paper>
                <Grid item xs={12}>
                    <Typography component={"h4"} variant={"h4"}>
                        Semantic Annotation of DM/ML Algorithms
                    </Typography>
                </Grid>
                <Grid container spacing={3}>
                    <Grid item xs={12}>
                        <TextField
                            required={true}
                            fullWidth={true}
                            label={'Algorithm Name'}
                            InputLabelProps={{shrink: true}}
                            helperText={"Name of the described algorithm."}
                            variant={"outlined"}
                            onChange={e => setAlgorithmName(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField
                            required={true}
                            fullWidth={true}
                            label={'Document name'}
                            InputLabelProps={{shrink: true}}
                            helperText={"Name of the Document where the Algorithm is described."}
                            variant={"outlined"}
                            onChange={e => setDocumentName(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField
                            required={true}
                            fullWidth={true}
                            label={'Document ID'}
                            InputLabelProps={{shrink: true}}
                            helperText={"DOI/ISBN of the Document where the Algorithm is described."}
                            variant={"outlined"}
                            onChange={e => setDocumentId(e.target.value)}
                        />
                    </Grid>
                </Grid>
                <Grid container spacing={3} justify={"space-evenly"}>
                    <Grid item xs={4}>
                        <DropdownTreeSelect
                            data={datasets}
                            onChange={onDatasetChange}
                            texts={{placeholder: 'Dataset'}}
                        />
                    </Grid>
                    <Grid item xs={4}>
                        <DropdownTreeSelect
                            data={tasks}
                            onChange={onTaskChange}
                            texts={{placeholder: 'Task'}}
                        />
                    </Grid>
                    <Grid item xs={4}>
                        <Typography component="div">
                            <Grid component="label" container alignItems="center" spacing={1}>
                                <Grid item>Batch</Grid>
                                <Grid item>
                                    <AntSwitch checked={!BatchMode}
                                               onChange={(e) => setBatchMode(!BatchMode)}
                                               name="BatchMode"/>
                                </Grid>
                                <Grid item>Online</Grid>
                            </Grid>
                        </Typography>
                    </Grid>
                </Grid>
                <Grid container justify={"space-evenly"} style={{padding: 10}}>
                    <Grid item xs={4}>
                        <DropdownTreeSelect
                            data={optimization_problems}
                            onChange={onOpProblemChange}
                            texts={{placeholder: 'Optimization Problem'}}
                        />
                    </Grid>
                    <Grid item xs={4}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Generalization Language Specification</InputLabel>
                            <Select onChange={e => setGeneralizationLanguage(e.target.value)}>
                                <MenuItem value={"BayesianNets"}>Language of Bayesian Nets</MenuItem>
                                <MenuItem value={"DecisionRules"}>Language of Decision Rules</MenuItem>
                                <MenuItem value={"DecisionTrees"}>Language of Decision Trees</MenuItem>
                                <MenuItem value={"GraphicalModels"}>Language of Graphical Models</MenuItem>
                                <MenuItem value={"MarkovChains"}>Language of Markov Chains</MenuItem>
                                <MenuItem value={"NeuralNets"}>Language of Neural Nets</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={4}>
                        <Typography component="div">
                            <Grid component="label" container alignItems="stretch" spacing={1}>
                                <Grid item>Ensemble</Grid>
                                <Grid item>
                                    <AntSwitch checked={!EnsembleMode}
                                               onChange={(e) => setEnsembleMode(!EnsembleMode)}
                                               name="EnsembleMode"/>
                                </Grid>
                                <Grid item>Single Generalization</Grid>
                            </Grid>
                        </Typography>
                    </Grid>
                </Grid>
                <Grid container justify={"space-evenly"}>
                    <Grid item xs={4}>
                        <FormControl style={{width: 240}}>
                            <InputLabel>Algorithm Assumptions</InputLabel>
                            <Select
                                multiple
                                value={Assumption}
                                onChange={e => setAssumption(e.target.value)}
                                input={<Input/>}
                                renderValue={(selected) => selected.join(', ')}
                            >
                                {assumptions.map((name) => (
                                    <MenuItem key={name} value={name}>
                                        <Checkbox checked={Assumption.indexOf(name) > -1}/>
                                        <ListItemText primary={name}/>
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={4}>
                        <TextField
                            required={true}
                            fullWidth={true}
                            label={'Custom Algorithm Assumption'}
                            InputLabelProps={{shrink: true}}
                            helperText={"Add a New Algorithm Assumption that is not listed."}
                            variant={"outlined"}
                            onChange={e => setNewAssumption(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={4}>
                        <Button variant={"contained"} color={"primary"} onClick={AddNewAssumption}
                                style={{minWidth: 60}}>Add New
                            Assumption</Button>
                    </Grid>
                </Grid>
                <Grid container justify={"space-evenly"} spacing={3} style={{padding: 25}}>
                    <Grid item xs={4}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Train Time Complexity</InputLabel>
                            <Select onChange={e => setTrainTimeComplexity(e.target.value)}>
                                {complexities.map((TrainTimeComplexity) => (
                                    <MenuItem key={TrainTimeComplexity} value={TrainTimeComplexity}>
                                        {TrainTimeComplexity}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={4}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Test\Run Time Complexity</InputLabel>
                            <Select onChange={e => setTestTimeComplexity(e.target.value)}>
                                {complexities.map((TestTimeComplexity) => (
                                    <MenuItem key={TestTimeComplexity} value={TestTimeComplexity}>
                                        {TestTimeComplexity}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={4}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Space Complexity</InputLabel>
                            <Select onChange={e => setSpaceComplexity(e.target.value)}>
                                {complexities.map((SpaceComplexity) => (
                                    <MenuItem key={SpaceComplexity} value={SpaceComplexity}>
                                        {SpaceComplexity}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>
                </Grid>
                <Grid container justify={"space-evenly"} spacing={3}>
                    <Grid item xs={4}>
                        <TextField
                            required={true}
                            fullWidth={true}
                            label={'Algorithm Parameter Name'}
                            InputLabelProps={{shrink: true}}
                            variant={"outlined"}
                            value={AlgorithmParameter}
                            onChange={e => setAlgorithmParameter(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={4}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Algorithm Parameter Datatype</InputLabel>
                            <Select onChange={e => setAlgorithmParameterDatatype(e.target.value)}>
                                {datatypes.map((AlgorithmParameterDatatype) => (
                                    <MenuItem key={AlgorithmParameterDatatype} value={AlgorithmParameterDatatype}>
                                        {AlgorithmParameterDatatype}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={4}>
                        <Button type="reset" variant={"contained"} color={"primary"}
                                onClick={AddNewAlgorithmParameter} style={{width: 220, height: 50}}>
                            Add New Algorithm Parameter
                        </Button>
                    </Grid>
                </Grid>
                <Grid container justify={"space-evenly"} spacing={3}>
                    <Grid item xs={4}>
                        <TextField
                            required={true}
                            fullWidth={true}
                            label={'Algorithm Hyperparameter Name'}
                            InputLabelProps={{shrink: true}}
                            variant={"outlined"}
                            value={AlgorithmHyperparameter}
                            onChange={e => setAlgorithmHyperparameter(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={4}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Algorithm Hyperparameter Datatype</InputLabel>
                            <Select onChange={e => setAlgorithmHyperparameterDatatype(e.target.value)}>
                                {datatypes.map((AlgorithmHyperparameterDatatype) => (
                                    <MenuItem key={AlgorithmHyperparameterDatatype}
                                              value={AlgorithmHyperparameterDatatype}>
                                        {AlgorithmHyperparameterDatatype}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={4}>
                        <Button type="reset" variant={"contained"} color={"primary"}
                                onClick={AddNewAlgorithmHyperparameter} style={{width: 220, height: 50}}>
                            Add New Algorithm Hyperparameter
                        </Button>
                    </Grid>
                </Grid>
                <Grid container justify={"space-evenly"} spacing={3}>
                    <Grid item xs={4}>
                        <TextField
                            required={true}
                            fullWidth={true}
                            label={'Model Parameter Name'}
                            InputLabelProps={{shrink: true}}
                            variant={"outlined"}
                            value={ModelParameter}
                            onChange={e => setModelParameter(e.target.value)}
                        />
                    </Grid>
                    <Grid item xs={4}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Model Parameter Datatype</InputLabel>
                            <Select onChange={e => setModelParameterDatatype(e.target.value)}>
                                {datatypes.map((ModelParameterDatatype) => (
                                    <MenuItem key={ModelParameterDatatype} value={ModelParameterDatatype}>
                                        {ModelParameterDatatype}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={4}>
                        <Button type="reset" variant={"contained"} color={"primary"}
                                onClick={AddNewModelParameter}
                                style={{width: 220, height: 50, justifyContent: "center"}}>
                            Add New Model Parameter
                        </Button>
                    </Grid>
                </Grid>
                <Grid container justify={"space-evenly"} spacing={3}>
                    <Grid item xs={6}>
                        <Button type="reset" variant={"contained"} color={"secondary"}
                                onClick={GenerateAnnotation}
                                style={{width: 400, height: 60, justifyContent: "center"}}>
                            Generate Annotation
                        </Button>
                    </Grid>
                </Grid>
            </Paper>
        </Grid>
    );
}