import {useNavigate} from "react-router-dom";
import StatCard from "../components/StatCard";
import {stats} from "../data/mockData";

export default function Dashboard(){
 const navigate=useNavigate();
 return <div>
  <section className="hero">
   <div><span className="eyebrow">FLEET OPTIMIZATION PLATFORM</span>
   <h1>Make every voyage <em>greener.</em></h1>
   <p>Predict fuel consumption and find the best vessel, speed and fuel combination while respecting operational constraints.</p></div>
   <button className="primary" onClick={()=>navigate("/optimize")}>Create Scenario →</button>
  </section>
  <section className="grid4">{stats.map(s=><StatCard key={s.title}{...s}/>)}</section>
  <section className="columns">
   <div className="card"><span className="eyebrow">RECENT ACTIVITY</span><h2>Optimization Scenarios</h2>
    {["S001 • V07 • LNG","S002 • V03 • Methanol","S003 • V11 • LNG"].map(x=><div className="row" key={x}><span>{x}</span><b>✓ Completed</b></div>)}
   </div>
   <div className="card highlight"><span className="eyebrow">CORE WORKFLOW</span><h2>Prediction → Optimization → Decision</h2>
    <p>Operational data is used to predict fuel consumption, then the optimizer searches for the best feasible fleet strategy.</p>
    <div className="flow"><span>Data</span>→<span>ML</span>→<span>Optimizer</span>→<span>Decision</span></div>
   </div>
  </section>
 </div>;
}