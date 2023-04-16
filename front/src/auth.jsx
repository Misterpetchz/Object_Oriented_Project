import { useLocation,Navigate } from "react-router-dom"


export const setToken = (token)=>{
    localStorage.setItem('access_token', token)// make up your own token
}

export const fetchToken = ()=>{
    return localStorage.getItem('access_token')
}

export function RequireToken({children}){

    let auth = fetchToken()
    let location = useLocation()

    if(!auth){

        return <Navigate to='/' state ={{from : location}}/>;
    }

    return children;
}