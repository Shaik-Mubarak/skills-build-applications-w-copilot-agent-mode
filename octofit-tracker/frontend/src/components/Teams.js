import React, { useEffect } from 'react';

function Teams() {

  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

    console.log("Teams API:", endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Teams</h2>
    </div>
  );
}

export default Teams;