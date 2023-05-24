"use client"
import { useState, FormEvent } from 'react';

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState<{ [key: string]: string }>({});

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // Validate the form
    const validationErrors: { [key: string]: string } = {};
    if (!username) {
      validationErrors.username = 'Username is required';
    }
    if (!password) {
      validationErrors.password = 'Password is required';
    }
    setErrors(validationErrors);

    // If there are no validation errors, proceed with login logic
    if (Object.keys(validationErrors).length === 0) {
      try {
        const response = await fetch('http://localhost:8000/login/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'credentials':'include'
          },
          body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
          // Login successful, handle the response
        } else {
          // Login failed, handle the error
        }
      } catch (error) {
        console.log(error)
      }
    }
  };

  return (
    <div className="container">
      <h1>Login Page</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          {errors.username && <span className="error">{errors.username}</span>}
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          {errors.password && <span className="error">{errors.password}</span>}
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginPage;
