import { useState } from 'react'
import './App.css';
import './css/home.css';
import { BrowserRouter, NavLink } from 'react-router-dom';
import { Routes, Route } from "react-router-dom";
import Login from './pages/Login';
import Profile from './pages/Profile';
import Register from './pages/Register';
import Catalog from './pages/Home';
import Searchs from './pages/Search';
import Admin from './pages/Admin';
import Basket from './pages/Basket';
import { RequireToken } from './auth'
import axios from 'axios';
import Book from './pages/Book';
import EditProfile from './pages/EditProfile';
import CreditCard from './pages/CreditCard';
import EditCreditCard from './pages/EditCreditCard';
import SearchBranch from './pages/SearchBranch';

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
      <h1 class="web_title">BookShop</h1>
      <nav>
        <div class="menu_tab"><NavLink to="/">Home</NavLink></div>
        <div class="menu_tab"><NavLink to="/login">Login</NavLink></div>
        <div class="menu_tab"><NavLink to="/profile">Profile</NavLink></div>
        <div class="menu_tab"><NavLink to="/contact">Contact</NavLink></div>
        <div class="menu_tab"><NavLink to="/search">Search</NavLink></div>
		    <div class="menu_tab"><NavLink to="/branch/search">Search_B</NavLink></div>
        <div class="menu_tab"><NavLink to="/register">Register</NavLink></div>
        <div class="menu_tab"><NavLink to="/admin">Admin</NavLink></div>
        <div class="menu_tab"><NavLink to="/basket">Basket</NavLink></div>
        <div class="menu_tab"><NavLink to="/profile/credit_card">CreditCard</NavLink></div>
        <div class="menu_tab"><NavLink to="/profile/credit_card/edit">EditCreditCard</NavLink></div>
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
        <Route path='/admin' element={<Admin/>}/>
		<Route path='/branch/search' element={<SearchBranch/>}/>
        <Route path='/profile/credit_card' element={<CreditCard/>}/>
        <Route path='/profile/credit_card/edit' element={<EditCreditCard/>}/>
        <Route path='/books/:bookname' element = {<Book/>}/>
        <Route path='/basket' element = {<RequireToken>
                                          <Basket />
                                        </RequireToken>}/>
        <Route path='/editprofile' element = {<EditProfile/>}/>
      </Routes>
    </BrowserRouter>
  )
}

export default App
