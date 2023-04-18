import axios from "axios";
import { useNavigate } from "react-router";
import { useState } from "react";

export default function EditProfile() {
  const navigate = useNavigate();
  const [password, setPassword] = useState("");
  const [full_name, setFullname] = useState("");
  const [gender, setGender] = useState("");
  const [tel, setTel] = useState("");
  const [address, setAddress] = useState("");
  const [email_noti, setEmailNoti] = useState("");
  const [sms_noti, setSmsNoti] = useState("");

  const editprofile = () => {
    if ((password == "") &&
    (full_name == "") &&
    (gender == "") &&
    (tel == "") &&
    (address == "") && 
    (email_noti == "") &&
    (sms_noti == "")){
      return;
    } else {
      axios
        .put("http://localhost:8000/users/edit", {
           password : password, full_name : full_name,
            gender : gender, tel : tel, address : address,
            email_noti : email_noti, sms_noti : sms_noti
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
                onChange={(e) => setFullname(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Gender</label>
                <input
                type="text"
                onChange={(e) => setGender(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Tel</label>
                <input
                type="text"
                onChange={(e) => setTel(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Address</label>
                <input
                type="text"
                onChange={(e) => setAddress(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Email Noti</label>
                <input
                type="text"
                onChange={(e) => setEmailNoti(e.target.value)}
              />
                </div>
                <div>
                <label style={{ marginRight: 10 }}>Sms Noti</label>
                <input
                type="text"
                onChange={(e) => setSmsNoti(e.target.value)}
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