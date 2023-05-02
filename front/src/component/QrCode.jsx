import React from "react";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function QrCode() {
	const { id } = useParams();
	const [qr, setQr] = useState("");

	useEffect(() => {
		axios
			.get(`http://localhost:8000/payment/${id}?payment_type=qrcode`)
			.then((response) => {
				setQr(response.data);
				// console.log(response.data);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	}, [id]);

	return (
		<div>
			<img src={`data:image/png;base64,${qr.payment}`} alt="Qr Code" />
		</div>
	);
}
