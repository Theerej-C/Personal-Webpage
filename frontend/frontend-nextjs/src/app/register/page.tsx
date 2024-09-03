// pages/RegisterPage.tsx
import React from 'react';
import RegisterForm from '@/components/RegisterForm';

interface RegisterPageProps {
  // Add props here if needed
}

const RegisterPage: React.FC<RegisterPageProps> = () => {
  return (
    <div>
      <h1>Register Page</h1>
      <RegisterForm />
    </div>
  );
};

export default RegisterPage;