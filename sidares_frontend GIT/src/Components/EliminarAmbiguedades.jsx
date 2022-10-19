import React from "react";
import axios from "axios";
import { useActEliminarContext } from "../Context/EliminarProvider";

export default function EliminarAmbiguedades() {
  const actualizarEliminar = useActEliminarContext();

  const url = "http://localhost:8000/verambiguedades/";

  const click = (e) => {
    e.preventDefault();
    axios.post(url);
    actualizarEliminar();
    window.location.reload();
  };

  return (
    <div className="container ">
      <button
        id="btn-table"
        className="btn btn-danger btn-sm float-right mx-2"
        onClick={click}
      >
        Eliminar lista de ambiguedades
      </button>
    </div>
  );
}
