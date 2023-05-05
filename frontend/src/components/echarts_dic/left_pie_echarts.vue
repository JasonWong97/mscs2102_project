<template>


  <div id="left_pie_echarts" v-loading="loading">
    <el-card style="min-height: 200px; max-height: 800px; ">
      <div slot="header">
        Sentiment Index
      </div>

      <div>
        <div id="main" style="width: 600px;height:500px;"></div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'left_pie_echarts',
  data () {
    return {
      timer: '',
      value: 0,
      BTC: 0,
      ETH: 0,
      BNB: 0,
      ADA: 0,
      USDT: 0

    }
  },
  methods: {
    myEcharts () {
      var chartDom = document.getElementById('main')
      var myChart = this.$echarts.init(chartDom)
      var option

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
            name: 'Positive',
            type: 'pie',
            radius: ['40%', '70%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            // label: {
            //   show: false,
            //   position: 'center'
            // },
            emphasis: {
              label: {
                show: true,
                fontSize: '20',
                fontWeight: 'bold',
                formatter: '{b}\n{c}',
              }
            },
            // labelLine: {
            //   show: false
            // },
            data: [
              {value: this.BTC, name: 'BTC'},
              {value: this.ETH, name: 'ETH'},
              {value: this.BNB, name: 'BNB'},
              {value: this.ADA, name: 'ADA'},
              {value: this.USDT, name: 'USDT'}
            ]
          }
        ]
      }

      option && myChart.setOption(option)
    },
    get_sentiment_data () {
      this.$http.get('apis/get_sentiment_data')
        .then(response => {
          this.BTC = response.data.BTC
          this.ETH = response.data.ETH
          this.BNB = response.data.BNB
          this.ADA = response.data.ADA
          this.USDT = response.data.USDT
          console.log(this.BTC)
          console.log(response)
        })
    },

    // nowTimes() {
    //   this.get_sentiment_data;
    //   this.timer = setTimeout(this.nowTimes, 3000);
    // }

  },
  mounted () {
    this.timer = setInterval(this.get_sentiment_data, 5000)
    this.timer = setInterval(this.myEcharts, 5000)
    this.myEcharts()

  },

  beforeDestroy () {
    clearInterval(this.timer)
  }
}
</script>

<style>

</style>
