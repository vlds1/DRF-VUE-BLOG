<template>
    <div id="app" class="app">
      <SideBar v-if="this.routeName.name != 'login'"/>
      <router-view/>
    </div>
</template>

<script>
import SideBar from './components/SideBar.vue'

export default {
  data(){
    return{
      routeName: this.$router['currentRoute']
    }
  },
  mounted(){
    this.$router['currentRoute']
  },
  name: 'App',
  components: {
    SideBar,
  }
}
</script>

<style lang="scss">
@import './assets/styles/index.scss';

</style>
