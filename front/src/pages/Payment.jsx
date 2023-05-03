import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

import SelectMethod from "../component/SelectMethodPayment";

export default function Payment() {
	const Navigate = useNavigate();
	const { id } = useParams();
	const [order, setOrder] = useState("");
	const [delay, setDelay] = useState(false);

	useEffect(() => {
		axios
			.get(`http://localhost:8000/payment/${id}`)
			.then((response) => {
				setOrder(response.data);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
		axios.get(`http://localhost:8000/payment_status/${id}`).then((response) => {
			if (response.data.status === "paid") {
				Navigate(`/order_list`);
			}
		});
		const timeoutId = setTimeout(() => {
			setDelay(!delay);
		}, 1000);

		return () => clearTimeout(timeoutId);
	}, [delay]);

	const cancel_order = () => {
		axios
			.delete(`http://localhost:8000/cancel_order`)
			.then(() => {
				Navigate('/')
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	};

	return (
		<div>
			<h2>Order</h2>
			{order&&order.order.map((item) => (
					<div>
						<p>Name : {item.name}</p>
						<p>Price : {item.price}</p>
						<p>Amount : {item.amount}</p>
					</div>
				))}
			<div>
				<p>Total : {order.total}</p>
			</div>
			<div>
				<SelectMethod />
			</div>
			<div>
				<button onClick={cancel_order}>
					Cancel Order
				</button>
			</div>
		</div>
	);
}
