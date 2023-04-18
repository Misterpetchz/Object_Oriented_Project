import React from "react";
import { useState } from "react";
import axios from "axios";
import SearchBar from "./SearchBar";

export default function Searchs() {

    const [search_list, setSearchList] = useState([]);

    const clearResults = () => setQuotes([]);

    const searching = async search => {
        if (search == "") {
          return;
        } else {
          axios
            .post(`http://localhost:8000/search/?name=${search}`)
            .then((result) => {
                setSearchList(result.data.searchlist);
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
          <h1>Search page</h1>
          <SearchBar searching={searching} clearResults={clearResults}/>
                <ul>
                    {search_list.map((item) => (
                        <li>
                            <div>
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