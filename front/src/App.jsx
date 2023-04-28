import { useState } from 'react'
import './App.css';
import './css/home.css';
import './css/navbar.css';
import { BrowserRouter, NavLink } from 'react-router-dom';
import { Routes, Route } from "react-router-dom";
import Login from './pages/Login';
import Profile from './pages/Profile';
import Register from './pages/Register';
import Catalog from './pages/Home';
import Searchs from './pages/Search';
import Admin from './pages/Admin';
import Basket from './pages/Basket';
import { RequireRole, RequireToken, NotRequireTokenButton, RequireTokenButton, RequireRoleButton} from './auth';
import axios from 'axios';
import Book from './pages/Book';
import EditProfile from './pages/EditProfile';
import CreditCard from './pages/CreditCard';
import EditCreditCard from './pages/EditCreditCard';
import SearchBranch from './pages/SearchBranch';
import Payment from './pages/Payment'
import OrderList from './pages/OrderList'
import Event from './pages/Event'
import Branches from './pages/branch'
import Error from './pages/error'
import ViewBranch from './pages/ViewBranch'

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

  return (
    <BrowserRouter>
      <nav class='navbar'>
        <NavLink to="/">Home</NavLink>
        {NotRequireTokenButton() && <NavLink to="/login">Login</NavLink>}
        {RequireTokenButton() && <NavLink to="/profile">Profile</NavLink>}
        <NavLink to="/search">Search</NavLink>
        <NavLink to="/branches/search">Search_B</NavLink>
        <NavLink to="/branches">Branches</NavLink>
        <NavLink to="/event">Event</NavLink>
        <NavLink to="/register">Register</NavLink>
        {RequireRoleButton() && <NavLink to="/admin">Admin</NavLink>}
        <NavLink to="/basket">Basket</NavLink>
        <NavLink to="/profile/credit_card">CreditCard</NavLink>
        <NavLink to="/profile/credit_card/edit">EditCreditCard</NavLink>
      </nav>
      <Routes>
        <Route path='/' element = {<Catalog/>}/>
        <Route path='/login' element = {<Login/>}/>
        <Route path='/profile' element={<RequireToken>
                                          <Profile />
                                        </RequireToken>}
        />
        <Route path='/search' element={<Searchs/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/admin' element={<RequireRole>
                                      <Admin/>
                                      </RequireRole>} /> 
		    <Route path='/branches' element={<Branches />} />
		    <Route path='*' element={<Error />} />
		    <Route path='/branches/search' element={<SearchBranch/>}/>
		    <Route path='/event' element={<Event/>}/>
        <Route path='/profile/credit_card' element={<CreditCard/>}/>
        <Route path='/profile/credit_card/edit' element={<EditCreditCard/>}/>
        <Route path='/books/:bookname' element = {<Book/>}/>
        <Route path='/basket' element = {<RequireToken>
                                          <Basket />
                                        </RequireToken>}/>
        <Route path='/editprofile' element = {<EditProfile/>}/>
		    <Route path='/payment/:id' element={<Payment/>} />
        <Route path='/order_list' element={<OrderList/>} />
        <Route path='/branch/:name' element={<ViewBranch/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
