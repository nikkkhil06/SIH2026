import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Dashboard from "./pages/Dashboard";
import Optimization from "./pages/Optimization";
import Results from "./pages/Results";

export default function App() {
  return (
    <>
      <Navbar />
      <main className="container">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/optimize" element={<Optimization />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </main>
    </>
  );
}
