import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import Navbar from "../navbar/Navbar";

class Home extends Component {
  render() {
    return(
      <div>
        <Navbar/>
        <h1>Home</h1>
      </div>
    );
  }
}

export default withRouter(Home);