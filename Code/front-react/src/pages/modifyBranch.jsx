import React, { useState } from "react"
import axios from "axios"

function ModifyBranchForm(){
    const [oldName, setOldName] = useState('');
    const [branchName, setBranchName] = useState('');
    const [openTime, setOpenTime] = useState('');
    const [location, setLocation] = useState('');
    const [tel, setTel] = useState('');
    const [lineId, setLineId] = useState('');
    const [facebookId, setFacebookId] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
    

    try {
        const response = await axios.put(`http://localhost:8000/ModifyBranch/${oldName}`, {
          branch_name: branchName,
          open_time: openTime,
          location: location,
          tel: tel,
          line_id: lineId,
          facebook_id: facebookId,
        //   add_book: [],
        //   remove_book: []
        });
  
        console.log('Response:', response.data);
        window.location.reload();
      } catch (error) {
        console.error('Error:', error);
      }
    }

    return (
        <form onSubmit={handleSubmit}>
        <div>
            <label htmlFor="oldName">Branch Name:</label>
            <input
            type="text"
            id="oldName"
            value={oldName}
            onChange={(e) => setOldName(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="branchName">New Branch Name:</label>
            <input
            type="text"
            id="branchName"
            value={branchName}
            onChange={(e) => setBranchName(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="openTime">Open Time:</label>
            <input
            type="text"
            id="openTime"
            value={openTime}
            onChange={(e) => setOpenTime(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="location">Location:</label>
            <input
            type="text"
            id="location"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="tel">Tel:</label>
            <input
            type="text"
            id="tel"
            value={tel}
            onChange={(e) => setTel(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="lineId">Line ID:</label>
            <input
            type="text"
            id="lineId"
            value={lineId}
            onChange={(e) => setLineId(e.target.value)}
            />
        </div>
        <div>
            <label htmlFor="facebookId">Facebook ID:</label>
            <input
            type="text"
            id="facebookId"
            value={facebookId}
            onChange={(e) => setFacebookId(e.target.value)}
            />
        </div>
        <button type="submit">Modify Branch</button>
        </form>
    )
}

export default ModifyBranchForm