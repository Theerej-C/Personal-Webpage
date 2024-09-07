// pages/RegisterPage.tsx
import React from 'react';
import RegisterForm from '@/components/RegisterForm';

interface RegisterPageProps {
  // Add props here if needed
}

const RegisterPage: React.FC<RegisterPageProps> = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <h1>Register Page</h1>
      <RegisterForm />
    </div>
    </div>
  );
};

export default RegisterPage;