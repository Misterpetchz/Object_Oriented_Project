import React, { useState, useEffect} from 'react'
import { Link } from 'react-router-dom'
import { useLocation,  Route, Routes} from 'react-router-dom'
import axios from 'axios'
import AddBranchForm from './addBranch'
import ModifyBranchForm from './modifyBranch'
import RemoveBranch from './removeBranch'


function Branches(){

    const [allBranch, setAllBranch] = useState([])    

    useEffect(() =>{
        axios.get('http://localhost:8000/GetAllBranch/')
        .then(response => {
            setAllBranch(response.data)
        })
    },[])
        
    
    return (
        <div>
            <div>
            {allBranch && allBranch.name && allBranch.name.map((branch)=> (
                <p>{branch.branch_name}</p>
            ))}
            </div>
            <div>
                <h2>Add Branch</h2>
                <AddBranchForm />
            </div>
            <div>
                <h2>Modify Branch</h2>
                <ModifyBranchForm />
            </div>
            <div>
                <h2>Remove Branch</h2>
                <RemoveBranch />
            </div>
        </div>
    )
}

export default Branches

