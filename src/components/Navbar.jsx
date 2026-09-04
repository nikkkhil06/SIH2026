import { NavLink } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="brand">
        <div className="brand-mark">GF</div>
        <div>
          <b>GreenFleetQ</b>
          <small>Fleet management & optimization</small>
        </div>
      </div>

      <div className="links">
        <NavLink to="/">Dashboard</NavLink>
        <NavLink to="/optimize">Optimize</NavLink>
        <NavLink to="/results">Results</NavLink>
      </div>
    </nav>
  );
}
