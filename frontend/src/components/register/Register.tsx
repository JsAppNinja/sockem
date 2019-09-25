import React, { Component } from "react";
import { withRouter } from "react-router-dom";
import { RouteComponentProps } from "react-router";
import axios from "axios";

const url: string = process.env.REACT_APP_API_USERS_URL as string;

// Type whatever you expect in 'this.props.match.params.*'
type PathParamsType = {
    // param1: string,
}

// Your component own properties
type PropsType = RouteComponentProps<PathParamsType> & {
    // someString: string,
}

class Register extends React.Component<PropsType> {
  state = {
    email: "",
    username: "",
    password: ""
  };

  validateEmail() {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    let message = "";
    if (!re.test(this.state.email.toLowerCase())) {
      message += "Invalid email form.\n";
    }
    if (this.state.email.length > 254 || this.state.email.length === 0) {
      message += "Invalid email length.\n";
    }
    return message;
  }

  validateUsername() {
    const re = /^[A-Za-z0-9]+$/;
    let message = "";
    if (!re.test(this.state.username)) {
      message += "Invalid username form.\n";
    }
    if (this.state.username.length > 150 || this.state.username.length === 0) {
      message += "Invalid username length\n";
    }
    return message;
  }

  validatePassword() {
    const allNums = /^[0-9]+$/;
    const allChar = /^[a-zA-Z]+$/;
    let message = "";
    if (allNums.test(this.state.password)) {
      message += "Invalid password. Password cannot be all numbers.\n";
    }
    if (allChar.test(this.state.password)) {
      message +=
        "Invalid password. Password must contain at least one number.\n";
    }
    if (this.state.password.length > 30 || this.state.password.length < 9) {
      message += "Invalid password length\n";
    }
    return message;
  }

  handleEmail = (event: React.FormEvent<HTMLInputElement>): void => {
    this.setState({ email: (event.target as HTMLTextAreaElement).value });
  };

  handleUsername = (event: React.FormEvent<HTMLInputElement>): void => {
    this.setState({ username: (event.target as HTMLTextAreaElement).value });
  };

  handlePassword = (event: React.FormEvent<HTMLInputElement>): void => {
    this.setState({ password: (event.target as HTMLTextAreaElement).value });
  };

  handleSubmit = (event: React.FormEvent<HTMLFormElement>): void => {
    event.preventDefault();

    let errorMessage = "";
    errorMessage += this.validateEmail();
    errorMessage += this.validateUsername();
    errorMessage += this.validatePassword();

    if (errorMessage !== "") {
      alert(errorMessage);
    } else {
      axios
        .post(url, {
          email: this.state.email,
          username: this.state.username,
          password: this.state.password,
          avatar: null
        })
        .then(response => {
          alert("Registration successful!");
          this.props.history.push("login");
        })
        .catch(err => {
          console.log(err.response);
          alert(err.response);
        });
    }
  };

  render() {
    return (
      <div>
        <h1>Register</h1>
        <form className="Register-form" onSubmit={this.handleSubmit}>
          <input
            type="email"
            placeholder="email"
            required
            onChange={this.handleEmail}
          />
          <br />
          <input
            type="text"
            placeholder="username"
            required
            onChange={this.handleUsername}
          />
          <br />
          <input
            type="password"
            placeholder="password"
            required
            onChange={this.handlePassword}
          />
          <br />
          <button className="Register-submit btn btn-secondary" type="submit">
            Register
          </button>
        </form>
      </div>
    );
  }
}

export default withRouter(Register);
