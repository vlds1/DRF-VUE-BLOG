<template>
  <div class="publication-page">
    <div class="navbar">
      <div class="navbar-inner">
        <!-- <input type="text" class="search-inp" placeholder="🔍︎ Search">  -->
        <button @click="getBlogPublications" class="catigory-btn">Blog</button>
        <button @click="getArticlesPublications" class="catigory-btn">Articles</button>
        <button @click="getAllPublications" class="catigory-btn">All Publications</button>
      </div>
      <div class="navbar-inner">
        <router-link :to="{name: 'home'}" class="logout" @click="logout" v-if="this.$store.state.isAuthed">
          <img src="../assets/logout.png" class="logout-img">
        </router-link>
      </div>
    </div>
    <div class="container">

      <div class="container-inner">
        <ul class="publication-list">
          <li v-for="item in publications.data" :key="item.id" class="publication">
            <router-link 
              :to="{ 
                name: 'publication', 
                params: {id: item.id},
              }" 
              class="publicatin-link"
              >
                {{item.title}}
            </router-link>
            <div class="publication-actions">
              <button
                v-if="this.$store.state.isAuthed" 
                @click="deletePubl(item.id)"
              >
                <img src="../assets/delete-publication.png" alt="">
              </button>
              <router-link
                v-if="this.$store.state.isAuthed"
                :to = "{
                  name: 'editpublication',  
                  params: {id: item.id},
                }" 
              >
                <img src="../assets/edit-publication.png" alt="">
              </router-link>
            </div>
          </li>
      </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from '../api'

export default {
    name: 'HomePage',
    components: {
    },
    data(){
      return {
        publications: [],
        showPubls: false,
      }
    },
    mounted () {
      this.getAllPublications()
      this.$store.state.isAuthed
    },
    methods: {
      getAllPublications(){
        axios.get('http://localhost:8000/api/v1/publ/all/')
        .then(r => this.publications = r.data)
      },
      getBlogPublications(){
        axios.get('http://localhost:8000/api/v1/publ/blog/')
        .then(r => this.publications = r.data)
      },
      getArticlesPublications(){
        axios.get('http://localhost:8000/api/v1/publ/articles/')
        .then(r => this.publications = r.data)
      },

      deletePubl(id){
        API.post(`http://localhost:8000/api/v1/publ/delete/${id}`)
        .then(() => {
          this.getAllPublications()
        })
      },
      editPublication(id){
        API.get(`http://localhost:8000/api/v1/publ/edit/${id}`)
        .then(() => {this.getAllPublications()})
      },
      logout(){
        this.$store.commit('LOGOUT')
      }
    }
}
</script>

<style scoped>

</style>