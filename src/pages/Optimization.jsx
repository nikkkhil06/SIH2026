import {useState} from "react";
import {useNavigate} from "react-router-dom";

export default function Optimization(){
 const navigate=useNavigate();
 const [form,setForm]=useState({cargo:"15000",distance:"800",time:"36",objective:"balanced"});
 const [fuels,setFuels]=useState(["Diesel","LNG","Methanol"]);
 const [vessels,setVessels]=useState(["V01","V02","V03","V07"]);

 const toggle=(arr,setter,item)=>setter(arr.includes(item)?arr.filter(x=>x!==item):[...arr,item]);
 const change=e=>setForm({...form,[e.target.name]:e.target.value});

 return <div>
  <section className="heading"><span className="eyebrow">OPTIMIZATION ENGINE</span><h1>Create Optimization Scenario</h1>
  <p>Enter voyage requirements and let the system find a feasible vessel-speed-fuel configuration.</p></section>
  <form className="columns" onSubmit={e=>{e.preventDefault();navigate("/results")}}>
   <div className="card">
    <h2>Voyage Requirements</h2>
    <div className="formgrid">
     <label>Cargo Demand (tonnes)<input name="cargo" type="number" value={form.cargo} onChange={change}/></label>
     <label>Distance (nautical miles)<input name="distance" type="number" value={form.distance} onChange={change}/></label>
     <label>Maximum Time (hours)<input name="time" type="number" value={form.time} onChange={change}/></label>
    </div>
    <h3>Available Vessels</h3>
    <div className="choices">{["V01","V02","V03","V07","V11","V15"].map(v=><button type="button" className={vessels.includes(v)?"choice selected":"choice"} onClick={()=>toggle(vessels,setVessels,v)} key={v}>{v}</button>)}</div>
    <h3>Fuel Options</h3>
    <div className="choices">{["Diesel","LNG","Methanol","Hydrogen","Ammonia"].map(f=><button type="button" className={fuels.includes(f)?"choice selected":"choice"} onClick={()=>toggle(fuels,setFuels,f)} key={f}>{f}</button>)}</div>
   </div>
   <div className="card">
    <h2>Optimization Objective</h2>
    {[
      ["fuel","Minimum Fuel"],["cost","Minimum Cost"],["emissions","Minimum Emissions"],["balanced","Balanced"]
    ].map(([value,label])=><label className="radio" key={value}><input type="radio" name="objective" value={value} checked={form.objective===value} onChange={change}/><div><b>{label}</b><small>{value==="balanced"?"Balance fuel, cost and emissions.":"Prioritize "+label.toLowerCase()+"."}</small></div></label>)}
    <div className="constraint"><b>✓ Constraints enforced</b><small>Cargo and schedule requirements must remain satisfied.</small></div>
    <button className="primary full" type="submit">🚀 Optimize Fleet</button>
   </div>
  </form>
 </div>;
}