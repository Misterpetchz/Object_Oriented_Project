import { useState } from "react";
import axios from "axios";

function RemoveBranch() {
	const [branchName, setBranchName] = useState("");

	const handleSubmit = async (e) => {
		e.preventDefault();

		try {
			const response = await axios.delete(
				`http://localhost:8000/RemoveBranch/${branchName}`
			);

			console.log("Response:", response.data);
			window.location.reload();
		} catch (error) {
			console.error("Error:", error);
		}
	};
	return (
		<form onSubmit={handleSubmit}>
			<div>
				<label htmlFor="branchName">Branch Name:</label>
				<input
					type="text"
					id="branchName"
					value={branchName}
					onChange={(e) => setBranchName(e.target.value)}
				/>
			</div>
			<button type="submit">Remove Branch</button>
		</form>
	);
}

export default RemoveBranch;
