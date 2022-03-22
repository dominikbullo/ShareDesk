import axios from '@axios'

export default {
  namespaced: true,
  state: {},
  getters: {},
  mutations: {},
  actions: {
    fetchIssues(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/spots-issues/', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
  },
}
