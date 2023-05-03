import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import axios from "axios";
import { Link } from "react-router-dom";
import CreditCard from "./CreditCard";
import { CustomerOnlyButton } from "../auth";
import "../css/profile.css";

export default function Profile() {
	const navigate = useNavigate();
	const [user, setUser] = useState("");

	useEffect(() => {
		axios.get("http://localhost:8000/users/me").then((response) => {
			console.log(response);
			setUser(response.data);
		});
	}, []);

	const signOut = () => {
		localStorage.removeItem("access_token");
		localStorage.removeItem("role");
		navigate("/");
		window.location.reload(false);
	};

	return (
		<>
			<div class = 'profile'>
				<h1>Profile page</h1>
				<p>Hello there, welcome to your profile page</p>
				<button onClick={signOut}>sign out</button>
				<ul>{user.full_name}</ul>
				<ul>{user.email}</ul>
				<ul>{user.gender}</ul>
				<ul>{user.tel}</ul>
				<ul>{user.address}</ul>
				{CustomerOnlyButton() && (
					<Link to="/editprofile" className="btn btn-primary">
						Edit
					</Link>
				)}
			</div>
			{CustomerOnlyButton() && (
				<div class = 'profile'>
					<CreditCard />
				</div>
			)}
		</>
	);
}
