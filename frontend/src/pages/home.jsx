import React from 'react';
import NavBar from './NavBar';
import Tablainfo from './tablainfo';

import './home.css';




function HomePage() {


  
  return (
    <div>
        <NavBar></NavBar>
      <div className='container-datagrid'>
        <Tablainfo />
      </div>
      
    </div>
  );
}

export default HomePage;