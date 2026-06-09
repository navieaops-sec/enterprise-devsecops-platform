import { useEffect, useState } from "react";

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/users")
      .then((response) => response.json())
      .then((data) => setUsers(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Enterprise DevSecOps Platform</h1>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
          </tr>
        </thead>

        <tbody>
          {users.map((user) => (
            <tr key={user[0]}>
              <td>{user[0]}</td>
              <td>{user[1]}</td>
              <td>{user[2]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;