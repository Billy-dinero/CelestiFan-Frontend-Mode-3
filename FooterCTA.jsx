import React from "react";

export default function FooterCTA() {
  return (
    <footer className="text-center py-20 px-6 bg-[#3A0CA3]">
      <h3 className="text-2xl font-bold mb-2">📬 Join the waitlist now</h3>
      <p className="text-lg max-w-xl mx-auto mb-6">
        Be first to access the experience. Be seen. Be part of the story. Welcome to CelestiFan — Your fanhood. Finally valued.
      </p>
      <button className="bg-[#FF007F] text-white px-6 py-3 rounded-full text-lg hover:bg-pink-500 transition">
        Join Now
      </button>
    </footer>
  );
}