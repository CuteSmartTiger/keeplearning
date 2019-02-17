<style lang="less">
  @import './login.less';
</style>

<template>
  <div class="login">
    <div class="login-con">
      <div  class="logo"><img src="../../assets/images/logo.jpg"></div>
      <Card icon="log-in" :bordered="false">
        <p slot="title" style="text-align: center">古语云桌面管理平台</p>
        <div class="form-con">
          <login-form @on-success-valid="handleSubmit"></login-form>
          <!--<p class="login-tip">输入任意用户名和密码即可</p>-->
        </div>
      </Card>
    </div>
  </div>
</template>

<script>
import LoginForm from '_c/login-form'
import { mapActions } from 'vuex'
export default {
  components: {
    LoginForm
  },
  data () {
    return {}
  },
  methods: {
    ...mapActions([
      'handleLogin',
      'getUserInfo'
    ]),
    handleSubmit ({ username, password }) {
      this.handleLogin({ username, password }).then(res => {
        this.$router.push({
          name: 'home'
        })
      })
    }
  }
}
</script>

<style>

</style>
