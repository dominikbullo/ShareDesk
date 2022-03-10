import Vue from 'vue'

// axios
import axios from 'axios'

const baseURL = '/api'

const axiosIns = axios.create({
  // You can add your headers here
  // ================================
  baseURL,
  timeout: 10000,
  // headers: {'X-Custom-Header': 'foobar'}
})

// Add a request interceptor
axiosIns.interceptors.request.use(config => {
  console.log('[AXIOS] Request Interceptors', config)
  return config
}, error => {
  console.error('[AXIOS] Request Interceptors Error', error)
  return Promise.reject(error)
})

// Add request/response interceptor
axiosIns.interceptors.response.use(response => {
  console.log('[AXIOS] Response Interceptors', response)
  return response
}, error => {
  console.error('[AXIOS] Response Interceptors', error)
  return Promise.reject(error)
})

axiosIns.defaults.xsrfHeaderName = 'X-CSRFToken'
axiosIns.defaults.xsrfCookieName = 'csrftoken'

Vue.prototype.$http = axiosIns

export default axiosIns
