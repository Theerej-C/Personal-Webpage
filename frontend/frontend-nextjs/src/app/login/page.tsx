import React, { Fragment } from "react";
import Link from "next/link";
import dynamic from "next/dynamic";
import Header from "@/components/Header";

const LoginForm = dynamic(() => import("../../components/LoginForm"), {
  ssr: false,
});

const LoginPage = () => {
  return (
    <Fragment>
      <Header></Header>
      <div className="flex flex-col items-center justify-center h-screen">
        <div className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
          <h1 className="text-3xl font-bold mb-4">Login</h1>
          <LoginForm />
          <p className="text-gray-700 text-sm">
            Don&apos;t have an account? <Link href="/register">Register</Link>
          </p>
        </div>
      </div>
    </Fragment>
  );
};

export default LoginPage;
