import axios from "axios";
import { useState, useEffect } from "react";

export default function AddBookToStock() {
	const [listOfBook, setListOfBook] = useState([]);
	const [selectedBook, setSelectedBook] = useState("");
	const [selectedBranches, setSelectedBranches] = useState([]);
	const [branchList, setBranchList] = useState([]);

	const handleCheckboxChange = (event) => {
		const item = event.target.name;
		const isChecked = event.target.checked;
		const newSelectedBranches = isChecked
			? [...selectedBranches, item]
			: selectedBranches.filter((branch) => branch !== item);
		setSelectedBranches(newSelectedBranches);
	};

	useEffect(() => {
		axios
			.get(`http://localhost:8000/`)
			.then((result) => {
				setListOfBook(result.data.catalog);
			})
			.catch(function (error) {
				console.log(error, "error");
			});
		axios.get(`http://localhost:8000/GetAllBranch/`).then((result) => {
			setBranchList(result.data.name);
		});
	}, []);

	const handleFormSubmit = (event) => {
		event.preventDefault();
		if (selectedBranches.length > 0 && selectedBook !== "") {
			selectedBranches.forEach((branch) => {
				axios
					.post(`http://localhost:8000/AddBookToBranch/`, {
						book_name: selectedBook,
						branch_name: branch,
					})
					.then((result) => {
						console.log(`Add to stock success at branch ${branch}`);
						setSelectedBook("");
						setSelectedBranches([]);
					})
					.catch((error) => {
						console.log(`Add to stock failed at branch ${branch}: ${error}`);
					});
			});
		}
	};

	return (
		<div>
			<h2>Add book to stock</h2>
			<form onSubmit={handleFormSubmit}>
				<div>
					<label>Book</label>
					<select
						value={selectedBook}
						onChange={(e) => setSelectedBook(e.target.value)}
					>
						<option value="">----</option>
						{listOfBook.map((book) => (
							<option key={book.id} value={book.name}>
								{book.name}
							</option>
						))}
					</select>
				</div>
				<div>
					<label>Branches</label>
					{branchList.map((branch, index) => (
						<div key={index}>
							<label>
								<input
									type="checkbox"
									name={branch.branch_name}
									checked={selectedBranches.includes(branch.branch_name)}
									onChange={handleCheckboxChange}
								/>
								{branch.branch_name}
							</label>
						</div>
					))}
				</div>
				<button type="submit">Add book to stock</button>
			</form>
		</div>
	);
}
