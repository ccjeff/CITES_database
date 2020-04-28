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
        d3.csv('/contribution.csv').then(function(df) {
            console.log(df); // [{"Hello": "world"}, …]
            console.log(typeof(df));
            console.log(df[0]);
            console.log(df[0].ISO);
            //获得国家（动物名称）array
            var country_name = new Array();
            var mydata = [];
            var count = 0;
            var myselected = {};
            for(let key in df){
                // console.log(df[key].Name);
                let o = {};
                o = {value: df[key].total_amt_paid, name: df[key].ISO};
                mydata.push(o);
                country_name.push(df[key].ISO);
                myselected[df[key].ISO] = count < 5;
                count = count + 1;
            }
            let myChart = echarts.init(document.getElementById('rose'));
            console.log(mydata);
            console.log(country_name);
            console.log(myselected);
            myChart.setOption({
                title: {
                    text: 'Each Country/Area\'s Fund to CITES',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'country/area',
                    formatter: '{a} <br/>{b} : {c} ({d}%)'
                },
                legend: {
                    type: 'scroll',
                    orient: 'vertical',
                    right: 10,
                    top: 20,
                    bottom: 20,
                    data: country_name,
                    selected: myselected
                },
                series: [
                    {
                        left: 0,
                        rigth: 700,
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

    // componentDidMount(){
    //     console.log(mydata);
//         let myChart = echarts.init(document.getElementById('pie'));
//         myChart.setOption({
//         tooltip: {
//           trigger: 'item',
//           formatter: "{a} <br/>{b}: {c} ({d}%)"
//       },
//     //   legend: {
//     //       orient: 'vertical',
//     //       x: 'right',
//     //       top: 'middle',
//     //       data:['species1','species2']
//     //   },
//       series: [
//           {
//               name:'trade species',
//               type:'pie',
//               radius: ['50%', '70%'],
//               avoidLabelOverlap: false,
//               label: {
//                   normal: {
//                       show: false,
//                       position: 'center'
//                   },
//                   emphasis: {
//                       show: true,
//                       textStyle: {
//                           fontSize: '30',
//                           fontWeight: 'bold'
//                       }
//                   }
//               },
//               labelLine: {
//                   normal: {
//                       show: false
//                   }
//               },
//               data: this.state
//           }
//       ]
//   });
// };

  render() {
      return (
        <div>
            <div id="rose" style={{width: '600px', height:'500px'}}></div>
        </div>
      )
  }
}

export default ContributeRank;
