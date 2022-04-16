<template>
  <layout-horizontal>

    <router-view />

    <template #breadcrumb>
      <app-breadcrumb />
    </template>

    <template #navbar="{ toggleVerticalMenuActive }">
      <app-navbar-horizontal-layout-brand />
      <navbar :toggle-vertical-menu-active="toggleVerticalMenuActive" />
    </template>

    <!-- <app-customizer
      v-if="showCustomizer"
      slot="customizer"
    /> -->
  </layout-horizontal>
</template>

<script>
import LayoutHorizontal from '@core/layouts/layout-horizontal/LayoutHorizontal.vue'
// import AppCustomizer from '@core/layouts/components/app-customizer/AppCustomizer.vue'
// import { $themeConfig } from '@themeConfig'
import AppNavbarHorizontalLayoutBrand from '@core/layouts/components/app-navbar/AppNavbarHorizontalLayoutBrand.vue'
import AppBreadcrumb from '@/layouts/components/AppBreadcrumb.vue'
import Navbar from '../components/app-navbar/Navbar.vue'

export default {
  components: {
    LayoutHorizontal,
    // AppCustomizer,
    Navbar,
    AppBreadcrumb,
    AppNavbarHorizontalLayoutBrand,
  },
  data() {
    return {
      // showCustomizer: $themeConfig.layout.customizer,
    }
  },
}
</script>
