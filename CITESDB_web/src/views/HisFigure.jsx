import React, { Component } from 'react';

import echarts from 'echarts';
import * as d3 from "d3-fetch";

import  'echarts/lib/chart/bar';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import 'echarts/lib/component/legend';
import 'echarts/lib/component/markPoint';

class HisFigure extends Component {
    constructor(props){
        super(props);
        d3.csv('/query_data/country_table.csv').then(function(df) {
            var xAxis = [];
            var yAxis = [];
            var myselected = {};
            var count = 0;
            for(let key in df){
                xAxis.push(df[key].trade_count);
                yAxis.push(df[key].country_and_area);
                myselected[df[key].country_and_area] = count < 7;
                count ++
            }
            console.log(xAxis);
            console.log(yAxis);
            console.log(myselected);
            // var myselected = {};
            // // console.log(count_species);
            // var count = 0;
            // for (let i in count_species){
            //     // console.log(i);
            //     myselected[i] = count < 7;
            //     count = count + 1;
            // }
            let myChart = echarts.init(document.getElementById('bar'));
            // console.log(mydata);
            // console.log(species_legend);
            // console.log(myselected);
            myChart.setOption({
            title: {
                text: 'Country Table',
                left: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                type: 'scroll',
                orient: 'vertical',
                right: 0,
                top: 20,
                bottom: 20,
                data: yAxis,
        
                selected: myselected
            },
            dataZoom : [
                {
                    type: 'slider',
                    show: true,
                    start: 94,
                    end: 100,
                    handleSize: 8
                },
                {
                    type: 'inside',
                    start: 94,
                    end: 100
                },
                {
                    type: 'slider',
                    show: true,
                    yAxisIndex: 0,
                    filterMode: 'empty',
                    width: 12,
                    height: '70%',
                    handleSize: 8,
                    showDataShadow: false,
                    left: '93%'
                }
            ],
                xAxis: {
                    type: 'category',
                    data: yAxis
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    data: xAxis,
                    type: 'bar',
                    showBackground: true,
                    backgroundStyle: {
                        color: 'rgba(220, 220, 220, 0.8)'
                    }
                }]
            });
        });
    };


  render() {

        return (
            <div>
                <div id="bar" style={{width: '1200px', height:'500px'}}></div>
            </div>
            )

  }
}

export default HisFigure;
