<template>
  <b-tabs
    vertical
    content-class="col-12 col-md-9 mt-1 mt-md-0"
    pills
    nav-wrapper-class="col-md-3 col-12"
    nav-class="nav-left"
  >

    <!-- general tab -->
    <b-tab active>

      <!-- title -->
      <template #title>
        <feather-icon
          icon="UserIcon"
          size="18"
          class="mr-50"
        />
        <span class="font-weight-bold">General</span>
      </template>

      <account-setting-general
        v-if="options.general"
        :general-data="options.general"
      />
    </b-tab>
    <!--/ general tab -->

    <!-- change password tab -->
    <!--    <b-tab>-->

    <!--      &lt;!&ndash; title &ndash;&gt;-->
    <!--      <template #title>-->
    <!--        <feather-icon-->
    <!--          icon="LockIcon"-->
    <!--          size="18"-->
    <!--          class="mr-50"-->
    <!--        />-->
    <!--        <span class="font-weight-bold">Change Password</span>-->
    <!--      </template>-->

    <!--      <account-setting-password />-->
    <!--    </b-tab>-->
    <!--/ change password tab -->

  </b-tabs>
</template>

<script>
import { BTabs, BTab } from 'bootstrap-vue'
import AccountSettingGeneral from './AccountSettingGeneral.vue'
import AccountSettingPassword from './AccountSettingPassword.vue'

export default {
  components: {
    BTabs,
    BTab,
    AccountSettingGeneral,
    AccountSettingPassword,
  },
  data() {
    return {
      options: {
        general: {},
      },
    }
  },
  beforeCreate() {
    this.$http.get('/user/profile').then(res => {
      this.options = {
        general: {
          ...res.data,
        },
        info: {
          ...res.data,
        },
      }
    })
  },
}
</script>
