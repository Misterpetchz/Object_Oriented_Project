import { useState } from 'react'
import './App.css'
import { BrowserRouter, NavLink } from 'react-router-dom'
import { Routes, Route } from "react-router-dom";
import Login from './pages/Login'
import Profile from './pages/Profile'
import Home from './pages/Home'
import Searchs from './pages/Search'
import { RequireToken } from './auth'

function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <h1>BookShop</h1>
      <nav>
        <NavLink to="/home">Home</NavLink>
        <NavLink to="/login">Login</NavLink>
        <NavLink to="/profile">Profile</NavLink>
        <NavLink to="/contact">Contact</NavLink>
        <NavLink to="/cart">Cart</NavLink>
        <NavLink to="/search">Search</NavLink>
      </nav>
      <Routes>
        <Route path='/' element = {<Home/>}/>
        <Route path='/login' element = {<Login/>}/>
        <Route path='/profile' element={<RequireToken>
                                          <Profile />
                                        </RequireToken>}                        
        />
        <Route path='search' element={<Searchs/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
