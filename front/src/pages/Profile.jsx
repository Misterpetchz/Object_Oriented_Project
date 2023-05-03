import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import axios from "axios";
import { Link } from "react-router-dom";
import CreditCard from "./CreditCard";
import { CustomerOnlyButton } from "../auth";
import "../css/profile.css";

export const fetchPayment = () => {
	return localStorage.getItem("payment_local_id");
};

export default function Profile() {
	const navigate = useNavigate();
	const [user, setUser] = useState("");
	const [bookname, setBookName] = useState("");


	useEffect(() => {
		axios.get("http://localhost:8000/users/me").then((response) => {
			console.log(response);
			setUser(response.data);
		});
	}, []);

	const signOut = () => {
		axios
			.delete(`http://localhost:8000/clear_item/`)
			.then((result) => {
				clear_basket();
			});
		
	};

	const clear_basket = () => {
		localStorage.removeItem("access_token");
		localStorage.removeItem("role");
		navigate("/");
		window.location.reload(false);

	};

	const go_to_order = () =>{
		if (fetchPayment() != null){
			navigate(`/payment/${fetchPayment()}`)
		}
	}

	return (
		<>
			<div class = 'profile'>
				<h1>Profile page</h1>
				<p>Hello there, welcome to your profile page</p>
				<button onClick={signOut}>sign out</button><br/><br/>
				<span>Full name : {user.full_name}</span><br/><br/>
				<span>Email : {user.email}</span><br/><br/>
				<span>Gender : {user.gender}</span><br/><br/>
				<span>Tel : {user.tel}</span><br/><br/>
				<span>Address : {user.address}</span><br/><br/>
				{CustomerOnlyButton() && (
					<Link to="/editprofile" className="btn btn-primary">
						Edit
					</Link>
				)}
				<div><button onClick={go_to_order}>Order</button></div>
				
			</div>
			{CustomerOnlyButton() && (
				<div class = 'profile'>
					<CreditCard />
				</div>
			)}
		</>
	);
}
