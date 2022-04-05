import axios from '@axios'

export default {
  namespaced: true,
  state: {},
  getters: {},
  mutations: {},
  actions: {
    fetchWorkspaces(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/workspaces/', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchFloors(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/floors/', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchRooms(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/rooms/', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchRoom(ctx, { id }) {
      return new Promise((resolve, reject) => {
        axios
          .get(`/room/${id}`)
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchRoomSpots(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/reservations/', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    fetchIssues(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .get('/spots-issues/', { params: queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
    addSpotIssue(ctx, queryParams) {
      return new Promise((resolve, reject) => {
        axios
          .post('/spots-issues/', { ...queryParams })
          .then(response => resolve(response))
          .catch(error => reject(error))
      })
    },
  },
}
