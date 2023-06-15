"use client"
import { useState, FormEvent } from 'react';

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [repassword, setRePassword] = useState('');
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
    if (!repassword) {
      validationErrors.repassword = 'Retype Password is required';
    }
    setErrors(validationErrors);

    // If there are no validation errors, proceed with login logic
    if (Object.keys(validationErrors).length === 0) {
      try {
        const response = await fetch('http://localhost:8000/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          credentials: 'include',
          body: JSON.stringify({ username, password }),
        });

        if (response.ok) {
          window.location.href = '/'
        } else {
          alert('register failed');
        }
      } catch (error) {
        console.log(error)
      }
    }
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <div className="w-80vw">
        <div className="container mx-auto py-10">
          <h1 className="text-2xl font-bold mb-4">Register Page</h1>
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="username" className="block font-semibold mb-1">Username:</label>
              <input
                type="text"
                id="username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded"
                pattern="[a-z0-9]{2,6}"
                title="Login should be digits (0 to 9) or alphabets (a to z) length: 2-16 ."
              />
              {errors.username && <span className="text-red-500">{errors.username}</span>}
            </div>
            <div className="mb-4">
              <label htmlFor="password" className="block font-semibold mb-1">Password:</label>
              <input
                type="password"
                id="password"
                value={password}
                minLength={4}
                maxLength={64}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded"
                pattern="^[\x20-\x7E]*$"
                title="Password should contain only printable characters."
              />
              {errors.password && <span className="text-red-500">{errors.password}</span>}
            </div>
            <div className="mb-4">
              <label htmlFor="repassword" className="block font-semibold mb-1">Retype password:</label>
              <input
                type="password"
                id="repassword"
                value={repassword}
                minLength={4}
                maxLength={64}
                onChange={(e) => setRePassword(e.target.value)}
                className="w-full px-4 py-2 border border-gray-300 rounded"
                pattern="^[\x20-\x7E]*$"
                title="Password should contain only printable characters."
              />
              {errors.repassword && <span className="text-red-500">{errors.repassword}</span>}
            </div>
            <button type="submit" className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded">
              Register
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
