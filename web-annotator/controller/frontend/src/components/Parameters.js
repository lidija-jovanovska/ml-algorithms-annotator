import React, {useState} from "react";
import {
    Button,
    Card,
    FormControl,
    Grid,
    InputLabel,
    MenuItem,
    Paper,
    Select,
    TextField,
    Typography
} from "@material-ui/core";
import MaterialTable from "material-table";

const datatypes = ['integer', 'boolean', 'real', 'dictionary', 'discrete', 'other', 'function'];

export default function Parameters({setAlgorithmParameters, setAlgorithmHyperparameters, setModelParameters}) {

    var [AlgorithmParameter, setAlgorithmParameter] = useState('');
    const [AlgorithmParameterDatatype, setAlgorithmParameterDatatype] = useState('');

    // var [AlgorithmHyperparameter, setAlgorithmHyperparameter] = useState('');
    // var [ModelParameter, setModelParameter] = useState('');
    // const [AlgorithmHyperparameterDatatype, setAlgorithmHyperparameterDatatype] = useState('');
    // const [ModelParameterDatatype, setModelParameterDatatype] = useState('');

    const [selectedRows, setSelectedRows] = useState([]);
    const [tableData, setTableData] = useState([]);

    const columns = [
        // {title: "Parameter Type", field: "parameterType"},
        {title: "Parameter Name", field: "parameterName"},
        {title: 'Parameter Datatype', field: "parameterDatatype"}
    ]

    const handleBulkDelete = () => {
        const updatedData = tableData.filter(row => !selectedRows.includes(row));
        setTableData(updatedData);
        const alg_params = {algorithmParameters: updatedData.filter(row => row.parameterType === 'AlgorithmParameter')};
        // const alg_hyperparams = {algorithmHyperparameters: updatedData.filter(row => row.parameterType === 'AlgorithmHyperparameter')};
        // const model_params = {modelParameters: updatedData.filter(row => row.parameterType === 'ModelParameter')};

        setAlgorithmParameters(alg_params.algorithmParameters);
        // setAlgorithmHyperparameters(alg_hyperparams.algorithmHyperparameters);
        // setModelParameters(model_params.modelParameters);
    }

    const AddParameter = () => {
        if (AlgorithmParameter.length > 0) {
            const param = {
                parameterType: 'AlgorithmParameter',
                parameterName: AlgorithmParameter,
                parameterDatatype: AlgorithmParameterDatatype
            };
            const newTableData = tableData.concat(param);
            setTableData(newTableData);
            const update = {algorithmParameters: newTableData.filter(row => row.parameterType === 'AlgorithmParameter')};
            setAlgorithmParameters(update.algorithmParameters);
        }
    }

    // const AddHyperparameter = () => {
    //     if (AlgorithmHyperparameter.length > 0) {
    //         const param = {
    //             parameterType: 'AlgorithmHyperparameter',
    //             parameterName: AlgorithmHyperparameter,
    //             parameterDatatype: AlgorithmHyperparameterDatatype
    //         };
    //         const newTableData = tableData.concat(param);
    //         setTableData(newTableData);
    //         const update = {algorithmHyperparameters: newTableData.filter(row => row.parameterType === 'AlgorithmHyperparameter')};
    //         setAlgorithmHyperparameters(update.algorithmHyperparameters);
    //     }
    // }
    //
    // const AddModelParameter = () => {
    //     if (ModelParameter.length > 0) {
    //         const param = {
    //             parameterType: 'ModelParameter',
    //             parameterName: ModelParameter,
    //             parameterDatatype: ModelParameterDatatype
    //         };
    //         const newTableData = tableData.concat(param);
    //         setTableData(newTableData);
    //         const update = {modelParameters: newTableData.filter(row => row.parameterType === 'ModelParameter')};
    //         setModelParameters(update.modelParameters);
    //     }
    // }

    return (
        <Card>
            <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 30}}>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Parameters
                    </Typography>
                </Grid>
                <Grid item xs={12}>
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
                <Grid item xs={12}>
                    <FormControl fullWidth size="small" variant="outlined">
                        <InputLabel shrink>Algorithm Parameter Datatype</InputLabel>
                        <Select onChange={e => setAlgorithmParameterDatatype(e.target.value)}>
                            {datatypes.map((AlgorithmParameterDatatype) => (
                                <MenuItem key={AlgorithmParameterDatatype}
                                          value={AlgorithmParameterDatatype}>
                                    {AlgorithmParameterDatatype}
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </Grid>
                <Grid container justify="flex-end">
                    <Grid item xs={4}>
                        <Button type="reset" variant={"contained"} color={"primary"}
                                onClick={AddParameter} style={{width: 150, height: 50}}>
                            Add
                        </Button>
                    </Grid>
                </Grid>
                {/*<Grid item xs={12}>*/}
                {/*    <TextField*/}
                {/*        required={true}*/}
                {/*        fullWidth={true}*/}
                {/*        label={'Algorithm Hyperparameter Name'}*/}
                {/*        InputLabelProps={{shrink: true}}*/}
                {/*        variant={"outlined"}*/}
                {/*        value={AlgorithmHyperparameter}*/}
                {/*        onChange={e => setAlgorithmHyperparameter(e.target.value)}*/}
                {/*    />*/}
                {/*</Grid>*/}
                {/*<Grid item xs={12}>*/}
                {/*    <FormControl fullWidth size="small" variant="outlined">*/}
                {/*        <InputLabel shrink>Algorithm Hyperparameter Datatype</InputLabel>*/}
                {/*        <Select onChange={e => setAlgorithmHyperparameterDatatype(e.target.value)}>*/}
                {/*            {datatypes.map((AlgorithmHyperparameterDatatype) => (*/}
                {/*                <MenuItem key={AlgorithmHyperparameterDatatype}*/}
                {/*                          value={AlgorithmHyperparameterDatatype}>*/}
                {/*                    {AlgorithmHyperparameterDatatype}*/}
                {/*                </MenuItem>*/}
                {/*            ))}*/}
                {/*        </Select>*/}
                {/*    </FormControl>*/}
                {/*</Grid>*/}
                {/*<Grid container justify="flex-end">*/}
                {/*    <Grid item xs={4}>*/}
                {/*        <Button type="reset" variant={"contained"} color={"primary"}*/}
                {/*                onClick={AddHyperparameter} style={{width: 150, height: 50}}>*/}
                {/*            Add*/}
                {/*        </Button>*/}
                {/*    </Grid>*/}
                {/*</Grid>*/}
                {/*<Grid item xs={12}>*/}
                {/*    <TextField*/}
                {/*        required={true}*/}
                {/*        fullWidth={true}*/}
                {/*        label={'Model Parameter Name'}*/}
                {/*        InputLabelProps={{shrink: true}}*/}
                {/*        variant={"outlined"}*/}
                {/*        value={ModelParameter}*/}
                {/*        onChange={e => setModelParameter(e.target.value)}*/}
                {/*    />*/}
                {/*</Grid>*/}
                {/*<Grid item xs={12}>*/}
                {/*    <FormControl fullWidth size="small" variant="outlined">*/}
                {/*        <InputLabel shrink>Model Parameter Datatype</InputLabel>*/}
                {/*        <Select onChange={e => setModelParameterDatatype(e.target.value)}>*/}
                {/*            {datatypes.map((ModelParameterDatatype) => (*/}
                {/*                <MenuItem key={ModelParameterDatatype} value={ModelParameterDatatype}>*/}
                {/*                    {ModelParameterDatatype}*/}
                {/*                </MenuItem>*/}
                {/*            ))}*/}
                {/*        </Select>*/}
                {/*    </FormControl>*/}
                {/*</Grid>*/}
                {/*<Grid container justify="flex-end">*/}
                {/*    <Grid item xs={4}>*/}
                {/*        <Button type="reset" variant={"contained"} color={"primary"}*/}
                {/*                onClick={AddModelParameter} style={{width: 150, height: 50}}>*/}
                {/*            Add*/}
                {/*        </Button>*/}
                {/*    </Grid>*/}
                {/*</Grid>*/}
                <Grid item xs={12}>
                    <MaterialTable
                        title="Parameters"
                        data={tableData}
                        onSelectionChange={(rows) => setSelectedRows(rows)}
                        columns={columns}
                        options={{
                            selection: true
                        }}
                        actions={[
                            {
                                icon: 'delete',
                                tooltip: 'Delete all selected rows',
                                onClick: () => handleBulkDelete()
                            }
                        ]}
                    />
                </Grid>
            </Grid>
        </Card>
    );
}