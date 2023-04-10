import {Grid, Typography, Tabs, Tab, Paper, TextField} from "@material-ui/core";
import React, {useEffect, useState} from "react";
import {makeStyles} from "@material-ui/core";
import {TabContext, TabPanel} from "@material-ui/lab";
import DropdownTreeSelect from "react-dropdown-tree-select";
import datasets from "../../static/annotation-schema/datasets.json";
import tasks from "../../static/annotation-schema/tasks.json";

const useStyles = makeStyles({
    root: {
        flexGrow: 1,
    },
});


export default function HomePage() {

    function InputOutputTab() {
        return (
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
        );
    }

    function MetadataTab() {
        return (
            <Grid container spacing={3} align={"center"} justify={"center"}>
                <Paper elevation={4}>
                    <Grid item xs={6}>
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

                </Paper>
            </Grid>
        );
    }

    const [AlgorithmName, setAlgorithmName] = useState('');
    const [DocumentName, setDocumentName] = useState('');
    const [DocumentId, setDocumentId] = useState('');

    useEffect(() => {
        console.log("Algorithm name: ", AlgorithmName);
        console.log("Document name: ", DocumentName);
        console.log("Document ID: ", DocumentId);
    });

    return (
        <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 25}}>
            <Paper>
                <Grid item xs={12}>
                    <Typography component={"h4"} variant={"h4"}>
                        Semantic Annotation of DM/ML Algorithms
                    </Typography>
                </Grid>
                <CenteredTabs/>
            </Paper>
        </Grid>
    );
}