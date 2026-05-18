import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="container mt-4">
        <h1 className="mb-4">OctoFit Tracker</h1>

        <nav className="nav mb-4">
          <Link className="nav-link" to="/">Activities</Link>
          <Link className="nav-link" to="/users">Users</Link>
          <Link className="nav-link" to="/teams">Teams</Link>
          <Link className="nav-link" to="/workouts">Workouts</Link>
          <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
        </nav>

        <Routes>
          <Route path="/" element={<Activities />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;