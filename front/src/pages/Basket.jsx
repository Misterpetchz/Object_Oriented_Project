import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Basket() {

    const navigate = useNavigate();
    const [basket, setBasket] = useState([]);

    useEffect(() => {
        axios
            .get(`http://localhost:8000/basket`)
            .then((result) => {
                setBasket(result.data.basket);
                }
            )
            .catch(function (error) {
              console.log(error, "error");
            });
        },[])

    const make_order = () => {
        axios
            .get(`http://localhost:8000/make_order`)
            .then((response) => {
                navigate(`/payment/${response.data.id}`)
            })
            .catch(function (error) {
            console.log(error, "error");
            });
    }

    return(
        <div style={{ minHeight: 800, marginTop: 30 }}>
            <h1>Basket</h1>
            <div>
                <span>{basket?.map((book)=>(
                                <div>
                                    <div>{book.cover} </div>
                                    <div>{book.name} </div>
                                    <div>{book.price} </div>
                                    <div>{book.genre} </div>
                                    <div>{book.amount} </div>
                                    <br></br>
                                </div>
                        ))} </span>
                <div>
                <button type="button" onClick={make_order}>
                    Make Order
                </button>
                </div>
            </div>          
        </div>

        );
}
export default Basket