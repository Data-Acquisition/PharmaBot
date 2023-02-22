import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom"
import { LandingPage } from './pages/LandingPage'

export const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' exact component={LandingPage}/>
      </Routes>
    </BrowserRouter>
  )
}
