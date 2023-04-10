/*jshint esversion: 6 */

import React, {useEffect, useState} from "react";
import {Tabs, Tab, AppBar, Button} from "@material-ui/core";
// import About from "./About";
import Metadata from "./Metadata";
import InputOutput from "./InputOutput";
import Assumptions from "./Assumptions";
import Complexity from "./Complexity";
import Parameters from "./Parameters";
import AnnotatorInfo from "./AnnotatorInfo";
const axios = require('axios').default;

// tabs menu




export default function HomePage_v3() {

    // Metadata
    const [AlgorithmName, setAlgorithmName] = useState('');
    const [Documents, setDocuments] = useState([]);

    // Input/Output
    const [Datasets, setDatasets] = useState([]);
    const [Tasks, setTasks] = useState([]);
    const [BatchMode, setBatchMode] = useState(false);
    const [OpProblems, setOpProblems] = useState([]);
    const [GeneralizationLanguage, setGeneralizationLanguage] = useState('');
    const [GeneralizationSpecifications, setGeneralizationSpecifications] = useState([]);

    // Assumptions
    const [assumptions, setAssumptions] = useState([]);
    const [newAssumptions, setNewAssumptions] = useState([]);

    // Complexity
    const [TrainTimeComplexity, setTrainTimeComplexity] = useState('');
    const [TestTimeComplexity, setTestTimeComplexity] = useState('');
    const [SpaceComplexity, setSpaceComplexity] = useState('');

    // Parameters
    const [AlgorithmParameters, setAlgorithmParameters] = useState([]);
    const [AlgorithmHyperparameters, setAlgorithmHyperparameters] = useState([]);
    const [ModelParameters, setModelParameters] = useState([]);

    // AnnotatorInfo
    const [annotatorName, setAnnotatorName] = useState('');
    const [annotatorSurname, setAnnotatorSurname] = useState('');
    const [annotatorAffiliation, setAnnotatorAffiliation] = useState('');
    const [annotatorEmail, setAnnotatorEmail] = useState('');

    // Misc
    const [selectedTab, setSelectedTab] = React.useState(0);

    const handleChangeTab = (event, newValue) => {
        setSelectedTab(newValue);
    };

    const setMetadata = (props) => {
        console.log("Updating Metadata...");
        console.log("Alg. name: ", props.algName);
        console.log("Documents: ", props.documents);
        setAlgorithmName(props.algName);
        setDocuments(props.documents);
    };

    const setInputOutput = (props) => {
        console.log("Updating IO");
        console.log("Datasets: ", props.datasets);
        console.log("Tasks: ", props.tasks);
        console.log("Batch Mode: ", props.batchMode);
        console.log("Op. Problems: ", props.opProblems);
        console.log("Generalization Language: ", props.generalizationLanguage);
        console.log("Generalization Specifications: ", props.generalizationSpecifications);

        setDatasets(props.datasets);
        setTasks(props.tasks);
        setBatchMode(props.batchMode);
        setOpProblems(props.opProblems);
        setGeneralizationLanguage(props.generalizationLanguage);
        setGeneralizationSpecifications(props.generalizationSpecifications);
    };

    const setAssumptionData = (props) => {
        console.log("Updating Assumptions");
        console.log("Assumptions: ", props.assumptions);
        console.log("New Assumptions: ", props.newAssumptions);
        setAssumptions(props.assumptions);
        setNewAssumptions(props.newAssumptions);
    };

    const setComplexity = (props) => {
        console.log("Updating Complexity");
        console.log("Train: ", props.trainComplexity);
        console.log("Test: ", props.testComplexity);
        console.log("Space: ", props.spaceComplexity);
        setTrainTimeComplexity(props.trainComplexity);
        setTestTimeComplexity(props.testComplexity);
        setSpaceComplexity(props.spaceComplexity);
    };

    const setParameters = (props) => {
        console.log("Updating Parameters");
        console.log("Alg. Params: ", props.algorithmParameters);
        console.log("Alg. Hyperparams: ", props.algorithmHyperparameters);
        console.log("Model Params: ", props.modelParameters);
        setAlgorithmParameters(props.algorithmParameters);
        setAlgorithmHyperparameters(props.algorithmHyperparameters);
        setModelParameters(props.modelParameters);
    };


    const setAnnotatorInfo = (props) => {
        console.log("Updating AnnotatorInfo");
        console.log("annotatorName: ", props.annotatorName);
        console.log("annotatorAffiliation: ", props.annotatorAffiliation);
        console.log("annotatorEmail: ", props.annotatorEmail);
        setAnnotatorName(props.annotatorName);
        setAnnotatorAffiliation(props.annotatorAffiliation);
        setAnnotatorEmail(props.annotatorEmail);
    };

    // noinspection JSAnnotator
    function postAnnotation() {
        axios.post('api/annotations/', {
            algorithm_name: AlgorithmName,
            documents: Documents,
            datasets: Datasets,
            tasks: Tasks,
            batch_mode: BatchMode,
            op_problems: OpProblems,
            generalization_language: GeneralizationLanguage,
            generalization_specifications: GeneralizationSpecifications,
            assumptions: assumptions,
            new_assumptions: newAssumptions,
            train_time_complexity: TrainTimeComplexity,
            test_time_complexity: TestTimeComplexity,
            space_complexity: SpaceComplexity,
            algorithm_parameters: AlgorithmParameters,
            algorithm_hyperparameters: AlgorithmHyperparameters,
            model_parameters: ModelParameters,
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

    useEffect(() => {
    });

    return (
        <>
            <AppBar>
                <Tabs value={selectedTab} onChange={handleChangeTab} centered forceRenderTabPanel={true}>
                    <Tab label="Metadata"/>
                    <Tab label="Input/Output"/>
                    <Tab label="Assumptions"/>
                    <Tab label="Complexity"/>
                    <Tab label="Parameters"/>
                    <Tab label="Annotator Information"/>
                    <Tab label="Submit"/>
                </Tabs>
            </AppBar>

            <div style={{marginTop: "5%"}}>
                {selectedTab === 0 && <Metadata setMetadata={setMetadata}/>}
                {selectedTab === 1 && <InputOutput setInputOutput={setInputOutput}/>}
                {selectedTab === 2 && <Assumptions setAssumptionData={setAssumptionData}/>}
                {selectedTab === 3 && <Complexity setComplexity={setComplexity}/>}
                {selectedTab === 4 && <Parameters setParameters={setParameters}/>}
                {selectedTab === 5 && <AnnotatorInfo setAnnotatorInfo={setAnnotatorInfo}/>}
                {selectedTab === 6 && <Button style={{marginTop: 200}} onClick={postAnnotation}>Submit</Button>}
            </div>
        </>
    );
};