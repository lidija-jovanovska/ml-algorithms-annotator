import React, {useState} from "react";
import {Card, FormControl, Grid, InputLabel, MenuItem, Paper, Select, Switch, Typography} from "@material-ui/core";
import Container from './DropdownContainer';
import tasks from "../../static/annotation-schema/tasks.json";
import datasets from "../../static/annotation-schema/datasets.json";
import optimization_problems from "../../static/annotation-schema/optimization_problems.json";
import generalization_specifications from "../../static/annotation-schema/generalization_specification.json";

export default function InputOutput({setDatasets,
                                    setTasks,
                                    setBatchMode,
                                    setGeneralizationLanguage,
                                    setGeneralizationSpecifications
                                    }) {

    const onChange = (currentNode, selectedNodes) => {
        if (currentNode.label.includes("dataset")) {
            setDatasets(selectedNodes);
        } else if (currentNode.label.includes("task")) {
            setTasks(selectedNodes);
        } else if (currentNode.label.includes("model") || currentNode.label.includes("specification")) {
            setGeneralizationSpecifications(selectedNodes);
        }
    };

    const [Batch, setBatch] = useState(true);

    const setBatchmode = (Batch) => {
        setBatch(Batch);
        setBatchMode(Batch);
    };

    return (
        <Card>
            <Grid container spacing={3} align={"left"} justify={"center"} style={{padding: 50}}>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Input/Output
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <Container
                        data={datasets}
                        onChange={onChange}
                        texts={{placeholder: 'Dataset'}}
                        className="mdl-demo"
                    />
                </Grid>
                <Grid item xs={8}>
                    <Container
                        data={tasks}
                        onChange={onChange}
                        texts={{placeholder: 'Task'}}
                        className="mdl-demo"
                    />
                </Grid>
                <Grid item xs={4}>
                    <Typography component="div">
                        <Grid component="label" container alignItems="center" spacing={1}>
                            <Grid item>Batch</Grid>
                            <Grid item>
                                <Switch
                                    checked={!Batch}
                                    onChange={(e) => setBatchmode(!Batch)}
                                    name="BatchMode"/>
                            </Grid>
                            <Grid item>Online</Grid>
                        </Grid>
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <FormControl fullWidth size="small" variant="outlined">
                        <InputLabel shrink>Generalization Language Specification</InputLabel>
                        <Select onChange={e => setGeneralizationLanguage(e.target.value)}>
                            <MenuItem value={0}>None</MenuItem>
                            <MenuItem value={1}>Language of Bayesian Nets</MenuItem>
                            <MenuItem value={2}>Language of Decision Rules</MenuItem>
                            <MenuItem value={3}>Language of Decision Trees</MenuItem>
                            <MenuItem value={4}>Language of Graphical Models</MenuItem>
                            <MenuItem value={5}>Language of Markov Chains</MenuItem>
                            <MenuItem value={6}>Language of Neural Nets</MenuItem>
                            <MenuItem value={7}>Other</MenuItem>
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item xs={12}>
                    <Container
                        data={generalization_specifications}
                        onChange={onChange}
                        texts={{placeholder: 'Generalization Specification'}}
                        className="mdl-demo"
                    />
                </Grid>
            </Grid>
        </Card>
    );
}