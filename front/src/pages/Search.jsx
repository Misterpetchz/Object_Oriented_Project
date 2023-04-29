import React from "react";
import { useState } from "react";
import axios from "axios";
import SearchBar from "../component/SearchBar";
import {useNavigate} from "react-router-dom";

export default function Searchs() {
    const navigate = useNavigate();
    const [search_list, setSearchList] = useState([]);

    const clearResults = () => setQuotes([]);

    const delay = ms => new Promise(
      resolve => setTimeout(resolve, ms)
    );

    const searching = async search => {
        if (search == "") {
          return;
        } else {
          await delay(100);
          axios
            .post(`http://localhost:8000/search/?name=${search}`)
            .then((result) => {
                setSearchList(result.data.searchlist);
                console.log(result)
                }
            )
            .catch(function (error) {
              console.log(error, "error");
            })  
        }
      };
    
      return (
        <div style={{ minHeight: 800, marginTop: 30 }}>
          <h1>Search page</h1>
          <SearchBar searching={searching} clearResults={clearResults}/>
                <ul>
                    {search_list.map((item) => (
                        <p class='book'>
                        <img class='book_img' src='{item.cover}'></img><br></br>
                        <div class='book_detail'>
                            <button onClick={() => navigate(`/books/${item.name}`)}><b><u>Book name</u> : </b>{item.name} </button>
                            <div><b><u>Author</u> : </b>{item.creator} </div>
                            <div><b><u>Price</u> : </b>{item.old_price} </div>
                            <div><b><u>Discounted</u> : </b>{item.new_price} </div>
                            <div><b><u>Genre</u> : </b>{item.genre.map((genre)=>(
                                    <span>{genre}, </span>
                            ))} </div>
                            <div><b><u>Rating</u> : </b>{item.score} </div>
                            <div><b><u>Brief</u> : </b>{item.brief} </div>
                        </div>
                    </p>
                    ))}
                </ul>
            </div>
      );
    }