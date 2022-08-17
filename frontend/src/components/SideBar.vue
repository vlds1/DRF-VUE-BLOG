<template>


  <div class="sidebar">
    <div class="hide-sidebar">
    </div>
      <div class="logo">
          <img src="../assets/logo.png" class="logo-img">
      </div>
      <div class="sidebar-inner">
        <div class="menu" v-if="!this.$store.state.isAuthed">
            <ul class="menu__inner">
                <li><a href="/">Home</a></li>
            </ul>
            <ul class="menu__inner">
                <li><router-link class="django" :to="{ name: 'publications' }">Publications</router-link></li>
            </ul>
        </div>
        <div class="menu" v-if="this.$store.state.isAuthed">
            <ul class="menu__inner">
                <li><router-link :to="{ name: 'home' }"><img src="../assets/home.png"> <p>Home</p></router-link></li>
            </ul>
            <ul class="menu__inner">
                <li><router-link 
                    class="django" 
                    :to="{ name: 'publications' }"> 
                    <img src="../assets/publications.png"> <p>Publications</p>
                    </router-link>
                </li>
            </ul>
            <ul class="menu__inner">
                <li>
                    <router-link :to="{ name: 'craetePublication' }" class="django">
                        <img src="../assets/createPublication.png" alt=""> <p>Create publication</p>
                    </router-link>
                </li>
            </ul>
            <ul class="menu__inner">
                <li>
                    <a href="http://localhost:8000/admin/" class="django">
                        <img src="../assets/adminPanel.png" alt=""> <p>Admin panel</p>
                    </a>
                </li>
            </ul>
        </div>
      </div>
  </div>
</template>

<script>


export default {
    name: 'SideBar',
    mounted(){
        this.$store.state.isAuthed
    },
}
</script>

<style scoped>
@import url('../assets/styles/sidebar.css');
</style>