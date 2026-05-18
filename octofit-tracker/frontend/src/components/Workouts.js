import React, { useEffect } from 'react';

function Workouts() {

  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

    console.log("Workouts API:", endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Workouts</h2>
    </div>
  );
}

export default Workouts;