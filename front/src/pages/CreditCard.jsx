import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import axios from "axios";
import { Link } from "react-router-dom";

export default function CreditCard() {
	const navigate = useNavigate();
	const [credit_card, setCreditCard] = useState("");

	useEffect(() => {
		axios.get("http://localhost:8000/CreditCard").then((response) => {
			console.log(response);
			setCreditCard(response.data);
		});
	}, []);

	if (credit_card.status === "Error") {
		return (
			<>
				<div style={{ marginTop: 20, minHeight: 700 }}>
					<h1>Credit Card Test</h1>
					<p>Testy, Test?</p>
					<Link to="/profile/credit_card/edit" className="btn btn-primary">
						Add Card
					</Link>
				</div>
			</>
		);
	} else {
		return (
			<>
				<div style={{ marginTop: 20, minHeight: 700 }}>
					<h1>Credit Card</h1>
					<span>Card number : {credit_card.credit_card_num}</span><br/><br/>
					<span>Expire date : {credit_card.credit_card_exp}</span><br/><br/>
					<span>CVC : {credit_card.credit_card_cvc}</span><br/><br/>
					<Link to="/profile/credit_card/edit" className="btn btn-primary">
						Edit Card
					</Link>
				</div>
			</>
		);
	}
}
