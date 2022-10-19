import React, { Fragment } from "react";
import axios from "axios";
import Form from "react-bootstrap/Form";
import { useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import SelectColumna from "./SelectColumna";
import toast from "react-hot-toast";

const CargarPDFFuncion = (props) => {
  const updateTextArea = props;
  const [state, setState] = useState(null);
  const [actualizar, setactualizar] = useState(0);
 

  const handleImage = (e) => {
    setState({
      selectedFile: e.target.files[0],
    });
    setactualizar(actualizar + 1);
  };

  function getFileExtension(filename) {
    const ext = /[.]/.exec(filename) ? /[^.]+$/.exec(filename)[0] : undefined;
    console.log(ext);

    if (ext === "csv") {
      console.log("posted csv file ", state.selectedFile);
     

      let formData = new FormData();
      formData.append("file_uploaded", state.selectedFile);

      const secretKey = localStorage.getItem("key");
      let url = "http://127.0.0.1:8000/upload/";
      axios
        .post(url, formData, {
          params: { ext } ,
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `token ${secretKey}`,
          },
        })
        .then((resp) => {
          console.log(resp.status);
          setactualizar(actualizar + 1);
        });
      toast.success("Documento cargado!");
    } else if (ext === "xlsx") {
      console.log("posted xlsx file ", state.selectedFile);
    
      let formData = new FormData();
      formData.append("fileexe_uploaded", state.selectedFile);

      const secretKey = localStorage.getItem("key");
      let url2 = "https://127.0.0.1:8000/uploadxlsx/";
      axios
        .post(url2, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: `token ${secretKey}`,
          },
        })
        .then((resp) => {
          console.log(resp.status);
          setactualizar(actualizar + 1);
        });
      toast.success("Documento cargado!");
    }
    return ext;
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    if (state == null) {
      toast.error("Debe cargar un archivo");
    } else {
      let extencion = state.selectedFile.name;

      getFileExtension(extencion);
   
    }
  };

  return (
    <>
      <Row>
        <Col className="row col-12">
          <Fragment>
            <div className="row">
              <div className="col-6">
                <Form.Group controlId="formFile" className="mb-5 mt-3 inputf">
                  <Form.Label>Seleccione un archivo para procesar</Form.Label>
                  <Form.Control
                    accept=".csv,.xlsx"
                    type="file"
                    className="inputf"
                    display="bock"
                    onChange={handleImage}
                  />
                </Form.Group>
              </div>

              <div className="col-6">
                <form>
                  <button
                    className="btn btn-primary mt-5 ms-4 inputf"
                    type="submit"
                    onClick={(e) => handleSubmit(e)}
                  >
                    Cargar documento
                  </button>
                </form>
              </div>
            </div>
            <div className="row">
              <div className="col-12 mb-5">
                <SelectColumna
                  actualizar={actualizar}
                  updateTextArea={updateTextArea}
                />
              </div>
            </div>
          </Fragment>
        </Col>
        <Col></Col>
      </Row>
    </>
  );
};

export default CargarPDFFuncion;
