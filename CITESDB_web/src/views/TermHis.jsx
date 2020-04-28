import React, { Component } from 'react';
import * as d3 from "d3-fetch";
// 引入 ECharts 主模块
import echarts from 'echarts/lib/echarts';
import 'echarts-gl';
// 引入柱状图
import  'echarts/lib/chart/bar';
// 引入提示框和标题组件
import 'echarts/lib/component/tooltip';
import 'echarts/lib/component/title';

class TermHis extends Component {
    constructor(props){
        super(props);
        d3.csv('/termRank.csv').then(function(df) {
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
                let o = [df[key].scientific_name, df[key].TermTotalTrade, df[key].term];
                // country_legend.push(df[key].country_name);
                mydata.push(o);
                // myselected[df[key].country_name] = count < 20;
                // count++;
            }
            console.log(mydata);
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('main'));
        // 绘制图表
        myChart.setOption({
            // title: { text: 'Top Ten Trade Term', padding:[5,10,5,230], },
            // tooltip: {},
            // xAxis: {},
            // yAxis: {data: ['live', 'leatherproducts', 'skins','trophies', 'raw_corals',                   
            // 'shoes', 'specimens', 'leather_products(large)', 'roots', 'garments']},
            // grid: {
            //     left: '10%',
            //     right: '4%',
            //     containLabel: true,
            //     x:130
            // },
            // series: [{
            //     name: 'Value',
            //     type: 'bar',
            //     data: [338234, 238153, 34896, 22815, 19434, 15972, 13601, 11137, 8519, 8203]
            // }]
            title: {
                text: 'The Relationship Bewteen Species, Term and Amounts', padding:[5,10,5,490]
            },
            xAxis3D:{
                type: 'category'
            },
            yAxis3D:{
               type: 'value'
            },
            zAxis3D : {
               type: 'category'
            },
            grid3D:{},
            series : [
                {
                    type: 'scatter3D', //设置图表类型为3d散点图
                    data: mydata
                }]
        });
    });
}
    render() {
        return (
            <div id="main" style={{ width: 1511, height: 545 }}></div>
        );
    }
}

export default TermHis;
