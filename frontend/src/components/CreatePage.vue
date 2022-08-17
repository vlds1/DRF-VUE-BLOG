<template>
  <div class="create-page">
    <!-- <SideBar/> -->
    <div class="navbar">
        <div class="navbar-inner">
          <router-link :to="{name: 'home'}" class="logout" @click="logout" v-if="this.$store.state.isAuthed">
            <img src="../assets/logout.png" class="logout-img">
          </router-link>
        </div>
    </div>
    <div class="container">
        <div class="create-inner">

          <div class="create-fields">
            <label for="title"></label>
            <input type="text" name="title" v-model="title" id="title" 
              class="create__title" placeholder="Title"
            >

            <label for="content"></label>
            <textarea type="text" name="content" v-model="content" 
              id="content" class="create__content" placeholder="Content"
            >
            </textarea>
          </div>

          <div class="create-selects">
            <div class="catigory" >
              <label for="catigory" class="catigory-label">
                Select catigory or <a href="#">create a new one</a>
              </label>
              
              <select v-model="catigory" id="catigory" class="catigory-select">
                <option value="Blog">Blog</option>
                <option value="Articles">Articles</option> 
              </select>
            </div>

            <div class="published">
              <input type="checkbox" v-model="isPublished" name="isPublished" id="isPublished" class="published-inp">
              <label for="isPublished" class="published-label">Published?</label>
            </div>
          </div>

        <button class="create-btn" @click="createPubl">Create</button>
      </div>
    </div>
  </div>
</template>

<script>

import API from '../api'

export default {
    name: 'CreatePage',
    components: {
    },
    data(){
        return{
            title: null,
            content: null,
            catigory: null,
            isPublished: null
        }
    },
    methods:{
      async createPubl(){   
        await API.post('http://localhost:8000/api/v1/publ/create/', {
          title: this.title,
          content: this.content,
          cat: this.catigory,
        })
        this.$router.push('publications')
      },
      logout(){
        this.$store.commit('LOGOUT')
      }
    }
}
</script>

<style scoped>

</style>