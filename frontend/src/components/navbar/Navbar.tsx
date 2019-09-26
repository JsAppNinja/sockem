import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import { RouteComponentProps } from "react-router";

// Type whatever you expect in 'this.props.match.params.*'
type PathParamsType = {
  // param1: string,
};

// Your component own properties
type PropsType = RouteComponentProps<PathParamsType> & {
  // someString: string,
};

class Navbar extends React.Component<PropsType> {
  render() {
    return (
      <div>
        <h1>Navbar</h1>
      </div>
    );
  }
}

export default withRouter(Navbar);
