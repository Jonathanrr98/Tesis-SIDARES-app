import React from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import EliminarAmbiguedades from "./EliminarAmbiguedades";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import { useEliminarContext } from "../Context/EliminarProvider";

function AmbiguedadesDetectadas(props) {
  const actualizar = props;
  const [tareas, setTareas] = React.useState([]);
  const eliminar = useEliminarContext();

  React.useEffect(() => {
    axios.get(`http://127.0.0.1:8000/verambiguedades/`).then((response) => {
      setTareas(response.data);
    });
  }, [actualizar,eliminar]);

  return (
    <div className="row mt-5">
      <div className="col-12">
        <h4 className="text-center">Lista de ambiguedades</h4>

        <div className="mt3 mb-3">
          <EliminarAmbiguedades />
        </div>
        <ul className="list-group">
          {tareas.length === 0 ? (
            <li className="list-group-item">No existen ambiguedades</li>
          ) : (
            tareas.map((item) => (
              <>
                <Card className="mb-3" key={item.id}>
                  <Card.Header>
                    <strong>{item.tipo}</strong>
                  </Card.Header>
                  <ListGroup variant="flush">
                    <ListGroup.Item>{item.descripcion}</ListGroup.Item>
                    <ListGroup.Item>{item.requisito}</ListGroup.Item>
                  </ListGroup>
                </Card>
              </>
            ))
          )}
        </ul>
      </div>
    </div>
  );
}

export default AmbiguedadesDetectadas;
