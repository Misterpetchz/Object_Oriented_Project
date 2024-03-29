import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { setPayment, fetchPayment } from "../auth";

function Basket() {
	const navigate = useNavigate();
	const [basket, setBasket] = useState([]);
	const [click, setClick] = useState(false);

	useEffect(() => {
		axios
			.get(`http://localhost:8000/basket`)
			.then((result) => {
				setBasket(result.data.basket);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	}, [click]);

	const make_order = () => {
		axios
			.get(`http://localhost:8000/make_order`)
			.then((response) => {
				setPayment(response.data.payment_id)
				navigate(`/payment/${response.data.payment_id}`);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	};

	const add_amount = (bookname) => {
		axios
			.put(`http://localhost:8000/basket/add_amount/${bookname}`)
			.then(() => {
				setClick(!click);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	};

	const reduce_amount = (bookname) => {
		axios
			.put(`http://localhost:8000/basket/reduce_amount/${bookname}`)
			.then(() => {
				setClick(!click);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	};

	const delete_amount = (bookname) => {
		axios
			.delete(`http://localhost:8000/basket/delete_item/${bookname}`)
			.then(() => {
				setClick(!click);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	};


	return (
		<div style={{ minHeight: 800, marginTop: 30 }}>
			<h1>Basket</h1>
			<div>
				<span>
					{basket?.map((book) => (
						<div>
							<div>
								<img src={book.cover} alt={book.cover} height="200px" />
							</div>
							<div>{book.name} </div>
							<div>{book.price} </div>
							<div>{book.genre} </div>
							<div>{book.amount} </div>
							<button type="button" onClick={() => add_amount(book.name)}>
								Add
							</button>
							<button type="button" onClick={() => reduce_amount(book.name)}>
								reduce
							</button>
							<button type="button" onClick={() => delete_amount(book.name)}>
								delete
							</button>
							<br></br>
						</div>
					))}{" "}
				</span>
				<div>
					<button type="button" onClick={make_order}>
						Make Order
					</button>
				</div>
			</div>
		</div>
	);
}
export default Basket;
