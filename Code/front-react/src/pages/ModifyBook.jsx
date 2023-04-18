import { useEffect, useState } from "react";
import axios from "axios";

export default function ModifyBookForm(){

    const [currentBook, setCurrentBook] = useState('');
    const [cover, setCover] = useState('');
    const [brief, setBrief] = useState('');
    const [creator, setCreator] = useState('');
    const [bookName, setBookName] = useState('');
    const [bookInfo, setBookInfo] = useState('');
    const [bookPublisher, setBookPublisher] = useState('');
    const [bookPreview, setBookPreview] = useState('');
    const [criticReview, setCriticReview] = useState('');
    const [tableOfContent, setTableOfContent] = useState('');
    const [summary, setSummary] = useState('');
    const [genre, setGenre] = useState('');
    const [dateCreated, setDateCreated] =  useState('')
    const [price, setPrice] = useState('');
    const [amount, setAmount] = useState('');

    const genre_checkList = ["School", "Intense", "Shounen", "Drama", "Horror", "fantasy", "science", "history", "mystery", "thriller", "romance"];

    const handleCheckboxChange = (event) => {
        const item = event.target.name;
        const isChecked = event.target.checked;
        const newCheckedItems = isChecked
          ? [...genre, item]
          : genre.filter((genre) => genre !== item);
          setGenre(newCheckedItems);
    }

    const modify_book = () => {
        if(cover == '' ||
        brief == '' ||
        creator == '' ||
        bookName == '' ||
        bookInfo == '' ||
        bookPublisher == '' ||
        bookPreview == '' ||
        criticReview == '' ||
        tableOfContent == '' ||
        summary == '' ||
        genre == [] ||
        dateCreated == '' ||
        price == '' ||
        amount == ''){
            return ;
        } else {
            axios.put(`http://localhost:8000/books/${currentBook}`,{
                cover: cover,
                brief: brief,
                creator: creator,
                name: bookName,
                book_info: bookInfo,
                book_publisher: bookPublisher,
                book_preview: bookPreview,
                critic_review: criticReview,
                table_of_content: tableOfContent,
                summary: summary,
                genre: genre,
                date_created: dateCreated,
                price: price,
                amount: amount
            })
            .then((result) => {
                console.log(result);
                window.location.reload();
            }
            )
            .catch(function (error){
                console.log(error, 'error');
            })
        }
    };
    return (
        <form>
            <div>
                <label>Book:</label>
                <input 
                    type="text"
                    onChange={(e) => setCurrentBook(e.target.value)} 
                    />
            </div>
            <div>
                <label>Cover:</label>
                <input 
                    type="text"
                    onChange={(e) => setCover(e.target.value)} 
                    />
            </div>
            <div>
                <label>Brief:</label>
                <input 
                    type="text"
                    onChange={(e) => setBrief(e.target.value)} 
                    />
            </div>
            <div>
                <label>Creator:</label>
                <input 
                    type="text"
                    onChange={(e) => setCreator(e.target.value)} 
                    />
            </div>
            <div>
                <label>Name:</label>
                <input 
                    type="text"
                    onChange={(e) => setBookName(e.target.value)} 
                    />
            </div>
            <div>
                <label>Book Info:</label>
                <input 
                    type="text"
                    onChange={(e) => setBookInfo(e.target.value)} 
                    />
            </div>
            <div>
                <label>Book Publisher:</label>
                <input 
                    type="text"
                    onChange={(e) => setBookPublisher(e.target.value)} 
                    />
            </div>
            <div>
                <label>Book Preview:</label>
                <input 
                    type="text"
                    onChange={(e) => setBookPreview(e.target.value)} 
                    />
            </div>
            <div>
                <label>Critic Review:</label>
                <input 
                    type="text"
                    onChange={(e) => setCriticReview(e.target.value)} 
                    />
            </div>
            <div>
                <label>Content:</label>
                <input 
                    type="text"
                    onChange={(e) => setTableOfContent(e.target.value)} 
                    />
            </div>
            <div>
                <label>Summary:</label>
                <input 
                    type="text"
                    onChange={(e) => setSummary(e.target.value)} 
                    />
            </div>
            <div>
                {genre_checkList.map((item) => (
                    <label key={item}>
                        <input 
                            type="checkbox"
                            name={item}
                            checked={genre.includes(item)}
                            onChange={handleCheckboxChange} 
                            />
                            {item}
                    </label>
                ))}
            </div>
            <div>
                <label>Date Created:</label>
                <input 
                    type="text"
                    onChange={(e) => setDateCreated(e.target.value)} 
                    />
            </div>
            <div>
                <label>Price:</label>
                <input 
                    type="text"
                    onChange={(e) => setPrice(e.target.value)} 
                    />
            </div>
            <div>
                <label>Amount:</label>
                <input 
                    type="text"
                    onChange={(e) => setAmount(e.target.value)} 
                    />
            </div>
            <button type="button" onClick={modify_book} >Modify</button>
        </form>
    )
}