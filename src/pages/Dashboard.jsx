import { useNavigate } from "react-router-dom";
import StatCard from "../components/StatCard";

export default function Dashboard() {
  const navigate = useNavigate();

  const stats = [
    { title: "Active Vessels", value: "0", description: "Fleet currently monitored" },
    { title: "Fuel Saved", value: "0", description: "Compared with baseline" },
    { title: "CO₂ Reduction", value: "0", description: "Across optimized voyages" },
    { title: "Scenarios", value: "0", description: "Optimization scenarios" }
  ];

  const recentScenarios = [
    { id: "S10241", route: "Mumbai → Dubai", objective: "Balanced", status: "Completed" },
    { id: "S10240", route: "Singapore → Mumbai", objective: "Emissions", status: "Completed" },
    { id: "S10239", route: "Chennai → Colombo", objective: "Fuel", status: "Completed" }
  ];

  const workflow = [
    { number: "01", title: "Input data", description: "Cargo, distance and time requirements" },
    { number: "02", title: "Fuel prediction", description: "Predict consumption under conditions" },
    { number: "03", title: "Optimization", description: "Find the best feasible combination" },
    { number: "04", title: "Decision", description: "Select the greener fleet strategy" }
  ];

  return (
    <>
      <section className="hero">
        <div>
          <span className="eyebrow">GREEN FLEET INTELLIGENCE</span>
          <h1>Plan cleaner voyages<br />with <em>better decisions.</em></h1>
          <p>
            Predict fuel consumption and optimize fleet decisions
            using operational, environmental and business constraints.
          </p>
        </div>
        <button className="primary" onClick={() => navigate("/optimize")}>
          Create Scenario
        </button>
      </section>

      <section className="grid4">
        {stats.map((item, index) => (
          <StatCard key={index} title={item.title} value={item.value} description={item.description} />
        ))}
      </section>

      <section className="columns">
        <div className="card">
          <h2>Recent optimization scenarios</h2>
          {recentScenarios.map((scenario) => (
            <div className="row" key={scenario.id}>
              <div>
                <b>{scenario.id}</b>
                <p>{scenario.route}</p>
              </div>
              <div>
                <span>{scenario.objective}</span>
                <small>{scenario.status}</small>
              </div>
            </div>
          ))}
        </div>

        <div className="card highlight">
          <h2>How GreenFleetQ works</h2>
          <p>
            The platform connects fuel prediction with
            multi-objective fleet optimization.
          </p>
          <div className="flow">
            <span>Prediction</span><i>→</i>
            <span>Optimization</span><i>→</i>
            <span>Decision</span>
          </div>
        </div>
      </section>

      <section className="card">
        <h2>Optimization workflow</h2>
        <div className="workflow">
          {workflow.map((item) => (
            <div className="workflow-item" key={item.number}>
              <span>{item.number}</span>
              <div>
                <h3>{item.title}</h3>
                <p>{item.description}</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
