import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import "../css/home.css";

function Catalog() {
	const navigate = useNavigate();
	const [list_of_book, setListofBook] = useState([]);

	useEffect(() => {
		axios
			.get(`http://localhost:8000/`)
			.then((result) => {
				setListofBook(result.data.catalog);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
	}, []);

	return (
		<div style={{ minHeight: 800, marginTop: 30 }}>
			<h1>Home</h1>
			<ul>
				{list_of_book.map((item) => (
					<div class="book">
						<img class="book_img" src={item.cover}></img>
						<br></br>
						<div class="book_detail">
							<button onClick={() => navigate(`/books/${item.name}`)}>
								<b>
									<u>Book name</u> :{" "}
								</b>
								{item.name}{" "}
							</button>
							<div>
								<b>
									<u>Author</u> :{" "}
								</b>
								{item.creator}{" "}
							</div>
							<div>
								<del>
									<b>
										<u>Price</u> :{" "}
									</b>
									{item.old_price}
								</del>
							</div>
							<div>
								<b>
									<u>Discounted</u> :{" "}
								</b>
								{item.new_price}{" "}
							</div>
							<div>
								<b>
									<u>Genre</u> :{" "}
								</b>
								{item.genre.join(", ")}
							</div>
							<div>
								<b>
									<u>Rating</u> :{" "}
								</b>
								{item.score}{" "}
							</div>
							<div>
								<b>
									<u>Brief</u> :{" "}
								</b>
								{item.brief}{" "}
							</div>
						</div>
					</div>
				))}
			</ul>
		</div>
	);
}
export default Catalog;
