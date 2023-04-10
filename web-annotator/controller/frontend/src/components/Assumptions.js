import React, {useState} from "react";
import {
    Button,
    Card,
    Checkbox,
    FormControl,
    Grid,
    Input,
    InputLabel,
    ListItemText,
    MenuItem,
    Paper,
    Select,
    TextField,
    Typography
} from "@material-ui/core";
import MaterialTable from "material-table";


const assumptions = [
    'No assumptions',
    'Independence of observations',
    'No hidden or missing variables',
    'Linear relationship',
    'Normality of residuals',
    'No or little multicollinearity',
    'Homoscedasticity',
    'All independent variables are uncorrelated with the error term',
    'Observations of the error term are uncorrelated with each other',
    'Similar things exist in close proximity',
    'Conditional independence between every pair of features given the value of the class variable',
    'The likelihood of the features is assumed to be Gaussian',
];

export default function Assumptions({setAssumptions, setNewAssumptions}) {

    const [Assumption, setAssumption] = useState([]);
    let [newAssumption, setNewAssumption] = useState('');
    const [tableData, setTableData] = useState([]);
    const [selectedRows, setSelectedRows] = useState([]);
    const columns = [
        {title: 'Assumption', field: 'Assumption'}
    ]

    const handleBulkDelete = () => {
        const updatedData = tableData.filter(row => !selectedRows.includes(row));
        setTableData(updatedData);
        setNewAssumptions(updatedData);
    };
    const AddAssumptions = () => {
        if (newAssumption.length <= 0) {
            return;
        }
        const param = {Assumption: newAssumption};
        const newTableData = tableData.concat(param);
        setTableData(newTableData);
        setNewAssumptions(newTableData);
    };
    const setAssumptionData = (data) => {
        setAssumption(data);
        setAssumptions(data);
    };

    return (
        <Card>
            <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 50}}>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Assumptions
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <FormControl style={{minWidth: 500, minHeight: 100}}>
                        <InputLabel>Algorithm Assumptions</InputLabel>
                        <Select
                            fullWidth
                            multiple
                            value={Assumption}
                            onChange={e => setAssumptionData(e.target.value)}
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
                <Grid item xs={12}>
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
                <Grid container justify="flex-end">
                    <Grid item xs={4}>
                        <Button variant={"contained"} color={"primary"} onClick={AddAssumptions}
                                style={{width: 150, height: 50}}>
                            Add
                        </Button>
                    </Grid>
                </Grid>
            </Grid>
            <Grid item xs={12}>
                <MaterialTable
                    title="Assumptions"
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
        </Card>
    );
}