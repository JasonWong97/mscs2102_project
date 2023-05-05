import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import AddBlog from '@/components/AddBlog'
import About from '@/components/About'
import BlogList from '@/components/BlogList'
import Face from '@/components/Face'
import Login from '@/components/User/Login'
import Register from '@/components/User/Register'
import ROOT from '@/components/User/ROOT'
import left_pie_echarts from '@/components/echarts_dic/left_pie_echarts'
import right_pie_echarts from '@/components/echarts_dic/right_pie_echarts'
import Candlestick_Chart from '@/components/echarts_dic/Candlestick_Chart'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {path: '/', name: 'Home', component: Home},  // 主页
    {path: '/candle', name: 'Candle', component: AddBlog},   // 添加blog
    {path: '/about', name: 'About', component: About},   // 关于
    {path: '/bloglist', name: 'BlogList', component: BlogList},  // 显示blog信息
    {path: '/face', name: 'Face', component: Face},   // 人脸识别
    {path: '/user/login', name: 'Login', component: Login},   // 登录
    {path: '/user/register', name: 'Register', component: Register},   // 注册
    {path: '/user/root', name: 'ROOT', component: ROOT},   // 注册
    {path: '/echarts_dic/left_pie_echarts', name: 'left_pie_echarts', component: left_pie_echarts},
    {path: '/echarts_dic/right_pie_echarts', name: 'right_pie_echarts', component: right_pie_echarts},
    {path: '/echarts_dic/Candlestick_Chart', name: 'Candlestick_Chart', component: Candlestick_Chart},
  ]
})
