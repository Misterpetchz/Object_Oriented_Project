import React from "react";
import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";

export default function ViaCreditCard() {
	const Navigate = useNavigate();
	const { id } = useParams();
	const [creditCard, setCreditCard] = useState("");

	useEffect(() => {
		axios
			.get(`http://localhost:8000/payment/${id}?payment_type=creditcard`)
			.then((response) => {
				setCreditCard(response.data.payment);
				// if (!creditCard){
				//     redirect to page add credit credit card
				//     Navigate('path credit card')
				// }
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	}, [id]);

	return (
		<div>
			<p>Card Number : {creditCard.card_num}</p>
			<p>Expire Date : {creditCard.expire_date}</p>
		</div>
	);
}
