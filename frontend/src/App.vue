<template>
  <div id="app">
    <el-container>
      <!--  header -->
      <el-header>
        <el-col :xs="24" :sm="24">
          <el-menu :default-active="$route.path" class="el-menu-vertical-demo" mode="horizontal" router>
            <el-menu-item class="hidden-sm-and-down"><img src="./assets/logo.png" style="width: 30px; height: 30px;"></el-menu-item>
            <el-menu-item index="/"><i class="el-icon-house"></i><span class="hidden-sm-and-down">Home</span></el-menu-item>
            <el-menu-item index="/candle" class="hidden-sm-and-down"><i class="el-icon-edit"></i><span class="hidden-sm-and-down">Candlestick Chart</span></el-menu-item>
            <el-menu-item index="/bloglist"><i class="el-icon-tickets"></i><span class="hidden-sm-and-down">My Cryptocurrency</span></el-menu-item>
<!--            <el-menu-item index="/face"><i class="el-icon-camera-solid"></i><span class="hidden-sm-and-down">FaceRecogntion</span></el-menu-item>-->
            <el-submenu index="1">
              <template slot="title"><i class="el-icon-user"></i><span class="hidden-sm-and-down">UserHome</span></template>
              <div>
                <el-menu-item index="/user/login" v-if="!islogin">Login</el-menu-item>
                <el-menu-item index="/user/register" v-if="!islogin">Register</el-menu-item>
                <div v-else>
                  <el-menu-item index="/user/root">{{ username }}</el-menu-item>
                  <el-menu-item @click="logout">Logout</el-menu-item>
                </div>

              </div>
            </el-submenu>
          </el-menu>
        </el-col>
      </el-header>

      <!--        导航栏-->
      <el-main :xs="24">

          <router-view></router-view>

      </el-main>

      <el-footer>
        <el-divider content-position="left">
          <router-link to="/about"><i class="el-icon-user"></i>Jiacheng Weng </router-link> &nbsp;  daily visitors: {{ num }}
        </el-divider>
      </el-footer>
    </el-container>

  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      loading: true,
      num: null,
      islogin: false,
      username: ""
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    logout: function () {
      this.$axios.get("/apis/user/logout")
        .then(response => {
          // 重载界面
          window.location.reload()
        })
    }
  },
  created () {

    this.$axios.post("/apis/add?access=add_access&aa=32&kk=34", {access: "access"})
      .then(response => {
        this.$axios.get("/apis/get_info?num=true&aa=66")
          .then(response => {
            this.loading = false
            this.num = response.data.num
          })
      }, error => {
        console.log("这里出错了.")
      })
    this.$axios.get('/apis/user/getstatus?aa=60&kk=6')
      .then(response => {
        if (response.data.status === 0) {
          this.islogin = true
          this.username = response.data.username
        }
      })



    console.log('Jiacheng Weng')

  }
}
</script>

<style>

</style>
