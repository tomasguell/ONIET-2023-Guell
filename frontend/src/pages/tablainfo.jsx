import React from 'react'
import { DataGrid, GridRowsProp, GridColDef } from '@mui/x-data-grid';



function Tablainfo() {
    
    const rows: GridRowsProp = [
        { id: 1, col1: 'Hello', col2: 'World' },
        { id: 2, col1: 'DataGridPro', col2: 'is Awesome' },
        { id: 3, col1: 'MUI', col2: 'is Amazing' },
      ];
      
      const columns: GridColDef[] = [
        { field: 'id', headerName: 'ID',headerAlign: "center",align: "center", width: 30},
        { field: 'nombre', headerName: 'Nombre', headerAlign: "center",align: "center", width: 300 },
      ];
  return (
    <div>
        <DataGrid 
            rows={rows} 
            columns={columns} 
        />
    </div>
  )
}

export default Tablainfo;