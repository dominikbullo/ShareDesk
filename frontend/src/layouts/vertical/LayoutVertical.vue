<template>
  <layout-vertical>

    <router-view />

    <template #navbar="{ toggleVerticalMenuActive }">
      <navbar :toggle-vertical-menu-active="toggleVerticalMenuActive" />
    </template>

    <!-- <app-customizer
      v-if="showCustomizer"
      slot="customizer"
    /> -->

    <div slot="footer">
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
    </div>
  </layout-vertical>
</template>

<script>
import LayoutVertical from '@core/layouts/layout-vertical/LayoutVertical.vue'
// import AppCustomizer from '@core/layouts/components/app-customizer/AppCustomizer.vue'
// import { $themeConfig } from '@themeConfig'
import { BLink } from 'bootstrap-vue'
import Navbar from '../components/app-navbar/Navbar.vue'

export default {
  components: {
    // AppCustomizer,
    LayoutVertical,
    Navbar,
    BLink,
  },
  data() {
    return {
      // showCustomizer: $themeConfig.layout.customizer,
    }
  },
}
</script>
