<template>
  <div class="Home" align="center">
    <!--    <div align="right">-->
    <!--      <div style="width: 300px">-->
    <!--        <h1 style="text-align: right">每个人都有属于自己的一片森林，</h1>-->
    <!--        <h1 style="text-align: right">迷失的人迷失了， </h1>-->
    <!--        <h1 style="text-align: right">相逢的人会再相逢。</h1>-->
    <!--      </div>-->
    <!--    </div>-->
<!--    <div style="width: 300px">-->
<!--    </div>-->
    <el-row :gutter="10">
      <el-col :offset="6" :xs="24" :xl="12" :lg="12" :sm="24" :md="12">

        <!--          <div style="overflow: auto; height: 300px; width: 100%;">-->
        <!--            <ul style="list-style: none">-->
        <!--              <li v-for="m in mp3.data">-->
        <!--                <el-link type="primany" @click="play(m.url, m.name)" style="margin: 10px">{{ m.name }}</el-link>-->
        <!--              </li>-->
        <!--            </ul>-->
        <!--          </div>-->
        <!--          <div>-->
        <!--&lt;!&ndash;            <router-link to="/echarts_dic/left_pie_echarts"></router-link>&ndash;&gt;-->
        <!--            <left_pie_echarts></left_pie_echarts>-->
        <!--          </div>-->

        <!--            <left_pie_echarts></left_pie_echarts>-->
        <!--            <router-link to="/echarts_dic/left_pie_echarts">Left_Pie</router-link>-->
        <!--            <router-view></router-view>-->
        <left_pie_echarts></left_pie_echarts>

      </el-col>

<!--      <el-col :xs="24" :xl="12" :lg="12" :sm="24" :md="12">-->
<!--        <right_pie_echarts></right_pie_echarts>-->
<!--      </el-col>-->
    </el-row>

  </div>
</template>

<script>
import Status from '@/components/Status'
import left_pie_echarts from '@/components/echarts_dic/left_pie_echarts'
import right_pie_echarts from '@/components/echarts_dic/right_pie_echarts'

export default {
  name: 'Home',
  components: {
    Status,
    left_pie_echarts,
    right_pie_echarts
  },
  data () {
    return {
      playm: false,
      mp3: '',
      audio: '',
      name: '',
    }
  },

  methods: {
    play: function (url, name) {
      console.log(name, url)
      this.audio = url
      this.name = name
      this.playm = true
    }

  },
  created () {
    // this.$http.get('apis/get_info?mp3=yep')
    //   .then(response => {
    //     this.mp3 = response.data
    //   }, error => {
    //     console.log('mp3 error')
    //   })
    fetch('apis/get_info?mp3=yep', {
      method: 'get',
    })
      .then(response => {
        return response.json()
      })
      .then(data => {
        this.mp3 = data
      })
  }
}
</script>

<style scoped>
.grid_content {
  background: #0b2e13;
  height: auto;
  width: auto;
}
</style>
