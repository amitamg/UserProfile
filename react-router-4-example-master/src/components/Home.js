import React, {Component} from 'react';
import './Home.css';
import {Link} from 'react-router-dom';

class Home extends Component{
    constructor(props){
        super(props);
        this.state={
        }
    }
    componentDidMount(){
    }

    render(){

        return(
            <div className="home">
              <div><Link to="/add-user">Add User</Link></div>
            </div>
        )
    }

}

export default Home;