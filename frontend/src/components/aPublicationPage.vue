<template>
<div class="publication-page">
    <!-- <SideBar/> -->
    <div class="navbar">
        <div class="navbar-inner">
          <router-link :to="{name: 'home'}" class="logout" @click="logout" v-if="this.$store.state.isAuthed">
            <img src="../assets/logout.png" class="logout-img">
        </router-link>
        </div>
    </div>
    <div class="container">

        <div class="title">
            {{publication.title}}
        </div>
        <div v-html="replaceNr" class="content">
        </div>
    </div>
</div>
</template>

<script>
import axios from "axios"

export default {
    data(){
        return {
            publication: {},
            content: '',
        }
    },
    props: ['id'],
    mounted () {
        this.loadPublication()
    },
    methods:{
        loadPublication(){
            axios.get(`http://localhost:8000/api/v1/publ/${this.id}`)
            .then((response) => {
                this.publication = response.data.data
                this.content = response.data.data.content
            })
        }

    },
    computed: {
        replaceNr: function(){
            return this.content.replace(/\n/g, '<br />')
        }
    }
}
</script>

<style scoped>

</style>