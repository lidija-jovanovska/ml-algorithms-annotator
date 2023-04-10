import React, {useEffect, useState} from "react";
import {
    Button,
    Card, Checkbox,
    FormControl,
    Grid,
    Input,
    InputLabel, ListItemText,
    MenuItem,
    Paper,
    Select,
    TextField,
    Typography
} from "@material-ui/core";
import {default as axios} from "axios";
import MaterialTable from "material-table";


export default function Algorithms({setSelectedSimpleAlgorithms, setNewSimpleAlgorithms}) {

    const [simpleAlgorithms, setSimpleAlgorithms] = useState([]);
    const [selectedAlgorithms, setSelectedAlgorithms] = useState([]);
    const [newSimpleAlgorithm, setNewSimpleAlgorithm] = useState('');

    const [tableData, setTableData] = useState([]);
    const [selectedRows, setSelectedRows] = useState([]);
    const columns = [
        {title: 'Algorithm', field: 'simpleAlgorithms'}
    ]

    const handleBulkDelete = () => {
        const updatedData = tableData.filter(row => !selectedRows.includes(row));
        setTableData(updatedData);
        setNewSimpleAlgorithms(updatedData);
    };
    const AddAlgorithms = () => {
        if (newSimpleAlgorithm.length <= 0) {
            return;
        }
        const param = {simpleAlgorithms: newSimpleAlgorithm};
        const newTableData = tableData.concat(param);
        setTableData(newTableData);
        setNewSimpleAlgorithms(newTableData);
    };

    useEffect(() => {
        getSimpleAlgorithms();
    }, []);

    const set_algorithms = (algorithms) => {
        setSelectedAlgorithms(algorithms);
        setSelectedSimpleAlgorithms(algorithms);
    };

    function getSimpleAlgorithms() {

        axios.get('api/simple_algorithms/', {
        }).then(response => {
            setSimpleAlgorithms(response.data);
            console.log(simpleAlgorithms);
        });
    }

    return (
        <Card>
            <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 20}}>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Algorithms Info
                    </Typography>
                    <Typography variant={"subtitle1"}>
                        Select a constituent algorithm or add a new one.
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <FormControl style={{minWidth: 500, minHeight: 100}}>
                        <InputLabel>Algorithms</InputLabel>
                        <Select
                            fullWidth
                            multiple
                            value={selectedAlgorithms}
                            onChange={e => set_algorithms(e.target.value)}
                            input={<Input/>}
                            renderValue={(selected) => selected.join(', ')}
                        >
                            {simpleAlgorithms.map((name) => (
                                <MenuItem key={name} value={name}>
                                    <Checkbox checked={selectedAlgorithms.indexOf(name) > -1}/>
                                    <ListItemText primary={name}/>
                                </MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Constituent Algorithm'}
                        InputLabelProps={{shrink: true}}
                        helperText={"Add a New Constituent Algorithm that is used by the Annotated Data Mining Algorithm."}
                        variant={"outlined"}
                        onChange={e => setNewSimpleAlgorithm(e.target.value)}
                    />
                </Grid>
                <Grid container justify="flex-end">
                    <Grid item xs={4}>
                        <Button variant={"contained"} color={"primary"} onClick={AddAlgorithms}
                                style={{width: 150, height: 50}}>
                            Add
                        </Button>
                    </Grid>
                </Grid>
                <Grid item xs={12}>
                    <MaterialTable
                        title="Algorithms"
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