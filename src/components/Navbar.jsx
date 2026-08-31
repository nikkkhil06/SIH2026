import {NavLink} from "react-router-dom";
export default function Navbar(){
 return <nav className="navbar">
   <div className="brand">⚓ <div><b>GreenFleetQ</b><small>Green Fleet Intelligence</small></div></div>
   <div className="links">
    <NavLink to="/">Dashboard</NavLink>
    <NavLink to="/optimize">Optimize</NavLink>
    <NavLink to="/results">Results</NavLink>
   </div>
 </nav>;
}