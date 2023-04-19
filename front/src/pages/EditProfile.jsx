import axios from "axios";
import { useNavigate } from "react-router";
import { useState, useEffect } from "react";

export default function EditProfile() {
  const navigate = useNavigate();
  const [old_data, setOldData] = useState("");
  const [password, setPassword] = useState("");
  const [full_name, setFullname] = useState("");
  const [gender, setGender] = useState("");
  const [tel, setTel] = useState("");
  const [address, setAddress] = useState("");
  const [email_noti, setEmailNoti] = useState(false);
  const [sms_noti, setSmsNoti] = useState(false);

  useEffect(() => {
    axios
        .get(`http://localhost:8000/user`)
        .then((result) => {
            setOldData(result.data);
            setSmsNoti(result.data.sms_noti)
            setEmailNoti(result.data.email_noti)
            }
        )
        .catch(function (error) {
          console.log(error, "error");
        });
    },[])

  const editprofile = () => {
    if ((password == "") &&
    (full_name == "") &&
    (gender == "") &&
    (tel == "") &&
    (address == "") &&
    (email_noti == old_data.email_noti) &&
    (sms_noti == old_data.sms_noti)){
      navigate("/profile");
    } else {
      axios
        .put("http://localhost:8000/users/edit", {
           password : password, full_name : full_name,
            gender : gender, tel : tel, address : address,
            email_noti : old_data.email_noti, sms_noti : old_data.sms_noti
        })
        .then((response) => {
          if (response.data.status == "Success") {
            navigate("/profile");
          }
        })
        .catch(function (error) {
          console.log(error, "error");
        });
    }
  };

  const handleInputChange = (event) => {
    const { name, type, checked, value } = event.target;
    const newValue = type === 'checkbox' ? checked : value;

    setOldData({
      ...old_data,
      [name]: newValue
    });
  };

  return (
    <div style={{ minHeight: 800, marginTop: 30 }}>
      <h1>Edit page</h1>
          <div>
            <form>
              <div>
              <label style={{ marginRight: 10 }}>Password</label>
              <input
                type="password"
                onChange={(e) => setPassword(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Full Name</label>
                <input
                type="text"
                placeholder={old_data.full_name}
                onChange={(e) => setFullname(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Gender</label>
                <input
                type="text"
                placeholder={old_data.gender}
                onChange={(e) => setGender(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Tel</label>
                <input
                type="text"
                placeholder={old_data.tel}
                onChange={(e) => setTel(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Address</label>
                <input
                type="text"
                placeholder={old_data.address}
                onChange={(e) => setAddress(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Email Noti</label>
                <input
                type="checkbox"
                name="email_noti"
                checked={old_data.email_noti}
                onChange={handleInputChange}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Sms Noti</label>
                <input
                type="checkbox"
                name="sms_noti"
                checked={old_data.sms_noti}
                onChange={handleInputChange}
              />
                </div>  
              <button type="button" onClick={editprofile}>
                Edit
              </button>
            </form>
          </div>
    </div>
  );
}