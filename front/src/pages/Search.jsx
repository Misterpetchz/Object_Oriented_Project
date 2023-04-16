import React from "react";
import { useState } from "react";
import axios from "axios";


export default function Searchs() {

    const [search, setSearch] = useState("");
    const [search_list, setSearchList] = useState([]);

    const searching = () => {
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
          <div style={{ marginTop: 30 }}>
            <form>
                <label style={{ marginRight: 10 }}>Input Book Name</label>
                <input
                type="text"
                onChange={(e) => setSearch(e.target.value)}
                />
                <button type="button" onClick={searching}>
                search
                </button>
            </form>
            <div>
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
                                    <span>{item.brie} </span>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
          </div>
        </div>
      );
    }