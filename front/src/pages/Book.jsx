import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useNavigate} from "react-router-dom";

function Book() {

    const navigate = useNavigate();
    const [book, setBook] = useState([]);
    const [score_each_rating, setRatingScore] = useState("");
    const [comment, setComment] = useState("");
    const [rating, setRating] = useState([]);
    const [comment_submit, setCommentSubmit] = useState(false)
    const params = useParams()

    useEffect(() => {
        axios
            .get(`http://localhost:8000/books/${params.bookname}`)
            .then((result) => {
                setBook(result.data);
                }
            )
            .catch(function (error) {
              console.log(error, "error");
            });
        axios
            .get(`http://localhost:8000/books/${params.bookname}/rating`)
            .then((result) => {
                setRating(result.data);
                }
            ).then(
              setCommentSubmit(false)
            )
            .catch(function (error) {
              console.log(error, "error");
            });
        },[comment_submit])

        const add_rating = () => {
          axios
              .post(`http://localhost:8000/books/${params.bookname}/addrating`, {
                comment:comment, score:score_each_rating
              })
              .then(
                setCommentSubmit(true)
              )
              .catch(function (error) {
                console.log(error, "error");
              });
        }

        const add_book_to_basket = () => {
            axios
              .post(`http://localhost:8000/books/${params.bookname}/add_book_to_basket?amount=1`)
              .then(() => {
                  navigate("/basket")
                })
              .catch(function (error) {
                console.log(error, "error");
              });
          }
  

        return(
            <div style={{ minHeight: 800, marginTop: 30 }}>
              <h1>Home</h1>
                            <img src={book.cover} height="200px" />
                            <span>{book.name} </span><br></br>
                            <span>{book.creator} </span><br></br>
                            <span>{book.old_price} </span><br></br>
                            <span>{book.new_price} </span><br></br>
                            <span>{book.genre?.map((genre)=>(
                                            <span>{genre}, </span>
                                    ))} </span><br></br>
                            <span>{book.score} </span><br></br>
                            <span>{book.brief} </span><br></br>
                            <span>{book.available_branch?.map((branch)=>(
                                            <span>{branch.name}, </span>
                                    ))} </span><br></br><br></br>
                            <div>
                            <button type="button" onClick={add_book_to_basket}>
                                Add Book to Basket
                            </button>
                            </div>
                            <div>Over all Score {rating.rating_score} </div>
                            <div>{rating.rating?.map((rate)=>(
                                            <div>{rate.score_each_rating} {rate.comment}</div>
                                            
                                    ))} </div>
                            <form>
                              <label style={{ marginRight: 10 }}>Comment</label>
                              <input
                                type="text"
                                onChange={(e) => setComment(e.target.value)}
                              />

                              <label style={{ marginRight: 10 }}>Score</label>
                              <select onChange={(e) => setRatingScore(parseInt(e.target.value))}>
                                <option>--</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5">5</option>
                                <option value="6">6</option>
                                <option value="7">7</option>
                                <option value="8">8</option>
                                <option value="9">9</option>
                                <option value="10">10</option>
                              </select>

                              <button type="button" onClick={add_rating}>
                                Post
                              </button>
                            </form>           
            </div>

          );
}
export default Book