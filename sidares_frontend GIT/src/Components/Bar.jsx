import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

function Bar() {
  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#">
            <strong>SIDARES</strong>{" "}
            <cite className="ms-3 blockquote-footer" title="Source Title">
              Sistema de Detección de Ambiguedades en Requisitos de Software
            </cite>
          </Navbar.Brand>

          <Nav className="me-auto"></Nav>
        </Container>
      </Navbar>

      <br />
    </>
  );
}

export default Bar;
