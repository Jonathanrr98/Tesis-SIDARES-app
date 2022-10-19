import React from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import CargarPDFFuncion from "./CargarPdfFuncion";
import { useEliminarContext } from "../Context/EliminarProvider";

const url = `http://127.0.0.1:8000/verambiguedades/`;

function Crud() {
  const [tarea, setTarea] = React.useState("");
  const [tareas, setTareas] = React.useState([]);
  const [error, setError] = React.useState(null);
  const [actualizar, setactualizar] = React.useState(0);
  const [updateTextArea, setupdateTextArea] = React.useState(0);
  const eliminar = useEliminarContext();

  React.useEffect(() => {
    axios.get(url).then((response) => {
      setTareas(response.data);
    });
  }, [actualizar]);

  //onchange
  const enviarRequisitos = (e) => {
    try {
      setTarea(e.target.value);
    } catch {}
  };

  //onsubmit
  const agregarRequisitos = (e) => {
    e.preventDefault();
    if (!tarea.trim()) {
      console.log("Elemento Vacío");
      setError("Escriba algo por favor...");
      return;
    } else {
      axios
        .get(`http://127.0.0.1:8000/ambiguedades/?text=${tarea}`)
        .then((res) => {
          console.log(res);
          console.log(res.data);
          setupdateTextArea(updateTextArea + 1);
        });
    }
  };
  console.log(tarea);

  return (
    <div className="container mt-3 mb-5">
      <h1 className="text-center">Detección de ambiguedades</h1>
      <hr />

      <div className="col-12 mt-5 mb-3 ">
        <form onSubmit={agregarRequisitos}>
          <div className="row">
            {error ? <span className="text-danger">{error}</span> : null}
            <div className="col-6">
              <textarea
                spellCheck="true"
                type="text"
                className="form-control mb-2  "
                placeholder="Ingrese requisitos"
                onChange={enviarRequisitos}
                value={tarea}
              />
            </div>

            <div className="col-6">
              <button className="btn btn-primary btn-block  mb-3" type="submit">
                Procesar requisitos
              </button>
            </div>
          </div>
          <div className="row">
            <div className=" container col-12">
              <CargarPDFFuncion updateTextArea={updateTextArea} />
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Crud;
