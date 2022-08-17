<template>
  <div class='login'>
    <div class="login-inner">
      <div class="login-fields">
        <label for="username">Username</label>
        <input type="text" name="username" v-model="username" placeholder="Username">
        <label for="password">Password</label>
        <input type="password" name="password" v-model="password" placeholder="Password">
      </div>
      <button @click.prevent="loginHandler" class="login-btn">login</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'LoginPage',
    data(){
      return {
          username: null,
          password: null,
      }
    },
    methods: {
      async loginHandler(){
        await axios.post(
          'http://localhost:8000/api/v1/token/', 
          { username: this.username, password: this.password}
        )
        .then(res => {
          this.$store.commit('LOGIN', {'access': res.data.access, 'refresh': res.data.refresh})
          this.$router.push('/')
        })
      }
    }
}
</script>

<style scoped>
.login{
  height: 80vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: space-around;
}
.login-inner{
  height: 300px;
  width: 500px;
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-evenly;
  background-color: #2a302d;
  box-shadow: 0 0 10px #242424;
  border-radius: 15px;
}
.login-fields{
  display: flex;
  flex-direction: column;
  width: 70%;
}
.login-btn{
  display: flex;
  justify-content: center;
  padding: 10px 20px;
  background-color: #fff;
  border-radius: 5px;
}
label{
  margin: 15px 0 5px 0;
  color: #fff;
}
input:-webkit-autofill{
  box-shadow:inset 0 0 0 1000px #fff;
}
input{
  padding: 10px;
  font-size: 16px;
  background-color: #fff;
  border: 1px solid #000;
  border-radius: 5px;
}
</style>