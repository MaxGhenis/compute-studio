import React from "react";
import { Formik, Form, Field, ErrorMessage } from "formik";
import axios from "axios";
import { Button } from "react-bootstrap";
import * as yup from "yup";

import { Message } from "./fields";

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

let LoginSchema = yup.object().shape({
  username: yup.string().required("Username is required."),
  password: yup.string().required("Password is required.")
});

let SignupSchema = yup.object().shape({
  username: yup.string().required("Username is required."),
  email: yup
    .string()
    .email("Must be a valid email address.")
    .required("Email address is required."),
  password1: yup.string().required("Password is required."),
  password2: yup
    .string()
    .oneOf([yup.ref("password1"), null], "Passwords don't match")
    .required("Confirmation password is required.")
});

const tos = (
  <p class="text-muted mt-3">
    By creating an account, you agree to the
    <a href="/terms/">Terms of Service</a>. For more information about Compute
    Studio's privacy practices, see the Compute Studio{" "}
    <a href="/privacy/">Privacy Statement</a>. We'll occasionally send you
    account-related emails.
  </p>
);

export const LoginForm = ({ setAuthStatus }) => (
  <div>
    <Formik
      initialValues={{ username: "", password: "" }}
      validationSchema={LoginSchema}
      onSubmit={(values, actions) => {
        let formdata = new FormData();
        formdata.append("username", values.username);
        formdata.append("password", values.password);
        axios
          .post("/rest-auth/login/", formdata)
          .then(resp => {
            setAuthStatus(true);
          })
          .catch(err => {
            if (err.response.status == 400) {
              actions.setStatus({ errors: err.response.data });
            } else {
              throw err;
            }
          });
      }}
      render={({ handleSubmit, status }) => (
        <Form>
          {status && status.errors && status.errors.non_field_errors ? (
            <div className="alert alert-danger" role="alert">
              {" "}
              {status.errors.non_field_errors}
            </div>
          ) : null}
          <div className="mt-1">
            <label> Username:</label>
            <Field name="username" className="form-control" />
            <ErrorMessage
              name="username"
              render={msg => <Message msg={msg} />}
            />
          </div>
          <div className="mt-1">
            <label> Password: </label>
            <Field name="password" type="password" className="form-control" />
            <ErrorMessage
              name="password"
              render={msg => <Message msg={msg} />}
            />
          </div>
          <Button
            onClick={e => {
              e.preventDefault();
              handleSubmit(e);
            }}
            variant="primary"
            className="mt-2"
          >
            {" "}
            Login{" "}
          </Button>
        </Form>
      )}
    ></Formik>
  </div>
);

export const SignupForm = ({ setAuthStatus }) => (
  <div>
    <Formik
      initialValues={{ username: "", email: "", password1: "", password2: "" }}
      validationSchema={SignupSchema}
      onSubmit={(values, actions) => {
        let formdata = new FormData();
        formdata.append("username", values.username);
        formdata.append("email", values.email);
        formdata.append("password1", values.password1);
        formdata.append("password2", values.password2);
        axios
          .post("/rest-auth/registration/", formdata)
          .then(resp => {
            setAuthStatus(true);
          })
          .catch(err => {
            if (err.response.status == 400) {
              actions.setStatus({ errors: err.response.data });
            } else {
              throw err;
            }
          });
      }}
      render={({ handleSubmit, status }) => (
        <Form>
          {status && status.errors && status.errors.email ? (
            <div className="alert alert-danger" role="alert">
              {" "}
              {status.errors.email}
            </div>
          ) : null}
          {status && status.errors && status.errors.username ? (
            <div className="alert alert-danger" role="alert">
              {" "}
              {status.errors.username}
            </div>
          ) : null}
          {status && status.errors && status.errors.password1 ? (
            <div className="alert alert-danger" role="alert">
              {" "}
              <ul>
                {status.errors.password1.map(msg => (
                  <li>{msg}</li>
                ))}
              </ul>
            </div>
          ) : null}
          <div className="mt-1">
            <label> Username:</label>
            <Field name="username" className="form-control" />
            <ErrorMessage
              name="username"
              render={msg => <Message msg={msg} />}
            />
          </div>
          <div className="mt-1">
            <label> Email:</label>
            <Field name="email" className="form-control" type="email" />
            <ErrorMessage name="email" render={msg => <Message msg={msg} />} />
          </div>
          <div className="mt-1">
            <label> Password: </label>
            <Field name="password1" type="password" className="form-control" />
            <ErrorMessage
              name="password1"
              render={msg => <Message msg={msg} />}
            />
          </div>
          <div className="mt-1">
            <label> Password confirmation: </label>
            <Field name="password2" type="password" className="form-control" />
            <ErrorMessage
              name="password2"
              render={msg => <Message msg={msg} />}
            />
          </div>
          <Button
            onClick={e => {
              e.preventDefault();
              handleSubmit(e);
            }}
            variant="success"
            className="mt-2"
          >
            {" "}
            Signup{" "}
          </Button>
          {tos}
        </Form>
      )}
    ></Formik>
  </div>
);
