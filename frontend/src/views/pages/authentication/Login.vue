<template>
  <div class="auth-wrapper auth-v1 px-2">
    <div class="auth-inner py-2">

      <!-- Login v1 -->
      <b-card class="mb-0">
        <b-link class="brand-logo">
          <h2 class="brand-text text-primary ml-1">
            ShareDesk
          </h2>
        </b-link>

        <b-card-title class="mb-1">
          Vitajte v aplikacií ShareDesk! 👋
        </b-card-title>

        <!-- form -->
        <validation-observer
          ref="loginForm"
          #default="{invalid}"
        >
          <b-form
            class="auth-login-form mt-2"
            @submit.prevent="login"
          >

            <!-- email -->
            <b-form-group
              label-for="email"
              label="Email"
            >
              <validation-provider
                #default="{ errors }"
                name="Email"
                rules="required|email"
              >
                <b-form-input
                  id="email"
                  v-model="userEmail"
                  name="login-email"
                  :state="errors.length > 0 ? false:null"
                  placeholder="john@example.com"
                  autofocus
                />
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>

            <!-- password -->
            <b-form-group>
              <div class="d-flex justify-content-between">
                <label for="password">{{ $t("Password") }}</label>
                <!--                <b-link :to="{name:'auth-forgot-password-v1'}">-->
                <!--                  <small>Forgot Password?</small>-->
                <!--                </b-link>-->
              </div>
              <validation-provider
                #default="{ errors }"
                name="Password"
                rules="required"
              >
                <b-input-group
                  class="input-group-merge"
                  :class="errors.length > 0 ? 'is-invalid':null"
                >
                  <b-form-input
                    id="password"
                    v-model="password"
                    :type="passwordFieldType"
                    class="form-control-merge"
                    :state="errors.length > 0 ? false:null"
                    name="login-password"
                    placeholder="Password"
                  />

                  <b-input-group-append is-text>
                    <feather-icon
                      class="cursor-pointer"
                      :icon="passwordToggleIcon"
                      @click="togglePasswordVisibility"
                    />
                  </b-input-group-append>
                </b-input-group>
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>

            <!-- checkbox -->
            <!--            <b-form-group>-->
            <!--              <b-form-checkbox-->
            <!--                id="remember-me"-->
            <!--                v-model="status"-->
            <!--                name="checkbox-1"-->
            <!--              >-->
            <!--                Remember Me-->
            <!--              </b-form-checkbox>-->
            <!--            </b-form-group>-->

            <!-- submit button -->
            <b-button
              variant="primary"
              type="submit"
              block
              :disabled="invalid"
            >
              {{ $t("Login") }}
            </b-button>
          </b-form>
        </validation-observer>

        <b-card-text class="text-center mt-2">
          <span>{{ $t("New on our platform?") }} </span>
          <b-link :to="{name:'auth-register'}">
            <span>{{ $t("Create an account") }}</span>
          </b-link>
        </b-card-text>

      </b-card>
      <!-- /Login v1 -->
    </div>
  </div>
</template>

<script>
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import {
  BButton,
  BForm,
  BFormInput,
  BFormGroup,
  BCard,
  BLink,
  BCardTitle,
  BCardText,
  BInputGroup,
  BInputGroupAppend,
  BFormCheckbox,
} from 'bootstrap-vue'
import { required, email } from '@validations'
import { togglePasswordVisibility } from '@core/mixins/ui/forms'

import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import axios from 'axios'
import jwt_decode from 'jwt-decode'
import useJwt from '@/auth/jwt/useJwt'
import store from '@/store/index'
import { getAbilityForUserRole } from '@/auth/utils'

import CustomLogo from '@/layouts/components/Logo.vue'

export default {
  components: {
    // BSV
    BButton,
    BForm,
    BFormInput,
    BFormGroup,
    BCard,
    BCardTitle,
    BLink,
    CustomLogo,
    BCardText,
    BInputGroup,
    BInputGroupAppend,
    BFormCheckbox,
    ValidationProvider,
    ValidationObserver,
  },
  mixins: [togglePasswordVisibility],
  data() {
    return {
      status: '',
      password: process.env.VUE_APP_PASS || '',
      userEmail: process.env.VUE_APP_LOGIN || '',
      sideImg: require('@/assets/images/pages/login-v2.svg'),
      // validation rules
      required,
      email,
    }
  },
  computed: {
    passwordToggleIcon() {
      return this.passwordFieldType === 'password' ? 'EyeIcon' : 'EyeOffIcon'
    },
    imgUrl() {
      if (store.state.appConfig.layout.skin === 'dark') {
        // eslint-disable-next-line vue/no-side-effects-in-computed-properties
        this.sideImg = require('@/assets/images/pages/login-v2-dark.svg')
        return this.sideImg
      }
      return this.sideImg
    },
  },
  methods: {
    login() {
      this.$refs.loginForm.validate().then(success => {
        if (success) {
          useJwt.login({
            email: this.userEmail,
            password: this.password,
          }).then(response => {
            useJwt.setToken(response.data.access)
            useJwt.setRefreshToken(response.data.refresh)

            const decoded = jwt_decode(response.data.refresh)
            this.$http.get(`/users/${decoded.user_id}`).then(res => {
              const userData = res.data
              localStorage.setItem('userData', JSON.stringify(userData))
              this.$ability.update(getAbilityForUserRole(userData.role))

              this.$router.replace('/').then(() => {
                this.$toast({
                  component: ToastificationContent,
                  position: 'top-right',
                  props: {
                    title: `${this.$t('Welcome')} ${userData.full_name || userData.email}`,
                    icon: 'CoffeeIcon',
                    variant: 'success',
                    text: `${this.$t('You have successfully logged in as')} ${userData.role}. ${this.$t('Now you can start to explore!')}`,
                  },
                })
              })
            })
          }).catch(error => {
            console.error(error)
            this.$refs.loginForm.setErrors(error.response.data.error)
          })
        }
      })
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/pages/page-auth.scss';
</style>
