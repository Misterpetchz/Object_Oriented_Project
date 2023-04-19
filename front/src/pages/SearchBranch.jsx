import React from "react";
import { useState } from "react";
import axios from "axios";
import SearchBar from "./SearchBar";
import { NavLink } from "react-router-dom";

export default function SearchBranch() {

    const [search_list_b, setSearchList_b] = useState([]);

    const clearResults = () => setQuotes([]);

    const searching = async search => {
        if (search == "") {
          return;
        } else {
          axios
            .post(`http://localhost:8000/branch/search/?name=${search}`)
            .then((result) => {
                setSearchList_b(result.data.branch);
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
                    {search_list_b.map((item) => (
                        <li>
                            <div>
                                    <span>{item.name} </span>
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
      );
    }
