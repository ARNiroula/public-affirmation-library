"use client"; // Marks this as a Client Component

import React from "react";

const HomePage = () => {
  return (
    <div
      style={{
        fontFamily: "Arial, sans-serif",
        textAlign: "center",
        padding: "20px",
      }}
    >
      <header
        style={{
          backgroundColor: "#f8f9fa",
          padding: "10px 0",
          marginBottom: "20px",
        }}
      >
        <h1>Welcome to Public Affirmation Library</h1>
      </header>

      <main>
        <p>This is a basic homepage for the project. Start exploring!</p>
        <button
          onClick={() => alert("Get Started!")}
          style={{
            backgroundColor: "#007bff",
            color: "#fff",
            border: "none",
            padding: "10px 20px",
            borderRadius: "5px",
            cursor: "pointer",
          }}
        >
          Get Started
        </button>
      </main>

      <footer
        style={{
          marginTop: "20px",
          fontSize: "14px",
          color: "#6c757d",
        }}
      >
        <p>© 2025 Public Affirmation Library. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;