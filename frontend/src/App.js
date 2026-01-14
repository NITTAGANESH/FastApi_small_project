import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Products from "./Products";
import ProtectedRoute from "./ProductedRoute";

function App() {
  return (
    <BrowserRouter>
        <Routes>
            <Route path="/" element={<Login/>}/>
            <Route path="/register" element={<Register/>}/>
            <Route 
              path="/products"
                element={
                    <ProtectedRoute>
                        <Products/>
                    </ProtectedRoute>
                }
            />
        </Routes>
    </BrowserRouter>
  );
}

export default App;