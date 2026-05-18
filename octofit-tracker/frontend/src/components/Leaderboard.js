import React, { useEffect } from 'react';

function Leaderboard() {

  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

    console.log("Leaderboard API:", endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Leaderboard</h2>
    </div>
  );
}

export default Leaderboard;