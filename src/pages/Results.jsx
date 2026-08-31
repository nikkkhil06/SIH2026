import {useNavigate} from "react-router-dom";
import {result,comparison} from "../data/mockData";

export default function Results(){
 const navigate=useNavigate(); const max=Math.max(...comparison.map(x=>x.value));
 return <div>
  <section className="heading"><button className="back" onClick={()=>navigate("/optimize")}>← Modify Scenario</button><span className="eyebrow">OPTIMIZATION COMPLETE</span><h1>Recommended Fleet Strategy</h1><p>Scenario S001 • Balanced objective</p></section>
  <div className="recommend card"><div><span>RECOMMENDED VESSEL</span><h2>{result.vessel}</h2><p>{result.fuel} • {result.speed} knots</p></div><b>✓ Feasible Solution</b></div>
  <section className="grid4">
   <div className="card stat"><span>Predicted Fuel</span><strong>{result.predictedFuel.toLocaleString()}</strong><small>kg</small></div>
   <div className="card stat"><span>Estimated Cost</span><strong>₹{result.cost.toLocaleString()}</strong><small>per scenario</small></div>
   <div className="card stat"><span>Estimated GHG</span><strong>{result.emissions.toLocaleString()}</strong><small>kg CO₂e</small></div>
   <div className="card stat"><span>Cruising Speed</span><strong>{result.speed}</strong><small>knots</small></div>
  </section>
  <section className="columns">
   <div className="card"><span className="eyebrow">FUEL SCENARIO COMPARISON</span><h2>Predicted consumption</h2>
    {comparison.map(x=><div className="barrow" key={x.fuel}><span>{x.fuel}</span><div><i style={{width:(x.value/max*100)+"%"}} className={x.fuel===result.fuel?"recommended":""}/></div><b>{x.value.toLocaleString()}</b></div>)}
   </div>
   <div className="card"><span className="eyebrow">CONSTRAINT CHECK</span><h2>Operational feasibility</h2>
    {["Cargo requirement","Schedule requirement","Available vessel","Selected fuel scenario"].map(x=><div className="check" key={x}>✓ <span>{x}</span><b>Satisfied</b></div>)}
   </div>
  </section>
 </div>;
}