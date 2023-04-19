import { useEffect, useState } from "react";
import { useNavigate } from "react-router";
import axios from "axios";


export default function Admin(){

    const[add_book_cover, setAddCover] = useState("");
    const[add_book_brief, setAddBrief] = useState("");
    const[add_book_creator, setAddCreator] = useState("");
    const[add_book_name, setAddName] = useState("");
    const[add_book_book_info, setAddBookInfo] = useState("");
    const[add_book_book_publisher, setAddBookPublisher] = useState("");
    const[add_book_book_preview, setAddBookPreview] = useState("");
    const[add_book_critic_review, setAddCriticReview] = useState("");
    const[add_book_table_of_content, setAddTableofContent] = useState("");
    const[add_book_summary, setAddSummary] = useState("");
    const[add_book_genre, setAddGenre] = useState([]);
    const[add_book_date_created, setAddDateCreated] = useState("");
    const[add_book_price, setAddPrice] = useState("");
    const[add_book_amount, setAddAmount] = useState("");
    
    const genre_checkList = ["School", "Intense", "Shounen", "Drama"];
    
    const handleCheckboxChange = (event) => {
        const item = event.target.name;
        const isChecked = event.target.checked;
        const newCheckedItems = isChecked
          ? [...add_book_genre, item]
          : add_book_genre.filter((add_book_genre) => add_book_genre !== item);
          setAddGenre(newCheckedItems);
    }

    const add_book = () => {
        if (add_book_cover == "" ||
        add_book_brief == "" ||
        add_book_creator == "" ||
        add_book_name == "" ||
        add_book_book_info == "" ||
        add_book_book_publisher == "" ||
        add_book_book_preview == "" ||
        add_book_critic_review == "" ||
        add_book_table_of_content == "" ||
        add_book_summary == "" ||
        add_book_genre == [] ||
        add_book_date_created == "" ||
        add_book_price == "" ||
        add_book_amount == "") {
          return;
        } else {
          axios
            .post(`http://localhost:8000/addbook`,
            {
                cover: add_book_cover,
                brief:add_book_brief,
                creator:add_book_creator,
                name:add_book_name,
                book_info : add_book_book_info,
                book_publisher : add_book_book_publisher,
                book_preview : add_book_book_preview,
                critic_review : add_book_critic_review,
                table_of_content : add_book_table_of_content,
                summary : add_book_summary,
                genre : add_book_genre,
                date_created : add_book_date_created,
                price : add_book_price,
                amount : add_book_amount
            })
            .then((result) => {
                console.log(result)
            }
            )
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
                  <label style={{ marginRight: 10 }}>Cover</label>
                  <input
                    type="text"
                    onChange={(e) => setAddCover(e.target.value)}
                  />
                  </div>
                  <div>
                  <label style={{ marginRight: 10 }}>Brief</label>
                  <input
                    type="text"
                    onChange={(e) => setAddBrief(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Creator</label>
                    <input
                    type="text"
                    onChange={(e) => setAddCreator(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Name</label>
                    <input
                    type="text"
                    onChange={(e) => setAddName(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Book Info</label>
                    <input
                    type="text"
                    onChange={(e) => setAddBookInfo(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Book Publisher</label>
                    <input
                    type="text"
                    onChange={(e) => setAddBookPublisher(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Book Preview</label>
                    <input
                    type="text"
                    onChange={(e) => setAddBookPreview(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Critic Review</label>
                    <input
                    type="text"
                    onChange={(e) => setAddCriticReview(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Table of Content</label>
                    <input
                    type="text"
                    onChange={(e) => setAddTableofContent(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Summary</label>
                    <input
                    type="text"
                    onChange={(e) => setAddSummary(e.target.value)}
                  />
                    </div>
                    <div>
                        {genre_checkList.map((item) => (
                        <label key={item}>
                        <input
                            type="checkbox"
                            name={item}
                            checked={add_book_genre.includes(item)}
                            onChange={handleCheckboxChange}
                        />
                        {item}
                        </label>
                        ))}
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Date Created</label>
                    <input
                    type="text"
                    onChange={(e) => setAddDateCreated(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Price</label>
                    <input
                    type="number"
                    onChange={(e) => setAddPrice(e.target.value)}
                  />
                    </div>
                    <div>
                    <label style={{ marginRight: 10 }}>Amount</label>
                    <input
                    type="number"
                    onChange={(e) => setAddAmount(e.target.value)}
                  />
                    </div>
                    
                  <button type="button" onClick={add_book}>
                    Add Book
                  </button>
                </form>
              </div>
        </div>
        
      );
    }