"use client"
import Header from "@/components/Header";
import { Fragment, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";

export default function Page() {
  const [token, setToken] = useState<string|null>(null);
  useEffect(()=>{
    const token = localStorage.getItem('user_token');
    if(token) setToken(token);
  },[])

  if(!token){
    return (
      <>
      No Login
      </>
    )
  }
  return (
    
    <Fragment>
      <h1>Dashboard</h1>
    </Fragment>
  )
}
