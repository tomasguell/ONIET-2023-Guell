import './App.css';
import HomePage from './pages/home';
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
            
          </Routes>
        </div>
      </div>
    
  </Router>
  )
}

export default App;
