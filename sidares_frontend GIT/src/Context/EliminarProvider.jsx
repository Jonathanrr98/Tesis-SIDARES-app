import { createContext } from "react";
import { useState } from "react";
import { useContext } from "react";

const eliminarContext = createContext();
const ActEliminarContext = createContext();

export function useEliminarContext() {
  return useContext(eliminarContext);
}

export function useActEliminarContext() {
  return useContext(ActEliminarContext);
}

export function EliminarProvider(props) {
  const [eliminar, seteliminar] = useState(0);

  const actualizarEliminar = () => {
    seteliminar(eliminar + 1);
  };

  return (
    <eliminarContext.Provider value={eliminar}>
      <ActEliminarContext.Provider value={actualizarEliminar}>
        {props.children}
      </ActEliminarContext.Provider>
    </eliminarContext.Provider>
  );
}
