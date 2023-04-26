import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";
import { useParams} from "react-router-dom";

function ViewBranch() {

    const [branch, setBranch] = useState([]);
    const params = useParams()

    useEffect(() => {
        axios
            .get(`http://localhost:8000/branch/${params.name}`)
            .then((result) => {
                setBranch(result.data);
                }
            )
            .catch(function (error) {
              console.log(error, "error");
            });
        },[])

        return(
            <div style={{ minHeight: 800, marginTop: 30 }}>
              <h1>Home</h1>
                            <span>{branch.name} </span><br></br>
                            <span>{branch.open_time} </span><br></br>
                            <span>{branch.location} </span><br></br>
                            <span>{branch.tel} </span><br></br>
                            <span>{branch.line_id} </span><br></br>
                            <span>{branch.facebook_id} </span><br></br>
                            <div>
                            </div>     
            </div>

          );
}
export default ViewBranch