import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import axios from "axios";


export default function Profile() {
  const navigate = useNavigate();
  const[user, setUser] = useState('');

  useEffect(() => {
    axios.get("http://localhost:8000/users/me")
    .then((response) => {console.log(response)
    setUser(response.data)})
  },[])

  const signOut = () => {
    localStorage.removeItem("access_token");
    navigate("/");
  };

  return (
    <>
      <div style={{ marginTop: 20, minHeight: 700 }}>
        <h1>Profile page</h1>
        <p>Hello there, welcome to your profile page</p>

        <button onClick={signOut}>sign out</button>
        <ul>
          {user.full_name}
        </ul>
        <ul>
          {user.email}
        </ul>
        <ul>
          {user.gender}
        </ul>
        <ul>
          {user.tel}
        </ul>
        <ul>
          {user.address}
        </ul>
      </div>
    </>
  );
}