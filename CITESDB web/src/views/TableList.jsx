/*!

=========================================================
* Light Bootstrap Dashboard React - v1.3.0
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/light-bootstrap-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
import React, { Component } from "react";
import { Grid, Row, Col, Table } from "react-bootstrap";
import { csv } from "d3-fetch";
import {
  FormGroup,
  ControlLabel,
  FormControl
} from "react-bootstrap";

import { Card } from "components/Card/Card.jsx";
import { FormInputs } from "components/FormInputs/FormInputs.jsx";
import { UserCard } from "components/UserCard/UserCard.jsx";
import Button from "components/CustomButton/CustomButton.jsx";

import avatar from "assets/img/faces/face-3.jpg";
import { thArray, tdArray } from "variables/Variables.jsx";



class TableList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      country: 'CN',
      year: '2020',
      creature: 'elephant',
    };

    this.handleButton = this.handleButton.bind(this);
    this.handleChange1 = this.handleChange1.bind(this);
    this.handleChange2 = this.handleChange2.bind(this);
    this.handleChange3 = this.handleChange3.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleButton = event => {
    // console.log(this.props);
    // alert('should be changed with communication with server: ' + this.state.country + this.state.year + this.state.creature);
    console.log(this.state);
    // const w=window.open('about:blank');
    // w.location.href="typography"
    // console.log(event.target.value);
    event.preventDefault();
  };

  handleChange1 = event => {
    console.log("on change");
    this.setState({ ["year"]: event.target.value });
  }
  handleChange2 = event => {
    console.log("on change");
    
    this.setState({ ["creature"]: event.target.value });
  }
  handleChange3 = event => {
    console.log('handle3');
    this.setState({ ["country"]: event.target.value });
  }

  handleSubmit(event) {
    alert('Your favorite flavor is: ' + this.state.value);
    event.preventDefault();
  }
  
  render() {
  
    return (
      <div className="content">
        {/* <form onSubmit={this.handleSubmit}> */}
        {/* <label>
          Choose the country for query 
          <select value={this.state.value} onChange={this.handleChange}>
            <option value="gg">Google</option>
            <option value="rn">Runoob</option>
            <option value="tb">Taobao</option>
            <option value="fb">Facebook</option>
          </select>

        </label>
        <input type="submit" value="submit" /> */}
      {/* </form>   */}

      
      <form onSubmit={this.handleButton}>
        <Grid fluid>
        <Row>
            <Col md={8}>
              <Card
                title="Search with year: "
                content={
                  <form onChange = {this.handleChange1}>
                    <FormInputs
                      name = "formValue"
                      ncols={["col-md-5"]}
                      properties={[
                        {
                          label: "Year",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "2020",
                          defaultValue: "2020",
                        }
                      ]}
                    />
                    <div className="clearfix" />
                  </form>
                }
              />
              <Card
                title="Search with creature name: "
                content={
                  <form onChange = {this.handleChange2}>
                    <FormInputs
                      name = "formValue"
                      ncols={["col-md-5"]}
                      properties={[
                        
                        {
                          label: "Creature Name",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "Elephant",
                          defaultValue: "Elephant"
                        }
                      ]}

                    />
                    

                    <div className="clearfix" />
                  </form>
                }
              />
              <Card
                title="Search with country: "
                content={
                  <form onChange = {this.handleChange3}>
                    <FormInputs
                      name = "formValue"
                      ncols={["col-md-5"]}
                      properties={[
                        {
                          label: "Country",
                          type: "text",
                          bsClass: "form-control",
                          placeholder: "CN",
                          defaultValue: "CN"
                        }
                      ]}

                    />
                    

                    <div className="clearfix" />
                  </form>
                }
              />
              
            </Col>
          </Row>
          
          <Button bsStyle="info" pullRight fill type="submit">
                Search
          </Button>
        </Grid>
        </form>
      </div>
    );
  }
}

export default TableList;
