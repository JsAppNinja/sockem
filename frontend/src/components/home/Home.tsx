import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import { RouteComponentProps } from "react-router";
import Navbar from "../navbar/Navbar";

// Type whatever you expect in 'this.props.match.params.*'
type PathParamsType = {
    // param1: string,
}

// Your component own properties
type PropsType = RouteComponentProps<PathParamsType> & {
    // someString: string,
}

class Home extends React.Component<PropsType> {
  render() {
    return (
      <div>
        <Navbar />
        <h1>Home</h1>
      </div>
    );
  }
}

export default withRouter(Home);
