import logo from './logo.svg';
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
   
      <div className="container">
        <div className="app">
          <Routes>
            <Route path="/" element={<HomePage/>} />
            
          </Routes>
        </div>
      </div>
    
  </Router>
  )
}

export default App;
