import "bootstrap/dist/css/bootstrap.min.css";
import Bar from "./Components/Bar";
import Crud from "./Components/Crud";
import { EliminarProvider } from "./Context/EliminarProvider";

function App() {
  return (
    
    <EliminarProvider>
      <header className="App-header">
        <Bar />
      </header>
      <div className=" col-12 container">
        <Crud />
      </div>
      <div className=" col-12 container">
     
      </div>
      </EliminarProvider>
    
  );
}

export default App;
