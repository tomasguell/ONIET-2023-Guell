import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';
function NavBar() {
  return (
    <Navbar bg="primary" expand="md">  
    <Container>  
      <Navbar.Brand href="/">ITS VILLADA</Navbar.Brand>  
      <Navbar.Toggle aria-controls="basic-navbar-nav" />  
      <Navbar.Collapse id="basic-navbar-nav">  
        <Nav className="me-auto">  
<<<<<<< HEAD
        <Nav.Link href="Empresas">Empresas</Nav.Link>  
        <Nav.Link href="#home">Informe De Rendimiento</Nav.Link>  
=======
        <Nav.Link href="/Empresas">Empresas</Nav.Link>  
        <Nav.Link href="/">Informe De Rendimiento</Nav.Link>  
>>>>>>> 126a8bc47a981720061e2e668bbe6e22cfebd5db

    
        </Nav>  
      </Navbar.Collapse>  
    </Container>  
  </Navbar>  
  );
}

export default NavBar;
