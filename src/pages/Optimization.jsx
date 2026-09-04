import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Optimization() {
  const navigate = useNavigate();

  const [form, setForm] = useState({
    cargo_demand: "",
    distance: "",
    max_time: "",
    objective: "balanced"
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  function handleChange(e) {
    const { name, value } = e.target;
    setForm({
      ...form,
      [name]: value
    });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");

    if (
      form.cargo_demand === "" ||
      form.distance === "" ||
      form.max_time === ""
    ) {
      setError("Please fill all voyage requirements.");
      return;
    }

    const requestData = {
      cargo_demand: Number(form.cargo_demand),
      distance: Number(form.distance),
      max_time: Number(form.max_time),
      objective: form.objective
    };

    try {
      setLoading(true);

      const response = await fetch(
        "http://127.0.0.1:8000/optimization/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(requestData)
        }
      );

      if (!response.ok) {
        throw new Error("Optimization request failed.");
      }

      const data = await response.json();

      navigate("/results", {
        state: {
          scenario_id: data.scenario_id,
          status: data.status,
          message: data.message,
          input: requestData
        }
      });
    } catch (err) {
      console.log(err);
      setError(
        "Unable to connect to the optimization server. Please make sure the backend is running."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <section className="heading">
        <span className="eyebrow">OPTIMIZATION SCENARIO</span>
        <h1>Create a fleet optimization scenario.</h1>
        <p>
          Enter the voyage requirements. The optimization engine
          will determine the suitable vessel and fuel combination.
        </p>
      </section>

      <form onSubmit={handleSubmit}>
        <section className="card">
          <h2>Voyage requirements</h2>
          <p className="section-description">
            These values define the operational requirements for the optimization problem.
          </p>

          <div className="formgrid">
            <label>
              Cargo Demand
              <span className="unit">tonnes</span>
              <input
                type="number"
                name="cargo_demand"
                value={form.cargo_demand}
                onChange={handleChange}
                placeholder="15000"
                min="0"
              />
            </label>

            <label>
              Distance
              <span className="unit">nautical miles</span>
              <input
                type="number"
                name="distance"
                value={form.distance}
                onChange={handleChange}
                placeholder="800"
                min="0"
              />
            </label>

            <label>
              Maximum Time
              <span className="unit">hours</span>
              <input
                type="number"
                name="max_time"
                value={form.max_time}
                onChange={handleChange}
                placeholder="36"
                min="0"
              />
            </label>
          </div>
        </section>

        <section className="card">
          <h2>Optimization objective</h2>
          <p className="section-description">
            Select what the optimizer should prioritize.
          </p>

          <div className="objective-grid">
            <label className="objective-card">
              <input type="radio" name="objective" value="fuel"
                checked={form.objective === "fuel"} onChange={handleChange} />
              <div><b>Fuel</b><small>Minimize fuel consumption</small></div>
            </label>

            <label className="objective-card">
              <input type="radio" name="objective" value="cost"
                checked={form.objective === "cost"} onChange={handleChange} />
              <div><b>Cost</b><small>Minimize operational cost</small></div>
            </label>

            <label className="objective-card">
              <input type="radio" name="objective" value="emissions"
                checked={form.objective === "emissions"} onChange={handleChange} />
              <div><b>Emissions</b><small>Minimize environmental impact</small></div>
            </label>

            <label className="objective-card">
              <input type="radio" name="objective" value="balanced"
                checked={form.objective === "balanced"} onChange={handleChange} />
              <div><b>Balanced</b><small>Balance fuel, cost and emissions</small></div>
            </label>
          </div>
        </section>

        <section className="constraint">
          <b>Optimizer-controlled decisions</b>
          <small>
            Vessel selection, fuel type and operating conditions will be
            determined automatically using fleet database information and the optimization engine.
          </small>
        </section>

        {error && <div className="error-box">{error}</div>}

        <button type="submit" className="primary full" disabled={loading}>
          {loading ? "Creating optimization scenario..." : "Optimize Fleet →"}
        </button>

        <p className="form-note">
          The scenario will be sent to the backend optimization service.
        </p>
      </form>
    </>
  );
}
