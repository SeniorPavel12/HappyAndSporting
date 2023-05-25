import React from "react"
import { BrowserRouter, Route, Routes } from "react-router-dom"

import { App } from "../../views/App"
import { Music } from "../../views/music/Music"
import { Options } from "../../views/settings/Settings.jsx"


export const Router = () => {
  return <BrowserRouter>
    <Routes>
      <Route element={<App />} path='/' />
      <Route element={<Music />} path='/music' />
      <Route element={<Options />} path='/options' />
      <Route element={<h1>Page not found</h1>} path='*' />
    </Routes>
  </BrowserRouter>
}