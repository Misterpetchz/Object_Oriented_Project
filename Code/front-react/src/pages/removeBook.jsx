import { useState } from "react"
import axios from "axios"

export default function RemoveBookForm(){

    const [bookName, setBookName] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.delete(`http://localhost:8000/books/${bookName}`);
      
            console.log('Response:', response.data);
            window.location.reload();
          } catch (error) {
            console.error('Error:', error);
          }
    }

    return (
        <form onSubmit={handleSubmit}>
            <div>
            <label>Book Name:</label>
            <input
            type="text"
            onChange={(e) => setBookName(e.target.value)}
            />
            </div>
            <button type="submit">Remove Book</button>
        </form>
    )
}