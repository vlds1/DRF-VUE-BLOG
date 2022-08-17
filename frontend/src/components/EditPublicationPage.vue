<template>
  <div class="create-page">
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
            <input type="text" name="title" id="title" class="title" placeholder="Title"
                v-model="title"
            >
            
            <label for="content"></label>
            <textarea type="text" name="content" id="content" class="content" placeholder="Content"
                :value="content"
            >
            </textarea>
          </div>
          <div class="create-selects">
            <div class="catigory" >
              <label for="catigory" class="catigory-label">Select catigory or <a href="#">create a new one</a></label>
              <select v-model="catigory" id="catigory" class="catigory-select" :value="publication.cat">
                <option value="Blog">Blog</option>
                <option value="Articles">Articles</option> 
              </select>
            </div>

            <div class="published">
              <input type="checkbox" v-model="isPublished" name="isPublished" id="isPublished" class="published-inp">
              <label for="isPublished" class="published-label">Published?</label>
            </div>
          </div>

        <button class="edit__publication__btn" @click="editPublication">Save</button>
      </div>
    </div>
  </div>
</template>

<script>

import API from '../api'

export default {
    data(){
        return{
            publication: {},

            title: null,
            content: null,
            catigory: null,
            isPublished: null
        }
    },
    props: ['id'],
    mounted(){
        this.getPublication()
    },
    methods:{
        getPublication(){
            API.get(`http://localhost:8000/api/v1/publ/${this.id}`)
            .then((response) => {
                this.title = response.data.data.title
                this.content = response.data.data.content
                this.catigory = response.data.data.cat
                this.isPublished = response.data.data.is_published
            })
        },
        editPublication(){
            API.post(`http://localhost:8000/api/v1/publ/edit/${this.id}`, {
                title: this.title,
                content: this.content,
                cat: this.catigory,
                is_published: this.isPublished,
            })
            .then(() => {
                this.$router.push('/')
            })
        },
        logout(){
            this.$store.commit('LOGOUT')
        }
    }
}
</script>

<style scoped>

</style>