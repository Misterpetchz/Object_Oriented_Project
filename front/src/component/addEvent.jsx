import { useState } from "react";
import axios from "axios";

export default function AddEventForm() {
	const [eventName, setEventName] = useState("");
	const [eventStart, setEventStart] = useState("");
	const [eventEnd, setEventEnd] = useState("");
	const [discountedPercentage, setDiscountedPercentage] = useState("");
	const [eventGenre, setEventGenre] = useState("");

	const handleSubmit = async (e) => {
		e.preventDefault();

		try {
			const response = await axios.post("http://localhost:8000/AddEvent", {
				event_name: eventName,
				event_start: eventStart,
				event_end: eventEnd,
				discounted_percentage: discountedPercentage,
				event_genre: eventGenre,
			});

			console.log("Response:", response.data);
			window.location.reload();
		} catch (error) {
			console.error("Error:", error);
		}
	};

	return (
		<form onSubmit={handleSubmit}>
			<div>
				<label>Name:</label>
				<input type="text" onChange={(e) => setEventName(e.target.value)} />
			</div>
			<div>
				<label>Start:</label>
				<input type="text" onChange={(e) => setEventStart(e.target.value)} />
			</div>
			<div>
				<label>End:</label>
				<input type="text" onChange={(e) => setEventEnd(e.target.value)} />
			</div>
			<div>
				<label>Discount Percentage:</label>
				<input
					type="text"
					onChange={(e) => setDiscountedPercentage(e.target.value)}
				/>
			</div>
			<div>
				<label>Genre:</label>
				<input type="text" onChange={(e) => setEventGenre(e.target.value)} />
			</div>
			<button type="submit">Add</button>
		</form>
	);
}
