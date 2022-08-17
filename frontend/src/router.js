import { createWebHistory, createRouter } from 'vue-router'

import HomePage from "./components/HomePage.vue"
import LoginPage from './components/LoginPage.vue'
import aPublicationPage from './components/aPublicationPage.vue'
import CreatePage from './components/CreatePage.vue'
import PublicationsPage from './components/PublicationsPage.vue'
import EditPublicationPage from './components/EditPublicationPage.vue'

const router = new createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/', 
            name: 'home',
            component: HomePage,
        },
        {
            path: '/login',
            name: 'login',
            component: LoginPage,
        },
        {
            path: '/publications',
            name: 'publications',
            component: PublicationsPage,
        },
        {
            path: '/publication/:id',
            name: 'publication',
            component: aPublicationPage,
            props: true,
        },
        {
            path: '/editpublication/:id',
            name: 'editpublication',
            component: EditPublicationPage,
            props: true,
        },
        {
            path: '/craetePublication',
            name: 'craetePublication',
            component: CreatePage,
        },
    ]
})

// router.beforeEach((to, from, next) => {
//     const accessToken = localStorage.getItem('accessToken')

//     if (to.name !== 'login'){
//         if (!accessToken){
//             return next({
//                 name: 'login'
//             })
//         }
//     }

//     next();
// })

export default router