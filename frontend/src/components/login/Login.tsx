import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import { RouteComponentProps } from "react-router";

// Type whatever you expect in 'this.props.match.params.*'
type PathParamsType = {
    // param1: string,
}

// Your component own properties
type PropsType = RouteComponentProps<PathParamsType> & {
    // someString: string,
}

class Login extends React.Component<PropsType> {
  render() {
    return (
      <div>
        <h1>Login</h1>
      </div>
    );
  }
}

export default withRouter(Login);
