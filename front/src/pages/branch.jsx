import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useLocation, Route, Routes, useNavigate } from "react-router-dom";
import axios from "axios";
import AddBranchForm from "../component/addBranch";
import ModifyBranchForm from "../component/modifyBranch";
import RemoveBranch from "../component/removeBranch";

function Branches() {
	const Navigate = useNavigate();
	const [allBranch, setAllBranch] = useState([]);
	const onPress = (branch_name) => {
		Navigate(`/branch/${branch_name}`);
	};

	useEffect(() => {
		axios.get("http://localhost:8000/GetAllBranch/").then((response) => {
			setAllBranch(response.data);
		});
	}, []);

	return (
		<div>
			<div>
				{allBranch &&
					allBranch.name &&
					allBranch.name.map((branch) => (
						<div>
							<button onClick={() => onPress(branch.branch_name)}>
								<span>{branch.branch_name}</span>
							</button>
						</div>
					))}
			</div>
			<div>
				<h2>Add Branch</h2>
				<AddBranchForm />
			</div>
			<div>
				<h2>Modify Branch</h2>
				<ModifyBranchForm />
			</div>
			<div>
				<h2>Remove Branch</h2>
				<RemoveBranch />
			</div>
		</div>
	);
}

export default Branches;
