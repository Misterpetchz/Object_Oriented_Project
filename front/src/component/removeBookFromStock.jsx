import axios from "axios";
import { useState, useEffect } from "react";

export default function RemoveBookFromStock() {
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

	const handleRemoveSubmit = (event) => {
		event.preventDefault();
		if (selectedBranches.length > 0 && selectedBook !== "") {
			selectedBranches.forEach((branch) => {
				axios
					.delete(
						`http://localhost:8000/RemoveBookFromBranch/${branch}/${selectedBook}`
					)
					.then((result) => {
						console.log(`${selectedBook} has been remove from branch success`);
						setSelectedBook("");
						setSelectedBranches([]);
					});
			});
		}
	};

	return (
		<div>
			<h2>Remove book from stock</h2>
			<form onSubmit={handleRemoveSubmit}>
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
				<button type="submit">Remove book from stock</button>
			</form>
		</div>
	);
}
