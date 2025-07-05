import React from "react";
import HeroSection from "./components/HeroSection";
import FanLeaderboard from "./components/FanLeaderboard";
import ArtistRanking from "./components/ArtistRanking";
import ExclusiveContent from "./components/ExclusiveContent";
import WhyCelestiFan from "./components/WhyCelestiFan";
import FooterCTA from "./components/FooterCTA";

export default function App() {
  return (
    <div className="bg-gradient-to-br from-[#1A1A40] to-[#3A0CA3] text-white font-sans">
      <HeroSection />
      <FanLeaderboard />
      <ArtistRanking />
      <ExclusiveContent />
      <WhyCelestiFan />
      <FooterCTA />
    </div>
  );
}