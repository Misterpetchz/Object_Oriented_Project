import React from "react";
import { useState } from "react";
import axios from "axios";
import SearchBar from "../component/SearchBar";
import { useNavigate } from "react-router-dom";

export default function SearchBranch() {
	const Navigate = useNavigate();
	const [search_list_b, setSearchList_b] = useState([]);

	const clearResults = () => setQuotes([]);
	const onPress = (branch_name) => {
		Navigate(`/branch/${branch_name}`);
	};

	const searching = async (search) => {
		if (search == "") {
			return;
		} else {
			axios
				.post(`http://localhost:8000/branch/search/?name=${search}`)
				.then((result) => {
					setSearchList_b(result.data.branch);
					console.log(result);
				})
				.catch(function (error) {
					console.log(error, "error");
				});
		}
	};

	return (
		<div style={{ minHeight: 800, marginTop: 30 }}>
			<h1>Search page</h1>
			<SearchBar searching={searching} clearResults={clearResults} />
			<ul>
				{search_list_b.map((item) => (
					<li>
						<div>
							<button onClick={() => onPress(item.name)}>
								<span>{item.name} </span>
							</button>
						</div>
					</li>
				))}
			</ul>
		</div>
	);
}
