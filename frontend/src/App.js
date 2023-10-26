import './App.css';
import HomePage from './pages/home';
import Empresas from './pages/Empresas';
import EmpresaDetalle from './pages/EmpresaDetalle';


import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";
function App() {
  return(


    <Router>
   
      <div >
        <div >
          <Routes>
            <Route path="/" element={<HomePage/>} />
            <Route path="/Empresas" element={<Empresas/>} />
            <Route path="/Empresas/:id" element={<EmpresaDetalle/>} />
          </Routes>
        </div>
      </div>
    
  </Router>
  )
}

export default App;
