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
import { thArray, tdArray } from "variables/Variables.jsx";

import HisFigure from "./HisFigure.jsx";
import PieFigure from "./PieFigure.jsx";
import LineFigure from "./LineFigure.jsx";
import Card from "components/Card/Card.jsx";
import * as d3 from "d3-fetch";

// import { notifyServerFinished } from './socket';



class Typography extends Component {
  constructor(props){
    super(props);

    this.state = {
      thArray: [],
      tdArray: []
    };


    // d3.csv('/query_data/all_table.csv').then(function(df) {
    //     console.log(df); // [{"Hello": "world"}, …]
    //     console.log(df[0]);
    //     var thead = [];
    //     var tcontest = [];
    //     var count = 0;
    //     for(let key in df){
    //         // console.log(df[key].Name);
    //         if (count == 0){
    //             thead.push(df[key]);
    //         }
    //         else{
    //             tcontest.push(df[key]);
    //         }
    //         count = count + 1;
    //     }
    //     this.setState({ ["thArray"]: thead });
    //     this.setState({["tdArray"]: tcontest});
    //     console.log("fsa", this.state.thArray);
    //     console.log("fndajk",this.state.tdArray);
    // });
  }

  
  render() {
    return (
      <div className="content">
        <Grid fulid>
          <Row>
            <Col md={12}>
              <Card
                  title="The Relationship Table Between Creature, Year and Country"
                  category="Selected Part of the Data Due to Large Amount"
                  ctTableFullWidth
                  ctTableResponsive
                  content={
                    <Table striped hover>
                      <thead>
                        <tr>
                          {thArray.map((prop, key) => {
                            return <th key={key}>{prop}</th>;
                          })}
                        </tr>
                      </thead>
                      <tbody>
                        {tdArray.map((prop, key) => {
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
            </Col>
          </Row>
          <Row>
            <Col md={12}>
                  <div>
                    {<HisFigure />}
                  </div>
              </Col>
          </Row>
          <Row>
              <Col md={12}>
                <div>
                  <PieFigure />
                </div>
              </Col>
          </Row>
          <Col md={6} sm={24}></Col>
          <Col md={6} sm={24}></Col>
          <Row>
            <Col md={12}>
                  <div>
                    {<LineFigure />}
                  </div>
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default Typography;
