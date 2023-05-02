import axios from "axios";
import { useNavigate } from "react-router";
import { useState } from "react";

export default function Register() {
	const navigate = useNavigate();
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [full_name, setFullname] = useState("");
	const [gender, setGender] = useState("");
	const [tel, setTel] = useState("");
	const [address, setAddress] = useState("");
	const [email_noti, setEmailNoti] = useState(false);
	const [sms_noti, setSmsNoti] = useState(false);
	const [fail, setFail] = useState("");

	const register = () => {
		if (
			username == "" ||
			password == "" ||
			full_name == "" ||
			gender == "" ||
			tel == "" ||
			address == ""
		) {
			return;
		} else {
			axios
				.post("http://localhost:8000/users/registration", {
					email: username,
					password: password,
					full_name: full_name,
					gender: gender,
					tel: tel,
					address: address,
					email_noti: email_noti,
					sms_noti: sms_noti,
				})
				.then(function (response) {
					if (response.data.status == "Success") {
						navigate("/login");
					} else if (response.data.status == "Reject") {
						setFail("Have already Username");
					}
				})
				.catch(function (error) {
					console.log(error, "error");
				});
		}
	};

	return (
		<div style={{ minHeight: 800, marginTop: 30 }}>
			<h1>Register page</h1>
			<div>
				<form>
					<div>
						<label style={{ marginRight: 10 }}>Username</label>
						<input type="text" onChange={(e) => setUsername(e.target.value)} />
					</div>
					<div>
						<label style={{ marginRight: 10 }}>Password</label>
						<input
							type="password"
							onChange={(e) => setPassword(e.target.value)}
						/>
					</div>
					<div>
						<label style={{ marginRight: 10 }}>Full Name</label>
						<input type="text" onChange={(e) => setFullname(e.target.value)} />
					</div>
					<div>
						<label style={{ marginRight: 10 }}>Gender</label>
						<input type="text" onChange={(e) => setGender(e.target.value)} />
					</div>
					<div>
						<label style={{ marginRight: 10 }}>Tel</label>
						<input type="text" onChange={(e) => setTel(e.target.value)} />
					</div>
					<div>
						<label style={{ marginRight: 10 }}>Address</label>
						<input type="text" onChange={(e) => setAddress(e.target.value)} />
					</div>
					<div>
						<label style={{ marginRight: 10 }}>Email Noti</label>
						<input
							type="checkbox"
							checked={email_noti}
							onChange={(e) => setEmailNoti(!email_noti)}
						/>
					</div>
					<div>
						<label style={{ marginRight: 10 }}>Sms Noti</label>
						<input
							type="checkbox"
							checked={sms_noti}
							onChange={(e) => setSmsNoti(!sms_noti)}
						/>
					</div>

					<button type="button" onClick={register}>
						Register
					</button>
				</form>
				<div>{fail}</div>
			</div>
		</div>
	);
}
