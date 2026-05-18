import React, { useEffect } from 'react';

function Users() {

  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

    console.log("Users API:", endpoint);

    fetch(endpoint)
      .then(res => res.json())
      .then(data => console.log(data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div>
      <h2>Users</h2>
    </div>
  );
}

export default Users;