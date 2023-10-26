import React from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Container from 'react-bootstrap/Container';
function NavBar() {
  return (
    <Navbar bg="primary" expand="md">  
    <Container>  
      <Navbar.Brand href="#home">ITS VILLADA</Navbar.Brand>  
      <Navbar.Toggle aria-controls="basic-navbar-nav" />  
      <Navbar.Collapse id="basic-navbar-nav">  
        <Nav className="me-auto">  
        <Nav.Link href="#home">Informe De Rendimiento</Nav.Link>  
          <Nav.Link href="#link">Informacion Raw</Nav.Link> 
        </Nav>  
      </Navbar.Collapse>  
    </Container>  
  </Navbar>  
  );
}

export default NavBar;
