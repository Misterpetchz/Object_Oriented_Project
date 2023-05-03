import React, { useState, useEffect } from "react";
import axios from "axios";

export default function OrderList() {
	const [orderList, setOrderList] = useState([]);

	useEffect(() => {
		axios
			.get("http://localhost:8000/order_list/")
			.then((response) => {
				setOrderList(response.data.order_list);
				console.log(response.data.order_list)
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	}, []);

	return (
		<div>
			<div>
				{orderList.map((order) => (
					<div>
						{order.purchased_item.map((item) => (
							<div class="book">
								<img class="book_img" src={item.cover}/>
								<p class="book_detail">{item.name}</p>
							</div>
						))}
						<div>
							<p>{order.total}</p>
						</div>
					</div>
				))}
			</div>
		</div>
	);
}
