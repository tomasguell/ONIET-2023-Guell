import React from 'react';
import Table from 'react-bootstrap/Table';
function TableComponent({ data }) {
  // Convierte el objeto JSON en un array de objetos para facilitar el mapeo

  return (
    
<div>
   
      <Table responsive striped bordered hover className="mt-3">
        
        <tbody>
          {data.map((presupuesto) => (
            <tr
              key={presupuesto.id}
             
              className={`cursor-pointer`}
            >
              <td>{presupuesto.Producción_Total}</td>
              <td>{presupuesto.Cantidad_Piezas_Ok}</td>
              <td>{presupuesto.CantidaPiezasError}</td>
              <td>{presupuesto.porcentaje_Piezas_Ok}</td>
              <td >{presupuesto.porcentaje_Piezas_Error}</td>
            </tr>
          ))}
        </tbody>
      </Table>
      
      </div>
  );
}

export default TableComponent;
