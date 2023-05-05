<template>
    <div id="Login" v-loading="false" style="margin: 0 auto">
        <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
          <el-form ref="FormDatas" :model="FormDatas" label-width="80px" :rules="rules">
            <el-form-item label="username" prop="username">
              <el-input type="text" v-model="FormDatas.username" autocomplete="off" placeholder="username"></el-input>
            </el-form-item>
            <el-form-item label="password" prop="password">
              <el-input type="password" v-model="FormDatas.password" autocomplete="off" placeholder="password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="submitd('FormDatas')">sign in</el-button>
              &nbsp;&nbsp;no account?
              <router-link to="/user/register">click me to sign up</router-link>
            </el-form-item>
          </el-form>
        </el-col>
    </div>
</template>

<script>
  export default {
    name: 'Login',
    data() {
      return {
        FormDatas: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            {required: true, message: 'This is a required field!', trigger: 'blur'}
          ],
          password: [
            {required: true, message: 'This is a required field!', trigger: 'blur'}
          ]
        }
      }
    },
    methods: {
      submitd: function (Dataset) {
        this.$refs[Dataset].validate((valid) => {
          if (valid) {
            // 成功
            this.$axios.post("/apis/user/login", {
              username: this.FormDatas.username,
              password: this.FormDatas.password,
            })
              .then(response => {
                if (response.data.status === 0) {
                  this.$router.push({path: "/"});
                  window.location.reload();
                } else {
                  this.$notify({
                    title: 'login fail',
                    message: response.data.message,
                    type: 'error'
                  })
                }

              })
          } else {
            return false;
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
