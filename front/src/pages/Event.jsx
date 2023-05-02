import React, { useState, useEffect } from "react";
import axios from "axios";

import AddEventForm from "../component/addEvent";
import ModifyEventForm from "../component/ModifyEvent";
import RemoveEventForm from "../component/removeEvent";

export default function Event() {
	const [allEvent, setAllEvent] = useState("");

	useEffect(() => {
		axios.get("http://localhost:8000/GetAllEvent/").then((response) => {
			setAllEvent(response.data);
		});
	}, []);

	return (
		<div>
			<div>
				<h2>Event Discount</h2>
				{allEvent &&
					allEvent.eventDis &&
					allEvent.eventDis.map((event) => <p>{event.event_name}</p>)}
			</div>
			<div>
				<h2>Modify Event</h2>
				<ModifyEventForm />
			</div>
		</div>
	);
}
