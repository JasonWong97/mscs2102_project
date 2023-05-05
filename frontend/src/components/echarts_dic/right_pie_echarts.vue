<template>


  <div id="right_pie_echarts" v-loading="loading">
    <el-card style="min-height: 200px; max-height: 800px; ">
      <div slot="header">
        Negative Sentiment
      </div>

      <div>
        <div id="main2" style="width: 600px;height:500px;"></div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'right_pie_echarts',

  methods: {
    myEcharts () {
      var chartDom = document.getElementById('main2');
      var myChart = this.$echarts.init(chartDom);
      var option;

      option = {
        tooltip: {
          trigger: 'item'
        },
        title: {
          left: 'center'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: 'Negative',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: 0.8, name: 'BTC'},
              {value: 0.1, name: 'ETH'},
              {value: 0.23, name: 'BNB'},
              {value: 0.4, name: 'ADA'},
              {value: 0.9, name: 'USDT'}
            ]
          }
        ]
      };

      option && myChart.setOption(option);
    }
  },
  mounted() {
    this.myEcharts();
  }
}
</script>

<style>

</style>
