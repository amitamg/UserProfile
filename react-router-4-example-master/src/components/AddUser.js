import React, { Component } from 'react';
import './AddUser.css';
import { Link } from 'react-router-dom';
import { API_BASE } from './Const';
import axios from 'axios';

class AddUser extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            age:0,
            skills:[],
            image1:undefined,
            image2:undefined
        }
    }
    componentDidMount() {
    }

    saveUserData=(contentType, data, setResponse)=>{
        axios({
            url: `${API_BASE}/api/cintauser`,
            method: 'POST',
            data: data,
            headers: {
            'Content-Type': contentType
            }
            }).then((response) => {
            setResponse(response.data);
            }).catch((error) => {
            setResponse("error");
            })
    }

    uploadWithJSON=async ()=>{
        const toBase64 = file => new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
        });
       
        let obj = { ...this.state }
        obj.image1 = await toBase64(obj.image1);
        obj.image2 = await toBase64(obj.image2);
       
        this.saveUserData("application/json", obj, (msg) => console.log(msg));
        }

    render() {
        return (
            <div className="home">
                <div><Link to="/">Cancel</Link></div>
                <div className={"add-user-container"}>
                    <div>Name : <input
                        type='text'
                        value={this.state.username}
                        onChange={(e) => {
                            this.setState({username:e.target.value})
                        }}
                    /></div>
                    <div>Age : <input
                        type='number'
                        value={this.state.age}
                        onChange={(e) => {
                            this.setState({age:parseInt(e.target.value)})
                        }}
                    /></div>
                    <div>skills : <input
                        type='text'
                        value={this.state.skills.toString()}
                        onChange={(e) => {
                            this.setState({skills:e.target.value.split(",")})
                        }}
                        placeholder=", separated values"
                    /></div>
                    <div>Image 1 : <input
                        type='file'
                        accept={'image/*'}
                        onChange={(e) => {
                            this.setState({image1:e.target.files[0]})
                        }}
                    /></div>
                    <div>Image 2 : <input
                        type='file'
                        accept={'image/*'}
                        onChange={(e) => {
                            this.setState({image2:e.target.files[0]})
                        }}
                    /></div>
                    <div>
                        <button onClick={(e)=>{
                            if(this.state.image1&&this.state.image2)
                            this.uploadWithJSON();
                        }}>SAVE</button>
                    </div>
                </div>
            </div>
        )
    }

}
export default AddUser;

