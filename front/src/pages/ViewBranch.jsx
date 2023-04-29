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
                <div>
                  <span>Name : {branch.name} </span><br></br>
                  <span>Open Time : {branch.open} </span><br></br>
                  <span>Location : {branch.location} </span><br></br>
                  <span>Tel : {branch.tel} </span><br></br>
                  <span>Line ID : {branch.line_id} </span><br></br>
                  <span>Facebook : {branch.facebook_id} </span><br></br>
                  <div>
                    <h3>Products in stock</h3>
                      {branch.product && branch.product && branch.product.map((product, index) => (
                        <div key={index}>
                          <span>{product._name}</span>
                        </div>
                      ))}
                  </div>
                </div>     
            </div>

          );
}
export default ViewBranch