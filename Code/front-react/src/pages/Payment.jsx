import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

import SelectMethod from "./SelectMethodPayment";

export default function Payment(){

    const { id } = useParams();
    const [order, setOrder] = useState('');

    useEffect(() => {
        axios.get(`http://localhost:8000/payment/${id}`)
        .then(response => {
            setOrder(response.data)
        })
        .catch(function (error) {
            console.log(error, "error");
            });
    },[id])

    return (
        <div>
            <h2>Order</h2>
            {order && order._purchased_item && order._purchased_item.map((item) => (
                <div>
                    <p>Name : {item._name}</p>
                    <p>Price : {item._price}</p>
                    <p>Amount : {item._amount}</p>
                </div>
            ))}
            <div>
                <p>Total : {order._total}</p>
            </div>
            <div>
                <SelectMethod />
            </div>
        </div>
    )
}