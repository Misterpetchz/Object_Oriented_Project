import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";

function Catalog() {

    const [list_of_book, setListofBook] = useState([]);

    useEffect(() => {
        axios
            .get(`http://localhost:8000/`)
            .then((result) => {
                setListofBook(result.data.catalog);
                }
            )
            .catch(function (error) {
              console.log(error, "error");
            });
        },[])

    return(
        <div style={{ minHeight: 800, marginTop: 30 }}>
          <h1>Home</h1>
                <ul>
                    {list_of_book.map((item) => (
                        <li>
                            <div>
                                <span>{item.cover} </span>
                                <span>{item.name} </span>
                                <span>{item.creator} </span>
                                <span>{item.old_price} </span>
                                <span>{item.new_price} </span>
                                <span>{item.genre.map((genre)=>(
                                        <span>{genre}, </span>
                                ))} </span>
                                <span>{item.score} </span>
                                <span>{item.brief} </span>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
      );
}
export default Catalog