import axios from '@axios'

export default {
  namespaced: true,
  state: {},
  getters: {},
  mutations: {},
  actions: {
    fetchTeams(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/teams/', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchTeam(ctx, { id }) {
      return new Promise((resolve, reject) => {
        axios
          .get(`/team/${id}`)
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    addTeam(ctx, userData) {
      return new Promise((resolve, reject) => {
        axios
          .post('/teams', { ...userData })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    deleteTeam(ctx, { id }) {
      return new Promise((resolve, reject) => {
        axios
          .delete(`/team/${id}`)
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
  },
}
