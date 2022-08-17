import axios from 'axios'

const api = axios.create()

api.interceptors.request.use(config => {
    if(localStorage.getItem('accessToken')){
        config.headers.authorization = `Bearer ${localStorage.getItem('accessToken')}`
    }
    
    return config
}, error => {
    console.log(error); 
})

api.interceptors.response.use(config => {
    if(localStorage.getItem('accessToken')){
        config.headers.authorization = `Bearer ${localStorage.getItem('accessToken')}`
    }
    
    return config
}, error => {
    if(error.response.data.messages[0].message === 'Token is invalid or expired'){
        return axios.post('http://localhost:8000/api/v1/token/refresh/', {
            'refresh': `${localStorage.getItem('refreshToken')}`
        }, {
            headers: {
                "Content-Type": "application/json",
            }
        }).then(res => {
            localStorage.setItem('accessToken', res.data.access)
            error.config.headers.authorization = `Bearer ${res.data.access}`

            return api.request(error.config)
        })
    }
})

export default api