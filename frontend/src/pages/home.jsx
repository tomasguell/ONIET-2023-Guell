import React from 'react';
import NavBar from './NavBar';
import { useEffect,useState} from 'react';


import './home.css';


import { DataGrid, GridToolbarExport, 
  GridToolbarContainer } from '@mui/x-data-grid';

const columns = [ 
  { field: 'Empresa', headerName: 'Empresa', width: 170 }, 
  { field: 'Produccion Total', headerName: 'Producción Total', width: 170 }, 
  { field: 'Cantidad Piezas Ok', headerName: 'Cantidad Piezas Ok', width: 170 }, 
  { field: 'Cantidad Piezas Error', headerName: 'Cantidad Piezas Error', width: 170 }, 
  { field: '%Piezas Ok', headerName: '%Piezas Ok', width: 170 }, 
  { field: '%Piezas Error', headerName: '%Piezas Error', width: 170 },
]; 

const rows = [ 
  {'id':0, 'Empresa': 'Empresa 1', 'Produccion Total': 3608, 'Cantidad Piezas Ok': 2945, 'Cantidad Piezas Error': 663, '%Piezas Ok': 0.8162416851441242, '%Piezas Error': 0.18375831485587582} ,
]; 
  
function MyExportButton() { 
  return ( 
    <GridToolbarContainer> 
      <GridToolbarExport /> 
    </GridToolbarContainer> 
  ); 
}


function HomePage() {
    const [data, setData] = useState(rows); // Estado para almacenar los datos
    const [loading, setLoading] = useState(true); // Estado para controlar la carga
    useEffect(() => {
      // Realizar la solicitud fetch en el efecto de montaje
      fetch('http://127.0.0.1:8000/api/dataProccessing/')
        .then(response => response.json())
        .then(data => {
            console.log(data['msg'])
          setData(data['msg']); // Almacenar los datos en el estado
          setLoading(false); // Cambiar el estado de carga a falso
        })
        .catch(error => {
          console.error('Error en la solicitud fetch:', error);
          setLoading(false); // En caso de error, cambiar el estado de carga a falso
        });
    }, []);

    console.log('columns:', columns);
    console.log('data:', data);


  return (
    <div>
        <NavBar></NavBar>
        <div style={{ height: 500, width: '80%' }}> 
        <h4> 
        How to use export our DataGrid 
        as CSV in ReactJS? 
        </h4> 
        <DataGrid rows={data} columns={columns}  
          pageSize={5}  
          components={{ 
            Toolbar: MyExportButton, 
          }} 
        /> 
      </div>

    </div>
  );
}

export default HomePage;