import React from 'react';
import NavBar from './NavBar';
import { useEffect,useState} from 'react';


import './home.css';


import { DataGrid, GridToolbarExport, 
  GridToolbarContainer } from '@mui/x-data-grid';

const columns = [ 
  { field: 'Empresa', headerName: 'Empresa', width: 170 }, 
  { field: 'Producción Total', headerName: 'Producción Total', width: 170 }, 
  { field: 'Cantidad Piezas Ok', headerName: 'Cantidad Piezas Ok', width: 170 }, 
  { field: 'Cantidad Piezas Error', headerName: 'Cantidad Piezas Error', width: 170 }, 
  { field: '%Piezas Ok', headerName: '%Piezas Ok', width: 170 }, 
  { field: '%Piezas Error', headerName: '%Piezas Error', width: 170 },
]; 

const rows = [ 
  { id: 1, name: 'Gourav', age: 12 }, 
  { id: 2, name: 'Geek', age: 43 }, 
  { id: 3, name: 'Pranav', age: 41 }, 
  { id: 4, name: 'Abhay', age: 34 }, 
  { id: 5, name: 'Pranav', age: 73 }, 
  { id: 6, name: 'Disha', age: 61 }, 
  { id: 7, name: 'Raghav', age: 72 }, 
  { id: 8, name: 'Amit', age: 24 }, 
  { id: 9, name: 'Anuj', age: 48 }, 
]; 
  
function MyExportButton() { 
  return ( 
    <GridToolbarContainer> 
      <GridToolbarExport /> 
    </GridToolbarContainer> 
  ); 
}


function HomePage() {
    const [data, setData] = useState(null); // Estado para almacenar los datos
    const [loading, setLoading] = useState(true); // Estado para controlar la carga
  
    useEffect(() => {
      // Realizar la solicitud fetch en el efecto de montaje
      fetch('http://127.0.0.1:8000/api/dataProccessing/')
        .then(response => response.json())
        .then(data => {
            console.log(data)
          setData(data); // Almacenar los datos en el estado
          setLoading(false); // Cambiar el estado de carga a falso
        })
        .catch(error => {
          console.error('Error en la solicitud fetch:', error);
          setLoading(false); // En caso de error, cambiar el estado de carga a falso
        });
    }, []);

    console.log('columns:', columns);    
    console.log('rows:', rows);    
    console.log('data:', data);


  return (
    <div>
        <NavBar></NavBar>
        <div style={{ height: 500, width: '80%' }}> 
        <h4> 
        How to use export our DataGrid 
        as CSV in ReactJS? 
        </h4> 
        <DataGrid rows={rows} columns={columns}  
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