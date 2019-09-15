import React, { Component } from "react";
import { withRouter } from "react-router-dom";

class Register extends Component {
  render() {
    return(
      <div>
        <h1>Register</h1>
        <form className="Register-form" onSubmit={this.handleSubmit}>
            <input
              type="email"
              placeholder="email"
              required
              onChange={this.handleEmail}
            /> <br/>
            <input
              type="text"
              placeholder="username"
              required
              onChange={this.handleUsername}
            /> <br/>
            <input
              type="password"
              placeholder="password"
              required
              onChange={this.handlePassword}
            /> <br/>
            <button className="Register-submit btn btn-secondary" type="submit">
              Register
            </button>
        </form>
      </div>
    );
  }
}

export default withRouter(Register);