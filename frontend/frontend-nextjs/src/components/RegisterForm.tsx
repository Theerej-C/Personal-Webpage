"use client";
import { useRouter } from 'next/navigation';
import React, { useState, useEffect, Fragment } from 'react';

interface RegisterFormProps {
  // Add any props you want to pass to the component
}

const RegisterForm: React.FC<RegisterFormProps> = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [phone_number, setPhoneNumber] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const router = useRouter()
  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    // Validate the form data
    if (!email || !username || !phone_number || !password || !confirmPassword) {
      setError('Please fill out all fields');
      return;
    }

    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    if (password.length < 8) {
      setError('Password must be at least 8 characters long');
      return;
    }

    // Send the data to the server (replace with your own API endpoint)
    try {
      const response = await fetch('http://localhost:8000/user/registration/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email,
          username,
          phone_number,
          password,
        }),
      });
      if (response.ok) {
        const data = await response.json();
        console.log(data['Token']);
        localStorage.setItem('user_token',data['Token']);
        router.push('/dashboard');
      }
      else if (response.status === 400) {
        const data = await response.json();
        setError(`Registration failed: ${data['username']}`);
        alert(error)
      }
    } catch (error) {
      setError('Registration Failed due to ' + error)
      alert(error)
    }
    // console.log(error);
    // setEmail('')
    // setUsername('')
    // setPhoneNumber('')
    // setPassword('')
    // setConfirmPassword('') 
  };

  return (
    <Fragment>
    <form onSubmit={handleSubmit} className="mb-4">
      <label className="block mb-2 text-gray-700 font-bold">
        Email:
        <input
          type="email"
          value={email}
          onChange={(event) => setEmail(event.target.value)}
          className="appearance-none border rounded w-full py-2 px-3 leading-tight"
        />
      </label>
      <br />
      <label className="block mb-2 text-gray-700 font-bold">
        Username:
        <input
          type="text"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
          className="appearance-none border rounded w-full py-2 px-3 leading-tight"
        />
      </label>
      <br />
      <label className="block mb-2 text-gray-700 font-bold">
        Phone Number:
        <input
          type="tel"
          value={phone_number}
          onChange={(event) => setPhoneNumber(event.target.value)}
          className="appearance-none border rounded w-full py-2 px-3 leading-tight"
        />
      </label>
      <br />
      <label className="block mb-2 text-gray-700 font-bold">
        Password:
        <input
          type="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          className="appearance-none border rounded w-full py-2 px-3 leading-tight"
        />
      </label>
      <br />
      <label className="block mb-2 text-gray-700 font-bold">
        Confirm Password:
        <input
          type="password"
          value={confirmPassword}
          onChange={(event) => setConfirmPassword(event.target.value)}
          className="appearance-none border rounded w-full py-2 px-3 leading-tight"
        />
      </label>
      <br />
      <button
        type="submit"
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Register
      </button>
    </form>
</Fragment>
  );
};

export default RegisterForm;