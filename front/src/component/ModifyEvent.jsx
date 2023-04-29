import { useState } from "react"
import axios from "axios"

export default function ModifyEventForm(){

    const [eventName, setEventName] = useState('');
    const [eventStart, setEventStart] = useState('');
    const [eventEnd, setEventEnd] = useState('');
    const [discountedPercentage, setDiscountedPercentage] = useState('');
    const [eventGenre, setEventGenre] = useState('');

    const genre_checkList = ["School", "Intense", "Shounen", "Drama"];

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
          const response = await axios.put(`http://localhost:8000/ModifyEvent/`, {
            event_name : eventName,
            event_start: eventStart,
            event_end: eventEnd,
            discounted_percentage: discountedPercentage,
            event_genre: eventGenre
          });

          console.log('Response:', response.data);
          window.location.reload();
        } catch (error) {
          console.error('Error:', error);
        }
      };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label>Name : </label>
                <input
                    type="text"
                    onChange={(e) => setEventName(e.target.value)}
                    />
            </div>
            <div>
                <label>Start : </label>
                <input
                    type="text"
                    onChange={(e) => setEventStart(e.target.value)}
                    />
            </div>
            <div>
                <label>End : </label>
                <input
                    type="text"
                    onChange={(e) => setEventEnd(e.target.value)}
                    />
            </div>
            <div>
                <label>Discount Percentage : </label>
                <input
                    type="text"
                    onChange={(e) => setDiscountedPercentage(parseFloat(e.target.value))}
                    />
            </div>
            <div>
                    <label>Discount Genre : </label>
                    <select onChange={(e) => setEventGenre(e.target.value)}>
                        <option>--</option>
                        {genre_checkList.map((item) => (
                            <option value={item}>{item}</option>
                        ))}
                      </select>
                    </div>
            <button type="submit">Modify</button>
        </form>
    )
}
