import * as React from 'react';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepButton from '@material-ui/core/StepButton';
import Button from '@material-ui/core/Button';
import {
    FormControl,
    Grid,
    Card,
    InputLabel,
    makeStyles,
    MenuItem,
    Paper,
    Select,
    Typography,
    Input, Checkbox, ListItemText
} from "@material-ui/core";
import Metadata from "./Metadata";
import Algorithms from "./Algorithms";
import InputOutput from "./InputOutput";
import Assumptions from "./Assumptions";
import Complexity from "./Complexity";
import Parameters from "./Parameters";
import AnnotatorInfo from "./AnnotatorInfo";
import {useEffect, useState} from "react";
const axios = require('axios').default;

const steps = ['Metadata', 'Algorithms', 'Input/Output', 'Assumptions', 'Complexity', 'Parameters', 'Submit', 'Invisible'];

const useStyles = makeStyles({
    stepper: {
        position: "fixed",
        height: "100%",
        width: "15%",
        backgroundColor: "#e7f6ec",
        borderRight: "3px solid #bd5845",
    },
    main: {
        position: "absolute",
        height: "100%",
        width: "60%",
        marginLeft: "30%",
    },
    textfield: {
        required: true,
        variant: "outlined",
    },
    button: {
        width: 200,
        height: 50,
        justifyContent: "center"
    },
});

export default function HorizontalNonLinearStepper() {
    const style = useStyles();
    // page references -> convert to dict
    const metadataRef = React.useRef(null);
    const algorithmsRef = React.useRef(null);
    const inputOutputRef = React.useRef(null);
    const assumptionsRef = React.useRef(null);
    const complexityRef = React.useRef(null);
    const parametersRef = React.useRef(null);
    const annotatorRef = React.useRef(null);
    const submitRef = React.useRef(null);
    const [activeStep, setActiveStep] = React.useState(0);
    const [completed, setCompleted] = React.useState({});

    useEffect(() => {
        getSingleGeneralizationAlgorithms();
        getDataMiningAlgorithms();
    }, []);

    const handleStep = (step) => () => {
        setActiveStep(step);
        if (step === 0) {
            metadataRef.current.scrollIntoView({behavior: "smooth"});
        } else if (step === 1) {
            algorithmsRef.current.scrollIntoView({behavior: "smooth"});
        } else if (step === 2) {
            inputOutputRef.current.scrollIntoView({behavior: "smooth"});
        } else if (step === 3) {
            assumptionsRef.current.scrollIntoView({behavior: "smooth"});
        } else if (step === 4) {
            complexityRef.current.scrollIntoView({behavior: "smooth"});
        } else if (step === 5) {
            parametersRef.current.scrollIntoView({behavior: "smooth"});
        } else if (step === 6) {
            annotatorRef.current.scrollIntoView({behavior: "smooth"});
        } else if (step === 7) {
            submitRef.current.scrollIntoView({behavior: "smooth"});
        }
    };

    function postAnnotation() {

        axios.post('api/annotations/', {
            algorithm_name: AlgorithmName,
            algorithm_type: DMAlgorithmType,
            documents: Documents,
            sampling: Sampling,
            base_estimator: BaseEstimator,
            selected_data_mining_algorithms: SelectedDataMiningAlgorithms,
            data_mining_algorithm_final_estimator: DataMiningAlgorithmFinalEstimator,
            selected_simple_algorithms: selectedSimpleAlgorithms,
            new_simple_algorithms: newSimpleAlgorithms,
            datasets: Datasets,
            tasks: Tasks,
            batch_mode: BatchMode,
            generalization_language: GeneralizationLanguage,
            generalization_specifications: GeneralizationSpecifications,
            assumptions: assumptions,
            new_assumptions: newAssumptions,
            op_problems: OpProblems,
            op_problem_text: OpProblemText,
            op_problem_maths: OpProblemMaths,
            train_time_complexity: TrainTimeComplexity,
            train_time_complexity_maths: TrainTimeComplexityMathsNotation,
            // test_time_complexity: TestTimeComplexity,
            // space_complexity: SpaceComplexity,
            algorithm_parameters: AlgorithmParameters,
            // algorithm_hyperparameters: AlgorithmHyperparameters,
            // model_parameters: ModelParameters,
            annotator_name: annotatorName,
            annotator_affiliation: annotatorAffiliation,
            annotator_email: annotatorEmail
        })
            .then(function (response) {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            });
    }


    function getSingleGeneralizationAlgorithms() {

        axios.get('api/single_generalization_algorithms/', {
        }).then(response => {
            setSingleGeneralizationAlgorithms(response.data);
            console.log(SingleGeneralizationAlgorithms);
        });
    }

    function getDataMiningAlgorithms() {

        axios.get('api/data_mining_algorithms/', {
        }).then(response => {
            setDataMiningAlgorithms(response.data);
            console.log(DataMiningAlgorithms);
        });
    }


    // Metadata
    const [AlgorithmName, setAlgorithmName] = useState('');
    const [DMAlgorithmType, setDMAlgorithmType] = useState('');
    const [Documents, setDocuments] = useState([]);

    // Ensembles
    const [Sampling, setSampling] = useState('');
    const [BaseEstimator, setBaseEstimator] = useState('');
    const [SingleGeneralizationAlgorithms, setSingleGeneralizationAlgorithms] = useState([]);
    const [DataMiningAlgorithms, setDataMiningAlgorithms] = useState([]);
    const [SelectedDataMiningAlgorithms, setSelectedDataMiningAlgorithms] = useState([]);
    const [DataMiningAlgorithmFinalEstimator, setDataMiningAlgorithmFinalEstimator] = useState([]);

    // Algorithms
    const [selectedSimpleAlgorithms, setSelectedSimpleAlgorithms] = useState([]);
    const [newSimpleAlgorithms, setNewSimpleAlgorithms] = useState('');

    // Input/Output
    const [Datasets, setDatasets] = useState([]);
    const [Tasks, setTasks] = useState([]);
    const [BatchMode, setBatchMode] = useState(false);
    const [GeneralizationLanguage, setGeneralizationLanguage] = useState('');
    const [GeneralizationSpecifications, setGeneralizationSpecifications] = useState([]);

    // Assumptions
    const [assumptions, setAssumptions] = useState([]);
    const [newAssumptions, setNewAssumptions] = useState([]);

    // Complexity
    const [OpProblems, setOpProblems] = useState([]);
    const [OpProblemText, setOpProblemText] = useState('');
    const [OpProblemMaths, setOpProblemMaths] = useState('');
    const [TrainTimeComplexity, setTrainTimeComplexity] = useState('');
    const [TrainTimeComplexityMathsNotation, setTrainTimeComplexityMathsNotation] = useState('');
    const [TestTimeComplexity, setTestTimeComplexity] = useState('');
    const [SpaceComplexity, setSpaceComplexity] = useState('');

    // Parameters
    const [AlgorithmParameters, setAlgorithmParameters] = useState([]);
    // const [AlgorithmHyperparameters, setAlgorithmHyperparameters] = useState([]);
    // const [ModelParameters, setModelParameters] = useState([]);

    // AnnotatorInfo
    const [annotatorName, setAnnotatorName] = useState('');
    const [annotatorAffiliation, setAnnotatorAffiliation] = useState('');
    const [annotatorEmail, setAnnotatorEmail] = useState('');

    function SingleGeneralizationAlgorithmsSelection(props) {
        return(
            <FormControl style={{minWidth: 500, minHeight: 100}}>
                <InputLabel>Base Estimator</InputLabel>
                <Select
                    fullWidth
                    value={BaseEstimator}
                    onChange={e => setBaseEstimator(e.target.value)}
                    input={<Input/>}
                >
                    {SingleGeneralizationAlgorithms.map((name) => (
                        <MenuItem key={name} value={name}>
                            <ListItemText primary={name}/>
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
        );
    }

    function DataMiningAlgorithmsSelection(props){
        return(
            <FormControl style={{minWidth: 500, minHeight: 100}}>
                <InputLabel>Estimators</InputLabel>
                    <Select
                        fullWidth
                        multiple
                        value={SelectedDataMiningAlgorithms}
                        onChange={e => setSelectedDataMiningAlgorithms(e.target.value)}
                        input={<Input/>}
                        renderValue={(selected) => selected.join(', ')}
                    >
                        {DataMiningAlgorithms.map((name) => (
                            <MenuItem key={name} value={name}>
                                <Checkbox checked={SelectedDataMiningAlgorithms.indexOf(name) > -1}/>
                                <ListItemText primary={name}/>
                            </MenuItem>
                        ))}
                    </Select>
            </FormControl>
        );
    }

    function SingleDataMiningAlgorithmSelection(props){
        return(
            <FormControl fullWidth size="small" variant="outlined">
                <InputLabel shrink >Final Estimator</InputLabel>
                <Select
                    value={DataMiningAlgorithmFinalEstimator}
                    onChange={e => setDataMiningAlgorithmFinalEstimator(e.target.value)}>
                    {DataMiningAlgorithms.map((DataMiningAlgorithmFinalEstimator) => (
                        <MenuItem key={DataMiningAlgorithmFinalEstimator} value={DataMiningAlgorithmFinalEstimator}>
                            {DataMiningAlgorithmFinalEstimator}
                        </MenuItem>
                    ))}
                </Select>
            </FormControl>
        );
    }

    function Bagging(props) {
        return(
            <Card elevation={4}>
                <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 50}}>
                    <Grid item xs={12}>
                        <Typography variant={"h5"} align={"left"}>
                            Bagging
                        </Typography>
                    </Grid>
                    <Grid item xs={12}>
                        <FormControl fullWidth size="small" variant="outlined">
                            <InputLabel shrink>Sampling</InputLabel>
                            <Select value={Sampling} onChange={e => setSampling(e.target.value)}>
                                <MenuItem value={0}>sampling random subsets of the samples</MenuItem>
                                <MenuItem value={1}>sampling random subsets of the samples (with replacement)</MenuItem>
                                <MenuItem value={2}>sampling random subsets of the features</MenuItem>
                                <MenuItem value={3}>sampling random subsets of both samples and features</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12}>
                        <SingleGeneralizationAlgorithmsSelection/>
                    </Grid>
                </Grid>
            </Card>
        );
    }

    function Boosting(props) {
        return(
            <Card elevation={4}>
                <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 50}}>
                    <Grid item xs={12}>
                        <Typography variant={"h5"} align={"left"}>
                            Boosting
                        </Typography>
                    </Grid>
                    <Grid item xs={12}>
                        <SingleGeneralizationAlgorithmsSelection/>
                    </Grid>
                </Grid>
            </Card>
        );
    }

    function Voting(props) {
        return(
          <Card elevation={4}>
              <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 50}}>
                  <Grid item xs={12}>
                      <Typography variant={"h5"} align={"left"}>
                        Voting
                      </Typography>
                  </Grid>
                  <Grid item xs={12}>
                    <DataMiningAlgorithmsSelection/>
                </Grid>
              </Grid>
          </Card>
        );
    }

    function Stacking(props) {
        return(
            <Card elevation={4}>
              <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 50}}>
                  <Grid item xs={12}>
                      <Typography variant={"h5"} align={"left"}>
                        Stacking
                      </Typography>
                  </Grid>
                  <Grid item xs={12}>
                    <DataMiningAlgorithmsSelection/>
                    <SingleDataMiningAlgorithmSelection/>
                </Grid>
              </Grid>
          </Card>
        );
    }

    function Ensemble(props) {
        if (DMAlgorithmType === 'bagging') {
            return <Bagging/>
        } else if (DMAlgorithmType === 'boosting') {
            return <Boosting/>
        } else if (DMAlgorithmType === 'voting') {
            return <Voting/>
        } else if (DMAlgorithmType === 'stacking') {
            return <Stacking/>
        } else {
            return <div/>
        }
    }

    return (
        <div>
            <Stepper nonLinear activeStep={activeStep} orientation={"vertical"} className={style.stepper}>
                {steps.map((label, index) => (
                    <Step key={label} completed={completed[index]}>
                        <StepButton color="inherit" onClick={handleStep(index)}>
                            {label}
                        </StepButton>
                    </Step>
                ))}
            </Stepper>
            <Grid container spacing={10} className={style.main}>
                <Grid item ref={metadataRef}>
                    <Metadata
                        setAlgorithmName={setAlgorithmName}
                        setDocuments={setDocuments}
                        setDMAlgorithmType={setDMAlgorithmType}
                    />
                </Grid>
                <Grid item>
                    <Ensemble/>
                </Grid>
                <Grid item ref={algorithmsRef}>
                    <Algorithms
                        setSelectedSimpleAlgorithms={setSelectedSimpleAlgorithms}
                        setNewSimpleAlgorithms={setNewSimpleAlgorithms}
                    />
                </Grid>
                <Grid item ref={inputOutputRef}>
                    <InputOutput
                        setDatasets={setDatasets}
                        setTasks={setTasks}
                        setBatchMode={setBatchMode}
                        setGeneralizationLanguage={setGeneralizationLanguage}
                        setGeneralizationSpecifications={setGeneralizationSpecifications}
                    />
                </Grid>
                <Grid item ref={assumptionsRef}>
                    <Assumptions
                        setAssumptions={setAssumptions}
                        setNewAssumptions={setNewAssumptions}
                    />
                </Grid>
                <Grid item ref={complexityRef}>
                    <Complexity
                        setOpProblems={setOpProblems}
                        setOpProblemText={setOpProblemText}
                        setOpProblemMaths={setOpProblemMaths}
                        setTrainTimeComplexity={setTrainTimeComplexity}
                        setTrainTimeComplexityMathsNotation={setTrainTimeComplexityMathsNotation}
                        // setTestTimeComplexity={setTestTimeComplexity}
                        // setSpaceComplexity={setSpaceComplexity}
                    />
                </Grid>
                <Grid item ref={parametersRef}>
                    <Parameters
                        setAlgorithmParameters={setAlgorithmParameters}
                        // setAlgorithmHyperparameters={setAlgorithmHyperparameters}
                        // setModelParameters={setModelParameters}
                    />
                </Grid>
                <Grid item ref={annotatorRef}>
                    <AnnotatorInfo
                        setAnnotatorName={setAnnotatorName}
                        setAnnotatorAffiliation={setAnnotatorAffiliation}
                        setAnnotatorEmail={setAnnotatorEmail}
                    />
                </Grid>
                <Grid item xs={4} textAlign={'center'} ref={submitRef} style={{paddingBottom: 50, paddingLeft: 250}}>
                    <Button
                        disabled={AlgorithmName === ''}
                        variant="contained"
                        color="primary"
                        onClick={postAnnotation}
                        className={style.button}>
                        Submit
                    </Button>
                </Grid>
            </Grid>
        </div>
    );
};