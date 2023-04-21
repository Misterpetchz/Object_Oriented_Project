import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter, NavLink, Route, Routes, Navigate} from 'react-router-dom'
import { RequireToken } from './auth'
import axios from 'axios';

// Pages
import Home from './pages/Home'
import Error from './pages/error'
import BookEdit from './pages/Book'
import Branches from './pages/branch'
import Login from './pages/login'
import Profile from './pages/Profile'
import Event from './pages/Event'
import Register from './pages/Register'
import Basket from './pages/Basket'
import Payment from './pages/Payment'

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

  let activeClassName = "nav-active"

  return (
    <BrowserRouter>
      <nav>
        <NavLink to="/" className={({ isActive }) => isActive ? activeClassName : undefined}>Home</NavLink><br />
        <NavLink to="/login" className={({ isActive }) => isActive ? activeClassName : undefined}>Login</NavLink><br />
        <NavLink to="/profile" className={({ isActive }) => isActive ? activeClassName : undefined}>Profile</NavLink><br />
        <NavLink to='/book' className={({ isActive }) => isActive ? activeClassName : undefined}>Book</NavLink><br />
        <NavLink to="/branches" className={({ isActive }) => isActive ? activeClassName : undefined}>Branches</NavLink><br />
        <NavLink to="/event" className={({ isActive }) => isActive ? activeClassName : undefined}>Event</NavLink> <br />
        <NavLink to="/basket" className={({ isActive }) => isActive ? activeClassName : undefined}>Basket</NavLink>
      </nav>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/book' element={<BookEdit />} />
        {/* <Route path='/books/:bookname' element = {<Book/>}/> */}
        <Route path='/branches' element={<Branches />} />
        <Route path='*' element={<Error />} />
        <Route path='/login' element = {<Login/>}/>
        <Route path='/profile' element={<RequireToken>
                                          <Profile />
                                        </RequireToken>}                        
        />
        <Route path='/event' element={<Event/>}/>
        <Route path='/basket' element={<Basket />}/>
        <Route path='/payment/:id/' element={<Payment/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
