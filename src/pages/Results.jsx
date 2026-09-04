import { useLocation, useNavigate } from "react-router-dom";

export default function Results() {
  const location = useLocation();
  const navigate = useNavigate();
  const data = location.state;

  if (!data) {
    return (
      <section className="empty-result">
        <span className="eyebrow">NO SCENARIO SELECTED</span>
        <h1>No optimization scenario found.</h1>
        <p>Create a new optimization scenario to view its results.</p>
        <button className="primary" onClick={() => navigate("/optimize")}>
          Create Scenario
        </button>
      </section>
    );
  }

  return (
    <>
      <section className="heading">
        <button className="back" onClick={() => navigate("/optimize")}>
          ← Back to Optimization
        </button>
        <span className="eyebrow">OPTIMIZATION SCENARIO</span>
        <h1>Scenario created successfully.</h1>
        <p>
          Your optimization request has been submitted to the backend optimization service.
        </p>
      </section>

      <section className="card scenario-card">
        <div>
          <span className="result-label">SCENARIO ID</span>
          <h2>{data.scenario_id}</h2>
          <p>{data.message}</p>
        </div>
        <span className="status-badge">{data.status}</span>
      </section>

      <section className="columns">
        <div className="card">
          <h2>Scenario inputs</h2>

          <div className="result-row">
            <span>Cargo Demand</span>
            <b>{data.input.cargo_demand} tonnes</b>
          </div>

          <div className="result-row">
            <span>Distance</span>
            <b>{data.input.distance} nautical miles</b>
          </div>

          <div className="result-row">
            <span>Maximum Time</span>
            <b>{data.input.max_time} hours</b>
          </div>

          <div className="result-row">
            <span>Objective</span>
            <b>{data.input.objective}</b>
          </div>
        </div>

        <div className="card highlight">
          <h2>What happens next?</h2>
          <p>
            The backend will use fleet database information and the optimization
            engine to determine the optimal vessel, fuel and operating strategy.
          </p>

          <div className="process-list">
            <div><span>01</span><p>Scenario created</p></div>
            <div><span>02</span><p>Optimizer processes the scenario</p></div>
            <div><span>03</span><p>Optimal fleet strategy generated</p></div>
          </div>
        </div>
      </section>

      <section className="card pending-card">
        <span className="eyebrow">CURRENT STATUS</span>
        <h2>Optimization is pending.</h2>
        <p>
          The scenario has been successfully sent to the backend.
          Detailed vessel, fuel, speed, fuel consumption, cost and emission
          results will appear here once the optimizer is connected.
        </p>

        <button className="primary" onClick={() => navigate("/optimize")}>
          Create Another Scenario
        </button>
      </section>
    </>
  );
}
