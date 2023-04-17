import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useNavigate} from "react-router-dom";

function Book() {

    const navigate = useNavigate();
    const [book, setBook] = useState([]);
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
        },[])

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
                            <button type="button" onClick={add_book_to_basket}>
                                Add Book to Basket
                            </button>
                </div>
          );
}
export default Book