<template>
  <div class="navbar-container d-flex content align-items-center">

    <!-- Nav Menu Toggler -->
    <ul class="nav navbar-nav d-xl-none">
      <li class="nav-item">
        <b-link
          class="nav-link"
          @click="toggleVerticalMenuActive"
        >
          <feather-icon
            icon="MenuIcon"
            size="21"
          />
        </b-link>
      </li>
    </ul>

    <!-- Left Col -->
    <div class="bookmark-wrapper align-items-center flex-grow-1 d-none d-lg-flex">
<!--      <bookmarks />-->
      <dark-Toggler class="d-none d-lg-block" />
    </div>

    <!-- Right Col -->
<!--      <search-bar />-->
    <b-navbar-nav class="nav align-items-center ml-auto">
<!--      <locale />-->
<!--      <cart-dropdown />-->
<!--      <notification-dropdown />-->
      <user-dropdown />
    </b-navbar-nav>
  </div>
</template>

<script>
import {
  BLink, BNavbarNav,
} from 'bootstrap-vue'
import DarkToggler from './components/DarkToggler.vue'
import UserDropdown from './components/UserDropdown.vue'

export default {
  components: {
    BLink,

    // Navbar Components
    BNavbarNav,
    DarkToggler,
    UserDropdown,
  },
  props: {
    toggleVerticalMenuActive: {
      type: Function,
      default: () => {},
    },
  },

}
</script>
