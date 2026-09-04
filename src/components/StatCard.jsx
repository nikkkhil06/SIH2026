export default function StatCard({ title, value, description }) {
  return (
    <div className="card stat">
      <span>{title}</span>
      <strong>{value}</strong>
      <small>{description}</small>
    </div>
  );
}
