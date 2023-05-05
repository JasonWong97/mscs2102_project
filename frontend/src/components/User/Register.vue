<template>
  <div id="Register">
    <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
      <el-form :model="FormData" status-icon ref="FormData" :rules="rules">
        <el-form-item label="username" prop="username">
          <el-input type="text" v-model="FormData.username" placeholder="username"></el-input>
        </el-form-item>
        <el-form-item label="password" prop="password">
          <el-input type="password" v-model="FormData.password" placeholder="password"></el-input>
        </el-form-item>
        <el-form-item label="confirm password" prop="repassword">
          <el-input type="password" v-model="FormData.repassword" placeholder="confirm password"></el-input>
        </el-form-item>
        <el-form-item label="email" prop="email">
          <el-input v-model="FormData.email" placeholder="please enter your email"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitd('FormData')">submit</el-button>
          <el-button @click="resetForm('FormData')">clear</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </div>
</template>

<script>
  export default {
    name: 'Register',
    data() {
      // 检测第二次输入的密码
      var checkPassword = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('please enter you password again'))
        } else if (value !== this.FormData.password) {
          callback(new Error('The passwords you typed do not match..'))
        } else {
          callback()
        }
      }
      // 检测用户名是否已经被注册
      var dulaUsername = (rule, value, callback) => {
        // 验证用户名是否存在.  一会再写
        if (value.length < 3) {
          callback(new Error('username too short！'))
        } else if (value.length > 18) {
          callback(new Error('username too long！'))
        } else {
          this.$axios.post('/apis/user/register?select=1', {
            select_username: value
          })
            .then(response => {
              if (response.data.is_indb === 1) {
                callback(new Error('The user name has been registered.'))
              } else {
                callback();
              }
            })
        }
      }

      // 检测密码的长度
      var checkLen = (rule, value, callback) => {
        if (value.length < 6) {
          callback(new Error('Password length cannot be less than 6 digits'))
        } else if (value.length > 18) {
          callback(new Error('Password length cannot exceed 18 digits'))
        } else {
          callback()
        }
      }

      return {
        FormData: {
          username: "",
          password: "",
          repassword: "",
          email: ""
        },
        rules: {
          username: [{required: true, message: 'This is a required field', trigger: 'blur'}, {validator: dulaUsername, trigger: 'blur'}],
          password: [{required: true, message: "This is a required field", trigger: 'blur'}, {validator: checkLen, trigger: 'blur'}],
          repassword: [{required: true, message: 'This is a required field', trigger: 'blur'}, {validator: checkPassword, trigger: 'blur'}],
          email: [{required: true, message: "Please enter your email address", trigger: 'blur'}, {type: 'email', message: 'Please enter the correct email address', trigger: ['blur', 'change']}]
        }
      }
    },
    methods: {
      submitd: function (formdata) {
        this.$refs[formdata].validate((valid) => {
          if (valid) {
            // 成功.
            this.$axios.post('/apis/user/register', {
              username: this.FormData.username,
              password: this.FormData.password,
              email: this.FormData.email
            })
              .then(response => {
                if (response.data.status === 0) {
                  this.$router.push({path: '/'})
                  window.location.reload()
                } else {
                  return false
                }
              })

          } else {
            return false;
          }
        });
      },
      resetForm: function (formdata) {
        this.$refs[formdata].resetFields()
      }
    }
  }
</script>

<style scoped>

</style>
