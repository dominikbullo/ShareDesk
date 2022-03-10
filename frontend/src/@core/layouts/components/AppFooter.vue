<template>
  <p class="clearfix mb-0">
    <span class="float-md-left d-block d-md-inline-block mt-25">
      COPYRIGHT  © {{ new Date().getFullYear() }}
      <b-link
        class="ml-25"
        href="https://bullo.sk/"
        target="_blank"
      >Dominik Bullo</b-link>
      <span class="d-none d-sm-inline-block">, All rights Reserved</span>
    </span>
    <span class="float-md-right d-none d-md-block">
      <b-link
        class="ml-10"
        href="https://bullo.sk/"
        target="_blank"
      >Share Desk</b-link>
      version {{ $store.getters['app/appVersion'] }}
    </span>
  </p>
</template>

<script>
import { BLink } from 'bootstrap-vue'

export default {
  components: {
    BLink,
  },
}
</script>
