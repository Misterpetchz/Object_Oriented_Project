import { useState } from "react";
import axios from "axios";
import QrCode from "./QrCode";
import ViaCreditCard from "./ViaCreditCard";

export default function SelectMethod(){

    const [selectedPaymentMethod, setSelectedPaymentMethod] = useState('');
    // const [paymentStatus, setPaymentStatus] = useState('');

    const handlePaymentMethodSelect = (event) => {
        setSelectedPaymentMethod(event.target.value)
    }

    return (
        <div>
            <form>
                <label>Select a payment method : </label>
                <select id="paymentMethod" value={selectedPaymentMethod} onChange={handlePaymentMethodSelect}>
                    <option value="">-- Please Select --</option>
                    <option value="QrCode">QR Code</option>
                    <option value="CreditCard">Credit Card</option>
                </select>
                {selectedPaymentMethod === 'QrCode' && (
                    <div>
                        <h3>Pay with Qr Code</h3>
                        <QrCode />
                    </div>
                )}
                {selectedPaymentMethod === 'CreditCard' && (
                    <div>
                        <h3>Pay with Credit Card</h3>
                        <ViaCreditCard />
                    </div>
                )}
            </form>
            {/* <div>
                {selectedPaymentMethod !== '' && (
                    <div>
                        <button type="button" onClick={handlePaidClick}>Paid</button>
                        <button type="button" onClick={handleNotPaidClick}>Not Paid</button>
                    </div>
                )}
            </div> */}
        </div>
    )
}