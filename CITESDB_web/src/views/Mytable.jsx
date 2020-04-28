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
import * as d3 from "d3-fetch";
import {
  FormGroup,
  ControlLabel,
  FormControl
} from "react-bootstrap";

import { Card } from "components/Card/Card.jsx";
import { FormInputs } from "components/FormInputs/FormInputs.jsx";
import { UserCard } from "components/UserCard/UserCard.jsx";
import Button from "components/CustomButton/CustomButton.jsx";
// import { subscribeToTimer, sendToServer, notifyServerFinished } from './socket';
import avatar from "assets/img/faces/face-3.jpg";
import { thArray, tdArray } from "variables/Variables.jsx";
import axios from 'axios' ;



class Mytable extends Component {
  constructor(props) {
    super(props);
    
    this.state = {
      thArray: [],
      tdArray: []
    };


    d3.csv('/query_data/all_table.csv').then(function(df) {
        console.log(df); // [{"Hello": "world"}, …]
        console.log(df[0]);
        var thead = [];
        var tcontest = [];
        var count = 0;
        for(let key in df){
            // console.log(df[key].Name);
            if (count == 0){
                thead.push(df[key]);
            }
            else{
                tcontest.push(df[key]);
            }
            count = count + 1;
        }
        this.setState({ thArray: thead });
        this.setState({tdArray: tcontest})
        console.log("fsa", thArray);
        console.log("fndajk",tdArray);
    });
  };

  
  render() {
    return (
            <Card
                title="Striped Table with Hover"
                category="Here is a subtitle for this table"
                ctTableFullWidth
                ctTableResponsive
                content={
                  <Table striped hover>
                    <thead>
                      <tr>
                        {this.state.thArray.map((prop, key) => {
                          return <th key={key}>{prop}</th>;
                        })}
                      </tr>
                    </thead>
                    <tbody>
                      {this.state.tdArray.map((prop, key) => {
                        return (
                          <tr key={key}>
                            {prop.map((prop, key) => {
                              return <td key={key}>{prop}</td>;
                            })}
                          </tr>
                        );
                      })}
                    </tbody>
                  </Table>
                }
            />
    )
  }
}

export default Mytable;
