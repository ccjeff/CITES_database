import React, { Component } from 'react';

import echarts from 'echarts';
import * as d3 from "d3-fetch";

import  'echarts/lib/chart/bar';
import  'echarts/lib/chart/pie';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import 'echarts/lib/component/legend';
import 'echarts/lib/component/markPoint';


class ContributeRank extends Component {
    constructor(props){
        super(props);
        d3.csv('/query_data/creature_table.csv').then(function(df) {
            // console.log(df); // [{"Hello": "world"}, …]
            // console.log(typeof(df));
            // console.log(df[0]);
            // console.log(df[0].name);
            //获得国家（动物名称）array
            var species_name = new Array();
            var mydata = [];
            var count = 0;
            var myselected = {};
            var target_year;
            for(let key in df){
                // console.log(df[key].Name);
                let o = {};
                o = {value: df[key].trade_count, name: df[key].name};
                mydata.push(o);
                species_name.push(df[key].name);
                myselected[df[key].name] = count < 5;
                target_year = df[key].year;
                count = count + 1;
            }
            let myChart = echarts.init(document.getElementById('rose'));
            console.log(mydata);
            console.log(species_name);
            console.log(myselected);
            myChart.setOption({
                title: {
                    text: 'Creature Table',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'country/area',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                legend: {
                    type: 'scroll',
                    orient: 'vertical',
                    right: 90,
                    // left: 0,
                    top: 20,
                    bottom: 20,
                    data: species_name,
                    selected: myselected
                },
                series: [
                    {
                        left: 120,
                        rigth: 0,
                        type: 'pie',
                        radius: [30, 110],
                        center: ['30%', '50%'],
                        roseType: 'area',
                        data: mydata,
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                    }   }
                ]
            });
        });
    };


  render() {
      return (
        <div>
            <div id="rose" style={{width: '1200px', height:'500px'}}></div>
        </div>
      )
  }
}

export default ContributeRank;
