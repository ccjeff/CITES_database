import React, { Component } from 'react';

import echarts from 'echarts';
import * as d3 from "d3-fetch";

import  'echarts/lib/chart/treemap';
// import  'echarts/lib/chart/pie';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import 'echarts/lib/component/legend';
import 'echarts/lib/component/markPoint';


class CreatureTreeMap extends Component {
    constructor(props){
        super(props);
        d3.csv('/creature_amt.csv').then(function(df) {
            // console.log(df); // [{"Hello": "world"}, …]
            // console.log(typeof(df));
            // console.log(df[0]);
            // console.log(df[0].ISO3);
            //获得国家（动物名称）array
            // var country_name = new Array();
            var mydata = [];
            var country_legend = [];
            var myselected = {};
            var count = 0;
            for(let key in df){
                // console.log(df[key].country_name);
                let o = {};
                o = {
                    name: df[key].country_name,
                    value: df[key].num_creatures_originated
                }
                country_legend.push(df[key].country_name);
                mydata.push(o);
                myselected[df[key].country_name] = count < 20;
                count++;
            }
            let myChart = echarts.init(document.getElementById('treemap'));
            myChart.showLoading();
            myChart.hideLoading();
            console.log(mydata);
            // console.log(species_legend);
            console.log(myselected);
            var option = {
                title : {
                    text: 'Creature Amount for Each Country',
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
                series : [
                    {
                        name:'creature amount',
                        type:'treemap',
                        itemStyle: {
                            normal: {
                                label: {
                                    show: true,
                                    formatter: "{b}"
                                },
                                borderWidth: 1
                            },
                            emphasis: {
                                label: {
                                    show: true
                                }
                            }
                        },
                        data: mydata
                    }
                ]
            };
            myChart.setOption(option);
        });
    };

  render() {
      return (
        <div>
            <div id="treemap" style={{width: '900px', height:'500px'}}></div>
        </div>
      )
  }
}

export default CreatureTreeMap;
