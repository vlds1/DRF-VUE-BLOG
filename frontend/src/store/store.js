import { createStore } from 'vuex'
// import createPersistedState from "vuex-persistedstate";
// import SecureLS from "secure-ls";
// var ls = new SecureLS({ isCompression: false });

const store = createStore({
    state(){
        return{
            isAuthed: localStorage.getItem('isAuthed') || false,
            accessToken: localStorage.getItem('accessToken') || null,
            refreshToken: localStorage.getItem('refreshToken') || null,
        }   
    },
    // plugins: [
    //     createPersistedState({
    //       storage: {
    //         getItem: (key) => ls.get(key),
    //         setItem: (key, value) => ls.set(key, value),
    //         removeItem: (key) => ls.remove(key),
    //       },
    //     }),
    //   ],
    mutations: {
        LOGIN(state, payload){
            state.isAuthed = true
            localStorage.setItem('isAuthed', true)
            state.accessToken = localStorage.setItem('accessToken', payload.access)
            state.refreshToken = localStorage.setItem('refreshToken', payload.refresh)
        },
        LOGOUT(state){
            localStorage.clear()
            state.isAuthed = false
            state.accessToken = null
            state.refreshToken = null
        }
    }
})

export default store