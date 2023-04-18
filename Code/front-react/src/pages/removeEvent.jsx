import { useState } from "react"
import axios from "axios"

export default function RemoveEventForm(){

    const [eventName, setEventName] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.delete(`http://localhost:8000/RemoveEvent/${eventName}`);
            console.log('Response:', response.data);
            window.location.reload();
          } catch (error) {
            console.error('Error:', error);
          }
    }

    return (
        <form onSubmit={handleSubmit}>
            <div>
            <label>Event Name:</label>
            <input
            type="text"
            onChange={(e) => setEventName(e.target.value)}
            />
            </div>
            <button type="submit">Remove Event</button>
        </form>
    )
}