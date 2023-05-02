import { useState } from 'react';
import axios from 'axios';

function AddBranchForm() {
  const [branchName, setBranchName] = useState('');
  const [openTime, setOpenTime] = useState('');
  const [location, setLocation] = useState('');
  const [tel, setTel] = useState('');
  const [lineId, setLineId] = useState('');
  const [facebookId, setFacebookId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/AddBranch', {
        branch_name: branchName,
        open_time: openTime,
        location: location,
        tel: tel,
        line_id: lineId,
        facebook_id: facebookId,
      });

      console.log('Response:', response.data);
      window.location.reload();
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="branchName">Branch Name:</label>
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
          type="time"
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
      <button type="submit">Add Branch</button>
    </form>
  );
}

export default AddBranchForm
