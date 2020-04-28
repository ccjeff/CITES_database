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
//import echarts from 'echarts/lib/echarts';
import 'echarts/lib/chart/pie';
import React, { Component } from "react";
import ChartistGraph from "react-chartist";
import { Grid, Row, Col } from "react-bootstrap";
import { ComposableMap } from "react-simple-maps";
import MapChart from "./MapChart.jsx";
import PieChart from "./PieChart.jsx";
import TermHis from "./TermHis.jsx";
import ContributeRank from "./ContributeRank.jsx";
import CreatureTreeMap from "./CreatureTreeMap.jsx";

import { Card } from "components/Card/Card.jsx";
import { StatsCard } from "components/StatsCard/StatsCard.jsx";
import { Tasks } from "components/Tasks/Tasks.jsx";
import {
  dataPie,
  legendPie,
  dataSales,
  optionsSales,
  responsiveSales,
  legendSales,
  dataBar,
  optionsBar,
  responsiveBar,
  legendBar
} from "variables/Variables.jsx";

class Dashboard extends Component {
  createLegend(json) {
    var legend = [];
    for (var i = 0; i < json["names"].length; i++) {
      var type = "fa fa-circle text-" + json["types"][i];
      legend.push(<i className={type} key={i} />);
      legend.push(" ");
      legend.push(json["names"][i]);
    }
    return legend;
  }
  render() {
    return (
      <div className="content">
         <h1>
          <p className="category"></p> CITES: Global Wildlife Trading Information{" "}
        </h1>
        <div>
          <MapChart />
        </div>

        <Grid fluid>
          <Row>
            <Col lg={3} sm={6}>
              <StatsCard
                bigIcon={<i className="pe-7s-server text-warning" />}
                statsText="Highest Import"
                statsValue="US of America"
                statsIcon={<i className="fa fa-refresh" />}
                statsIconText="Updated now"
              />
            </Col>
            <Col lg={3} sm={6}>
              <StatsCard
                bigIcon={<i className="pe-7s-wallet text-success" />}
                statsText="Highest Export"
                statsValue="Indonesia"
                statsIcon={<i className="fa fa-calendar-o" />}
                statsIconText="Updated now"
              />
            </Col>
            <Col lg={3} sm={6}>
              <StatsCard
                bigIcon={<i className="pe-7s-graph1 text-danger" />}
                statsText="Lowest Import"
                statsValue="Norfolk Island"
                statsIcon={<i className="fa fa-clock-o" />}
                statsIconText="Updated now"
              />
            </Col>
            <Col lg={3} sm={6}>
              <StatsCard
                bigIcon={<i className="fa fa-twitter text-info" />}
                statsText="Lowest Export"
                statsValue="Christmas Island"
                statsIcon={<i className="fa fa-refresh" />}
                statsIconText="Updated now"
              />
            </Col>
          </Row>
          <Row>
            <Col md={7}>
                <div style={{
                            display: 'inline-block',
                            width: '208px',
                            height: '100%',
                            background: 'url("${thumb[0]}") center center / cover no-repeat',
                        }}>
                  {<CreatureTreeMap />}
                </div>
            </Col>
            <Col md={4}>
              <div>
                <PieChart />
              </div>
            </Col>
          </Row>
          <Row>
            <Col md={4}>
              <div>
                <ContributeRank />
              </div>
            </Col>
            
            <Col md={4}>
              <div>
                <TermHis />
              </div>
            </Col>
          </Row>
        </Grid>
      </div>
    );
  }
}

export default Dashboard;
