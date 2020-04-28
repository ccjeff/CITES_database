import React, { Component } from 'react';

import echarts from 'echarts';
import * as d3 from "d3-fetch";

import  'echarts/lib/chart/line';
// import  'echarts/lib/chart/pie';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import 'echarts/lib/component/legend';
import 'echarts/lib/component/markPoint';


class LineFigure extends Component {
    constructor(props){
        super(props);
        d3.csv('/query_data/year_table.csv').then(function(df) {
            var xdata = [];
            var ydata = [];
            for(let key in df){
                // console.log(df[key].country_name);
                let o = {};
                o = {
                    name: df[key].country_name,
                    value: df[key].num_creatures_originated
                }
                xdata.push(df[key].year);
                ydata.push(df[key].trade_count)
            }
            let myChart = echarts.init(document.getElementById('treemap'));

            var option = {
                title : {
                    text: 'Years Table',
                    top: 5,
                    left: 'center',
                    backgroundColor: 'rgb(243,243,243)',
                    borderRadius: [5, 5, 0, 0]
                },
                tooltip : {
                    trigger: 'item',
                    formatter: "{b}: {c}"
                },
                toolbox: {
                    show : true,
                    feature : {
                        mark : {show: true},
                        dataView : {show: true, readOnly: false},
                        restore : {show: true},
                        saveAsImage : {show: true}
                    }
                },
                calculable : false,

                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: xdata
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: ydata,
                    type: 'line',
                    areaStyle: {}
                }]

                
            };
            myChart.setOption(option);
        });
    };

  render() {
      return (
        <div>
            <div id="treemap" style={{width: '1200px', height:'500px'}}></div>
        </div>
      )
  }
}

export default LineFigure;
