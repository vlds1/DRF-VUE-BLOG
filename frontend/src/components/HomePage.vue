<template>
  <div class="home-page">
    <div class="navbar">
      <div class="navbar-inner">
        <router-link v-if="this.$store.state.isAuthed" :to="{name: 'home'}" class="logout" @click="logout">
          <img src="../assets/logout.png" class="logout-img">
        </router-link>
      </div>
    </div>
    <div class="container">


      <div class="container-inner">
        HomePage
      </div>
    </div>
  </div>
</template>

<script>

export default {
    name: 'HomePage',
    components: {
    },
    methods: {
      logout(){
        this.$store.commit('LOGOUT')
      }
    }
}
</script>

<style scoped>

</style>