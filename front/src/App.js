import React, { useState, useEffect } from 'react';
import './App.css';
import {jwtDecode} from "jwt-decode"; // Importing jwtDecode correctly
import { useNavigate } from 'react-router-dom';

function App() {
  const navigate = useNavigate();
  const [name , setName] = useState('Student');
  const [authTokens, setAuthTokens] = useState(() =>
    localStorage.getItem("authTokens")
        ? JSON.parse(localStorage.getItem("authTokens"))
        : null
  );
  const [user, setUser] = useState(() => 
    localStorage.getItem("authTokens")
        ? jwtDecode(localStorage.getItem("authTokens"))
        : null
  );

  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    if (event) {
      event.preventDefault(); 
    }

    const loginData = {
      username: username,
      password: password,
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/api/token/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(loginData)
      });

      const data = await response.json();
      console.log(data);

      if (response.status === 200) {
        console.log("Logged In");
        setAuthTokens(data);
        setUser(jwtDecode(data.access));
        localStorage.setItem("authTokens", JSON.stringify(data));
        console.log('logged in successfully');
        navigate(`${name}/${username}`)
      
      } else {
        console.log(response.status);
        console.log("There was a server issue");
    
      }
    } catch (error) {
      console.error("An error occurred during login", error);
  
    }
  };

  useEffect(() => {
    if (authTokens) {
      setUser(jwtDecode(authTokens.access));
    }
  }, [authTokens]);

  const handleButtonClick = (buttonText) => {
    setName(buttonText);
  
  };









  return (
    <div className='login'>
    <div className='container '>
      <div className='row buttons' style={{marginBottom:'50px'}}>
      <button className=' text-white ' onClick={() => handleButtonClick('Student')} style={{ backgroundColor: name === 'Student' ? 'blue' : 'transparent' }}>
        <h2>Student</h2>
      </button> 
      <button className=' text-white ' onClick={() => handleButtonClick('Teacher')}   style={{ backgroundColor: name === 'Teacher' ? 'blue' : 'transparent' }}>
        <h2>Teacher</h2>
      </button>
      </div>
      <div className='row form'>
      <form onSubmit={handleSubmit}>
        <div>
          {<h4 className='text-white'>Dear {name} ,Please enter your assigned UserName and Password</h4>}
        </div>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">Login</button>
      </form>
      </div>
    </div>
    </div>
  );
}

export default App;
