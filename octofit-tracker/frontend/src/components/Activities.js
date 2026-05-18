import React, { useEffect } from 'react';

function Activities() {

  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

    console.log("Activities API:", endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Activities</h2>
    </div>
  );
}

export default Activities;