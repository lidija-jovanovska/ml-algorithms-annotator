import React, {useState} from "react";
import {Button, Card, Grid, Paper, TextField, Typography} from "@material-ui/core";
import MaterialTable from "material-table";
import Container from "./DropdownContainer";
import algorithm_types from "../../static/annotation-schema/algorithms.json";

export default function Metadata({setAlgorithmName, setDocuments, setDMAlgorithmType}) {

    const [DocumentName, setDocumentName] = useState('');
    const [DocumentId, setDocumentId] = useState('');
    const [tableData, setTableData] = useState([]);

    const [selectedRows, setSelectedRows] = useState([]);
    const columns = [
        {title: "Document ID", field: "DocumentId"},
        {title: 'Document Name', field: "DocumentName"}
    ]

    const onChange = (currentNode, selectedNodes) => {
        const alg_type = currentNode.label
        setDMAlgorithmType(alg_type);
    };

    const handleBulkDelete = () => {
        const updatedData = tableData.filter(row => !selectedRows.includes(row));
        setTableData(updatedData);
        setDocuments(updatedData);
    }

    const AddDocuments = () => {
        if (DocumentName.length <= 0) {
            return;
        }
        const param = {DocumentId: DocumentId, DocumentName: DocumentName};
        const newTableData = tableData.concat(param);
        setTableData(newTableData);
        setDocuments(newTableData);
    }

    return (
        <Card elevation={4}>
            <Grid container spacing={3} align={"center"} justify={"center"} style={{padding: 50}}>
                <Grid item xs={12}>
                    <Typography variant={"h5"} align={"left"}>
                        Metadata
                    </Typography>
                </Grid>
                <Grid item xs={12}>
                    <TextField
                        required={true}
                        fullWidth={true}
                        label={'Algorithm Name'}
                        InputLabelProps={{shrink: true}}
                        helperText={"Name of the described algorithm."}
                        variant={"outlined"}
                        // onChange={e => setAlgorithmName(e.target.value)}
                        onChange={e => setAlgorithmName(e.target.value)}
                    />
                </Grid>
                <Grid item xs={12}>
                    <Container
                        data={algorithm_types}
                        onChange={onChange}
                        texts={{placeholder: 'Algorithm type'}}
                        className={"mdl-demo"}
                        mode={"radioSelect"}
                    />
                </Grid>
                <Grid item xs={12}>
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
                <Grid item xs={12}>
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
                <Grid container justify="flex-end">
                    <Grid item xs={4}>
                        <Button type="reset" variant={"contained"}
                                color={"primary"}
                                onClick={AddDocuments}
                                style={{width: 150, height: 50, justifyContent: "center"}}>
                            Add</Button>
                    </Grid>
                </Grid>
                <Grid item xs={12}>
                    <MaterialTable
                        title="Documents"
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
};