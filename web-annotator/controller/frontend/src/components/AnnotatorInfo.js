import React from "react";
import {Card, Grid, Paper, TextField, Typography} from "@material-ui/core";

export default function AnnotatorInfo({setAnnotatorName, setAnnotatorAffiliation, setAnnotatorEmail}) {
    return (
        <Card>
            <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 20}}>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Sign & Submit
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Annotator Name'}
                        InputLabelProps={{shrink: true}}
                        variant={"outlined"}
                        onChange={e => setAnnotatorName(e.target.value)}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Annotator Affiliation'}
                        InputLabelProps={{shrink: true}}
                        variant={"outlined"}
                        onChange={e => setAnnotatorAffiliation(e.target.value)}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Annotator Email'}
                        InputLabelProps={{shrink: true}}
                        variant={"outlined"}
                        onChange={e => setAnnotatorEmail(e.target.value)}
                    />
                </Grid>
            </Grid>
        </Card>
    );
}