import { useState } from 'react'
import './App.css'
import { BrowserRouter, NavLink } from 'react-router-dom'
import { Routes, Route } from "react-router-dom";
import Login from './pages/Login'
import Profile from './pages/Profile'
import Register from './pages/Register';
import Home from './pages/Home'
import Searchs from './pages/Search'
import Admin from './pages/Admin';
import { RequireToken } from './auth'
import axios from 'axios';

axios.interceptors.request.use(
  config => {
    config.headers['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`;
        return config;
    },
    error => {
        return Promise.reject(error);
    }
);

function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <h1>BookShop</h1>
      <nav>
        <NavLink to="/">Home</NavLink>
        <NavLink to="/login">Login</NavLink>
        <NavLink to="/profile">Profile</NavLink>
        <NavLink to="/contact">Contact</NavLink>
        <NavLink to="/cart">Cart</NavLink>
        <NavLink to="/search">Search</NavLink>
        <NavLink to="/register">Register</NavLink>
        <NavLink to="/admin">Admin</NavLink>
        </nav>
      <Routes>
        <Route path='/' element = {<Home/>}/>
        <Route path='/login' element = {<Login/>}/>
        <Route path='/profile' element={<RequireToken>
                                          <Profile />
                                        </RequireToken>}                        
        />
        <Route path='/search' element={<Searchs/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/admin' element={<Admin/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
