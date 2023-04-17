import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter, NavLink, Route, Routes, Navigate} from 'react-router-dom'

// Pages
import Home from './pages/Home'
import Error from './pages/error'
import Branches from './pages/branch'

function App() {
  const [count, setCount] = useState(0)

  let activeClassName = "nav-active"

  return (
    <BrowserRouter>
      <nav>
        <NavLink to="/" className={({ isActive }) => isActive ? activeClassName : undefined}>Home</NavLink><br />
        <NavLink to="/branches" className={({ isActive }) => isActive ? activeClassName : undefined}>Branches</NavLink><br />
        {/* <NavLink to='/branches/addBranch' className={({ isActive }) => isActive ? activeClassName : undefined}>Add Branch</NavLink> */}
      </nav>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/branches' element={<Branches />}>
        </Route>
        <Route path='*' element={<Error />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
