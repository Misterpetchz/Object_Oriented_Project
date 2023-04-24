import React, { useState, useEffect} from 'react'
import axios from 'axios'

export default function OrderList(){

    const [orderList, setOrderList] = useState([])

    useEffect(() =>{
        axios.get('http://localhost:8000/order_list/')
        .then(response => {
            setOrderList(response.data.order_list)
        })
        .catch(function (error) {
            console.log(error, "error");
            });
    },[])

    return (
        <div>
            <div>
                {orderList.map((order) => (
                    <div>
                        {order._purchased_item.map((item) => (
                            <div>
                                <p>{item._cover}</p>
                                <p>{item._name}</p>
                            </div>
                        ))}
                        <div>
                            <p>{order._user}</p>
                            <p>{order._total}</p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
