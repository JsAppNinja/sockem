import React, { Component } from "react";
import { withRouter } from "react-router-dom";

class Navbar extends Component {
  render() {
    return(
      <div>
        <h1>Navbar</h1>
      </div>
    );
  }
}

export default withRouter(Navbar);