import React, { useEffect, useState } from "react";

export default function FanLeaderboard() {
  const [fans, setFans] = useState([]);

  useEffect(() => {
    fetch("https://api.celestifan.com/fans/top")
      .then(res => res.json())
      .then(data => setFans(data));
  }, []);

  return (
    <section className="text-center py-20 px-6 bg-[#2E2E6A]">
      <h2 className="text-3xl font-bold mb-4">Fan Leaderboard</h2>
      <p className="text-lg max-w-xl mx-auto mb-6">
        Climb the ranks. Be more than just a listener. Every stream, share, and reaction earns you a spot. Top fans get noticed, respected, and rewarded.
      </p>
      <ul className="max-w-xl mx-auto">
        {fans.map((fan, index) => (
          <li key={index} className="border-b border-white/10 py-2">
            #{index + 1} - {fan.username} ({fan.points} pts)
          </li>
        ))}
      </ul>
    </section>
  );
}