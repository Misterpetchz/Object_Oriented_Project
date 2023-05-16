import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import axios from "axios";
import { Link } from "react-router-dom";
import CreditCard from "./CreditCard";
import { CustomerOnlyButton } from "../auth";
import { fetchPayment } from "../auth";

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
		localStorage.removeItem("payment");
		navigate("/");
		window.location.reload(false);
	};

	const go_to_order = () => {
		console.log(fetchPayment())
		if(fetchPayment() != null){
		navigate(`/payment/${fetchPayment()}`);}
	};

	const go_to_order_list = () => {
		navigate(`/order_list`)
	}

	return (
		<>
			<div style={{ marginTop: 20, minHeight: 700 }}>
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
				<div>
					<button onClick={go_to_order}>
						Order
					</button>
				</div>
				<div>
					<button onClick={go_to_order_list}>
						Order List
					</button>
				</div>
			</div>
			{CustomerOnlyButton() && (
				<div>
					<CreditCard />
				</div>
				
			)}
		</>
	);
}
