<template>
  <div id="Candlestick_Chart" v-loading="loading">
    <el-card style="min-height: 200px; max-height: 800px; ">
      <div slot="header">
        Candlestick Chart
      </div>
<div>
  <el-select v-model="value" placeholder="请选择" @change="get_history_data(value)">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
</div>
      <div>
        <div id="main3" style="width: 600px;height:500px;"></div>
      </div>
    </el-card>
  </div>
</template>

<script>
import * as echarts from 'echarts/core';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from 'echarts/components';
import {
  PieChart
} from 'echarts/charts';
import {
  CanvasRenderer
} from 'echarts/renderers';

export default {
  name: 'Candlestick_Chart',
  data() {
    return {
      options: [{
        value: 'BTC',
        label: 'BTC'
      }, {
        value: 'ETH',
        label: 'ETH'
      }],
      value: '',
      history_data:''
    }
  },
  methods: {
    get_history_data (v) {
      this.$http.post('apis/get_history_data',
        v
      )
        .then(response => {
          this.history_data=response.data.history_data
          // console.log(response)
          console.log(this.history_data)
          this.myEcharts();

        })
    },

    myEcharts () {
      echarts.use(
        [TitleComponent, TooltipComponent, LegendComponent, PieChart, CanvasRenderer]
      );
      var chartDom = document.getElementById('main3');
      var myChart = this.$echarts.init(chartDom);
      var option;

      var upColor = '#ec0000';
      var upBorderColor = '#8A0000';
      var downColor = '#00da3c';
      var downBorderColor = '#008F28';

      var dataCount = 2e2;
      var data = generateOHLC(this.history_data);
      console.log(data)
      console.log(this.history_data)
      var option = {
        dataset: {
          source: data
        },
        // title: {
        //   text: 'Data Amount: ' + echarts.format.addCommas(dataCount)
        // },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'line'
          }
        },
        toolbox: {
          feature: {
            dataZoom: {
              yAxisIndex: false
            },
          }
        },
        grid: [
          {
            left: '10%',
            right: '10%',
            bottom: 200
          },
          {
            left: '10%',
            right: '10%',
            height: 80,
            bottom: 80
          }
        ],
        xAxis: [
          {
            type: 'category',
            scale: true,
            boundaryGap: false,
            // inverse: true,
            axisLine: {onZero: false},
            splitLine: {show: false},
            splitNumber: 20,
            min: 'dataMin',
            max: 'dataMax'
          },
          {
            type: 'category',
            gridIndex: 1,
            scale: true,
            boundaryGap: false,
            axisLine: {onZero: false},
            axisTick: {show: false},
            splitLine: {show: false},
            axisLabel: {show: false},
            splitNumber: 20,
            min: 'dataMin',
            max: 'dataMax'
          }
        ],
        yAxis: [
          {
            scale: true,
            splitArea: {
              show: true
            }
          },
          {
            scale: true,
            gridIndex: 1,
            splitNumber: 2,
            axisLabel: {show: false},
            axisLine: {show: false},
            axisTick: {show: false},
            splitLine: {show: false}
          }
        ],
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0, 1],
            start: 10,
            end: 100
          },
          {
            show: true,
            xAxisIndex: [0, 1],
            type: 'slider',
            bottom: 10,
            start: 10,
            end: 100
          }
        ],
        visualMap: {
          show: false,
          seriesIndex: 1,
          dimension: 6,
          pieces: [{
            value: 1,
            color: upColor
          }, {
            value: -1,
            color: downColor
          }]
        },
        series: [
          {
            type: 'candlestick',
            itemStyle: {
              color: upColor,
              color0: downColor,
              borderColor: upBorderColor,
              borderColor0: downBorderColor
            },
            encode: {
              x: 0,
              y: [1, 4, 3, 2]
            }
          },
          {
            name: 'Volumn',
            type: 'bar',
            xAxisIndex: 1,
            yAxisIndex: 1,
            itemStyle: {
              color: '#7fbe9e'
            },
            large: true,
            encode: {
              x: 0,
              y: 5
            }
          }
        ]
      };

      function generateOHLC(history_data) {
        var data = [];
        var len=history_data.length;


        for (var i = 0; i < len; i++) {

          // ['open', 'close', 'lowest', 'highest', 'volumn']
          // [1, 4, 3, 2]
          data[i] = [
            history_data[i]['time'],
            history_data[i]['open'].toFixed(2), // open
            history_data[i]['high'].toFixed(2), // highest
            history_data[i]['low'].toFixed(2), // lowest
            history_data[i]['close'].toFixed(2),  // close
            history_data[i]['volume'].toFixed(0),
            getSign(history_data[i]['open'],history_data[i]['close']) // sign
          ];
          console.log(data[i])
        }

        return data;

        function getSign(openVal, closeVal ) {
          var sign;
          if (openVal > closeVal) {
            sign = -1;
          }
          else if (openVal < closeVal) {
            sign = 1;
          }
          else {
            sign = 1;
          }

          return sign;
        }
      }

      option && myChart.setOption(option);
    }
  },
  mounted() {
    this.myEcharts();
  }
}

</script>

<style scoped>

</style>
