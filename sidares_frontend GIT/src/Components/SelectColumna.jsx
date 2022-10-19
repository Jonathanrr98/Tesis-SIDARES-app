import React from "react";
import Form from "react-bootstrap/Form";
import axios from "axios";
import { useEffect, useState } from "react";
import Button from "react-bootstrap/Button";
import toast from "react-hot-toast";
import { Toaster } from "react-hot-toast";
import Select from "react-select";
import AmbiguedadesDetectadas from "./AmbiguedadesDetectadas";

let url = "http://127.0.0.1:8000/colum";
let urlColumna = "http://127.0.0.1:8000/filter";
const secretKey = localStorage.getItem("key");

const SelectColumna = (props) => {
  
  const actualizar = props.actualizar;
  const updateTextArea = props.updateTextArea



  const [selection, setselection] = useState([]);
  const [selectedOption, setSelectedOption] = useState(null);
  const [cabecera, setcabecera] = useState("");
  const [actualizarC, setactualizarC] = useState(0);
  const [load, setload] = useState(undefined);


  const options = selection.map((item) => {
    return {
      label: item,
      value: item,
    };
  });

  const clickBoton = (r) => {
    r.preventDefault();
    if (selectedOption == null){
      toast.error("Debe seleccionar una columna")
    }
    let cabeceras = "";
    cabeceras = selectedOption["value"];
    setcabecera(selectedOption["value"]);
    setcabecera(cabeceras);
    setactualizarC(actualizarC + 1);
    enviarColumna();
    setload(false)

  };

  useEffect(() => {
    obtenerDatos();
  }, [actualizar,updateTextArea]);

  const obtenerDatos = () => {
    axios.get(url).then((response) => {
      setselection(response.data);
      console.log(response.data);
    });
  };

  const enviarColumna = () => {
    if (cabecera !== "") {
      axios

        .get(
          urlColumna,
          { params: { cabecera: cabecera }},
          {
            
            headers: {
              "Content-Type": "multipart/form-data",
              Authorization: `token ${secretKey}`,
            },
          }
        )
        .then((resp) => {
          console.log(resp.status);
          obtenerDatos();
        });
      toast.success("Procesado!");
    } else if (selection.value === null) {
      toast.error("Seleccione una columna!");
      return;
    }
  };
  return (
    <div className="row">
      <form >
        <Form.Label>Seleccione la columna a procesar</Form.Label>
        <div className="row ">
        <div className="col-6">
          <Select
            placeholder="Seleccione una columna"
            defaultValue={"Null"}
            onChange={setSelectedOption}
            options={options}
          />
        </div>

        <div className="col-6">
          <Button
        
            onClick={clickBoton}
            type="submit"
            variant="primary"
            className="ms-4"
          >
            Procesar columna
          </Button>


        </div>
        </div>
        <Toaster position="bottom-center" reverseOrder={false} />
      </form>

      <AmbiguedadesDetectadas actualizarC={actualizarC} load={load} />
    </div>
  );
};

export default SelectColumna;
