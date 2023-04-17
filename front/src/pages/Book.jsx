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
            )
            .catch(function (error) {
              console.log(error, "error");
            });
        },[])

        const add_rating = () => {
          axios
              .post(`http://localhost:8000/books/${params.bookname}/addrating`, {
                comment:comment, score:score_each_rating
              })
              .then(() => {
                window.location.reload(false);
                })
              .catch(function (error) {
                console.log(error, "error");
              });
        }

        const add_book_to_basket = () => {
            axios
              .post(`http://localhost:8000/books/${params.bookname}/add_book_to_basket?amount=10`)
              .then(() => {
                  navigate("/")
                })
              .catch(function (error) {
                console.log(error, "error");
              });
          }
  

        return(
            <div style={{ minHeight: 800, marginTop: 30 }}>
              <h1>Home</h1>
                            <span>{book.cover} </span>
                            <span>{book.name} </span>
                            <span>{book.creator} </span>
                            <span>{book.old_price} </span>
                            <span>{book.new_price} </span>
                            <span>{book.genre?.map((genre)=>(
                                            <span>{genre}, </span>
                                    ))} </span>
                            <span>{book.score} </span>
                            <span>{book.brief} </span>
                            <span>{book.available_branch?.map((branch)=>(
                                            <span>{branch}, </span>
                                    ))} </span>
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
                              <input
                                type="number"
                                onChange={(e) => setRatingScore(e.target.value)}
                              />

                              <button type="button" onClick={add_rating}>
                                Post
                              </button>
                            </form>           
            </div>

          );
}
export default Book