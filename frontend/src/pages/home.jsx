import NavBar from './NavBar';
import { useEffect,useState, React } from 'react';





function HomePage() {

    const [data, setData] = useState(null); // Estado para almacenar los datos
    const [loading, setLoading] = useState(true); // Estado para controlar la carga
  
    useEffect(() => {
      // Realizar la solicitud fetch en el efecto de montaje
      fetch('http://127.0.0.1:8000/api/EmpresaListCreateView/')
        .then(response => response.json())
        .then(data => {
            console.log("a")
          setData(data); // Almacenar los datos en el estado
          setLoading(false); // Cambiar el estado de carga a falso
        })
        .catch(error => {
          console.error('Error en la solicitud fetch:', error);
          setLoading(false); // En caso de error, cambiar el estado de carga a falso
        });
    }, []);

    

  
  return (
    <div className='pagecontainer container'>
        <NavBar></NavBar>
      Hola
    </div>
  );
}

export default HomePage;
