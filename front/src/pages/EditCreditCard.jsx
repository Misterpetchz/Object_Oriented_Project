import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import axios from "axios";
import { Link } from "react-router-dom";

export default function EditCreditCard() {
	const navigate = useNavigate();
	const [num, setNum] = useState("");
	const [exp, setEXP] = useState("");
	const [cvc, setCVC] = useState("");

	const editcard = () => {
		if ((num == "") && (exp == "") && (cvc == ""))
			{ return; }
		else
		{
			axios
				.put("http://localhost:8000/Creditcard/edit", {
					card_num : num, expire_date : exp, cvc : cvc
				})
				.then((response) => {
					if (response.data.status == "Success") {
						navigate("/profile/credit_card")
					}
					else if (response.data.status == "Error") {
						console.log(error, "Wrong format of card info")
					}
				})
				.catch(function (error) {
					console.log(error, "error");
				});
		}
	};
	return (
		<div style={{ minHeight: 800, marginTop: 30 }}>
		<h1>Edit page</h1>
			<div>
				<form>
					<div>
					<label style={{ marginRight: 10 }}>Card Number</label>
					<input
					type="text"
					onChange={(e) => setNum(e.target.value)}
				/>
					</div>
					<div>
					<label style={{ marginRight: 10 }}>Expire Date</label>
					<input
					type="text"
					onChange={(e) => setEXP(e.target.value)}
				/>
					</div>
					<div>
					<label style={{ marginRight: 10 }}>CVC</label>
					<input
					type="text"
					onChange={(e) => setCVC(e.target.value)}
				/>
					</div>
				<button type="button" onClick={editcard}>
					Edit
				</button>
				</form>
			</div>
		</div>
	);
}
