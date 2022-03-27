<template>
  <div>
    {{ test }}
  </div>
</template>

<script>

import axios from '@/libs/axios'

export default {
  data() {
    return {
      test: [],
    }
  },
  created() {
    return new Promise((resolve, reject) => {
      axios
        .get('/reservations/my_reservations/')
        .then(response => {
          this.test = response.data
          resolve(response)
        })
        .catch(error => reject(error))
    })
  },
}
</script>

<style>

</style>
