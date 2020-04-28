import React, { Component } from 'react';

import echarts from 'echarts';
import * as d3 from "d3-fetch";

import  'echarts/lib/chart/bar';
import  'echarts/lib/chart/pie';
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';
import 'echarts/lib/component/legend';
import 'echarts/lib/component/markPoint';

// var mydata;

// function csvJSON(csvpath){
//     // var exec = require('child_process').exec; 
//     // exec('python test.py', function(error, stdout, stderr){
//     //     if (error){
//     //         console.info("stderr: "+stderr);
//     //     }
//     //     console.log('exec '+stdout)
//     //     var json = JSON.parse(stdout);
//     //     console.log(json);
//     // });
//     d3.csv(csvpath).then(function(df) {
//         console.log(df); // [{"Hello": "world"}, …]
//         console.log(typeof(df));
//         console.log(df[0]);
//         console.log(df[0].ISO3);
//         //获得国家（动物名称）array
//         var species_arr = new Array();
//         for(let key in df){
//             // console.log(df[key].Name);
//             species_arr.push(df[key].Name);
//         }
//         console.log(species_arr);
//         var count_species = {}; // for counted species name
//         for(var i=0,v,l = species_arr.length; v = species_arr[i],i<l; i++)
//         {
//             var rv = /^([a-z]+)(?:.+?(\d+))?/i.exec(v);
//             if (!count_species[rv[1]])
//                 count_species[rv[1]] = 0;
//             count_species[rv[1]] += rv[2] ? parseInt(rv[2], 10) : 1;
//         }
//         console.log(count_species);
//         mydata = count_species;
//         return count_species;
//     });
// //   var result = [];
// //   var headers=lines[0].split(",");
// //   for(var i=1;i<lines.length;i++){
// //       var obj = {};
// //       var currentline=lines[i].split(",");
// //       for(var j=0;j<headers.length;j++){
// //           obj[headers[j]] = currentline[j];
// //       }
// //       result.push(obj);
// //   }
// //   console.log(JSON.stringify(result));
// //   return JSON.stringify(result);
//     // return 0;
// }

// function getData(){
//   var data = csvJSON('/recorded_creature.csv');
//   console.log('getData:'+data);
//   return data;
// }

// csvJSON('/recorded_creature.csv');
// console.log(mydata);

class Tradepie extends Component {
    constructor(props){
        super(props);
        d3.csv('/recorded_creature.csv').then(function(df) {
            var species_arr = new Array();
            for(let key in df){
                // console.log(df[key].Name);
                species_arr.push(df[key].Taxon);
            }
            // console.log(species_arr);
            var count_species = {}; // for counted species name
            for(var i=0,v,l = species_arr.length; v = species_arr[i],i<l; i++)
            {
                var rv = /^([a-z]+)(?:.+?(\d+))?/i.exec(v);
                if (!count_species[rv[1]])
                    count_species[rv[1]] = 0;
                count_species[rv[1]] += rv[2] ? parseInt(rv[2], 10) : 1;
            }
            var mydata = [];
            var species_legend = [];
            var myselected = {};
            // console.log(count_species);
            var count = 0;
            for (let i in count_species){
                let o = {};
                o = {value: count_species[i], name: i};
                mydata.push(o);
                species_legend.push(i);
                // console.log(i);
                myselected[i] = count < 5;
                count = count + 1;
            }
            let myChart = echarts.init(document.getElementById('pie'));
            // console.log(mydata);
            // console.log(species_legend);
            // console.log(myselected);
            myChart.setOption({
            title: {
                text: 'Each Specie\'s Percentage in Trade',
                left: 'center'
            },
            tooltip: {
                trigger: 'item',
                formatter: "{a} <br/>{b}: {c} ({d}%)"
            },
            legend: {
                type: 'scroll',
                orient: 'vertical',
                right: 10,
                top: 20,
                bottom: 20,
                data: species_legend,
        
                selected: myselected
            },
            series: [
                    {
                        name: 'Species Name',
                        type: 'pie',
                        radius: '55%',
                        center: ['40%', '50%'],
                        data: mydata,
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
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
            <div id="pie" style={{width: '600px', height:'500px'}}></div>
        </div>
      )
  }
}

export default Tradepie;
