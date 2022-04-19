<template>
  <div class="auth-wrapper auth-v1 px-2">
    <div class="auth-inner py-2">

      <!-- Register -->
      <b-card class="mb-0">
        <b-link class="brand-logo">
          <h2 class="brand-text text-primary ml-1">
            ShareDesk
          </h2>
        </b-link>

        <b-card-title class="mb-1">
          Adventure starts here 🚀
        </b-card-title>

        <!-- form -->
        <validation-observer ref="registerForm">
          <b-form
            class="auth-register-form mt-2"
            @submit.prevent="register"
          >

            <!-- First name -->
            <b-form-group
              label="First Name"
              label-for="mc-first-name"
            >
              <validation-provider
                #default="{ errors }"
                name="first_name"
                rules="required|alpha"
              >
                <b-form-input
                  id="mc-first-name"
                  v-model="regFirstName"
                  placeholder="First Name"
                  :state="errors.length > 0 ? false:null"
                />
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>

            <!-- Last name -->
            <b-form-group
              label="Last Name"
              label-for="mc-last-name"
            >
              <validation-provider
                #default="{ errors }"
                name="last_name"
                rules="required|alpha"
              >
                <b-form-input
                  id="mc-last-name"
                  v-model="regLastName"
                  placeholder="Last Name"
                  :state="errors.length > 0 ? false:null"
                />
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>

            <!-- email -->
            <b-form-group
              label="Email"
              label-for="email"
            >
              <validation-provider
                #default="{ errors }"
                name="email"
                rules="required|email"
              >
                <b-form-input
                  id="email"
                  v-model="regEmail"
                  :state="errors.length > 0 ? false:null"
                  name="register-email"
                  placeholder="john@example.com"
                />
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>

            <!-- password -->
            <b-form-group
              label="Password"
              label-for="password"
            >
              <validation-provider
                #default="{ errors }"
                name="password"
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
                    :state="errors.length > 0 ? false:null"
                    class="form-control-merge"
                    name="register-password"
                    placeholder="············"
                  />
                  <b-input-group-append is-text>
                    <feather-icon
                      :icon="passwordToggleIcon"
                      class="cursor-pointer"
                      @click="togglePasswordVisibility"
                    />
                  </b-input-group-append>
                </b-input-group>
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>

            <!-- password -->
            <b-form-group
              label="Password confirm"
              label-for="password"
            >
              <validation-provider
                #default="{ errors }"
                name="password"
                rules="required"
              >
                <b-input-group
                  class="input-group-merge"
                  :class="errors.length > 0 ? 'is-invalid':null"
                >
                  <b-form-input
                    id="password-confirm"
                    v-model="password"
                    :type="passwordFieldType"
                    :state="errors.length > 0 ? false:null"
                    class="form-control-merge"
                    name="register-password"
                    placeholder="············"
                  />
                  <b-input-group-append is-text>
                    <feather-icon
                      :icon="passwordToggleIcon"
                      class="cursor-pointer"
                      @click="togglePasswordVisibility"
                    />
                  </b-input-group-append>
                </b-input-group>
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>

            <!-- submit button -->
            <b-button
              variant="primary"
              block
              type="submit"
            >
              {{ $t("Register") }}
            </b-button>
          </b-form>
        </validation-observer>

        <b-card-text class="text-center mt-2">
          <span>{{ $t("Already have an account? ") }}</span>
          <b-link :to="{name:'auth-login'}">
            <span>{{ $t("Log in instead") }}</span>
          </b-link>
        </b-card-text>

      </b-card>
      <!-- /Register -->
    </div>
  </div>

</template>

<script>
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import {
  BCard, BLink, BCardTitle, BCardText, BForm,
  BButton, BFormInput, BFormGroup, BInputGroup, BInputGroupAppend, BFormCheckbox,
} from 'bootstrap-vue'
import { required, email } from '@validations'
import { togglePasswordVisibility } from '@core/mixins/ui/forms'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import CustomLogo from '@/layouts/components/Logo.vue'

import useJwt from '@/auth/jwt/useJwt'

export default {
  components: {
    CustomLogo,
    // BSV
    BCard,
    BLink,
    BCardTitle,
    BCardText,
    BForm,
    BButton,
    BFormInput,
    BFormGroup,
    BInputGroup,
    BInputGroupAppend,
    BFormCheckbox,
    // validations
    ValidationProvider,
    ValidationObserver,
  },
  mixins: [togglePasswordVisibility],
  data() {
    return {
      regFirstName: 'test',
      regLastName: 'testovací',
      regEmail: 'a@b.sk',
      password: 'testing321',

      // validation rules
      required,
      email,
    }
  },
  computed: {
    passwordToggleIcon() {
      return this.passwordFieldType === 'password' ? 'EyeIcon' : 'EyeOffIcon'
    },
  },
  methods: {
    register() {
      this.$refs.registerForm.validate().then(success => {
        if (success) {
          useJwt.register({
            first_name: this.regFirstName,
            last_name: this.regLastName,
            email: this.regEmail,
            password: this.password,
          }).then(() => {
            this.$toast({
              component: ToastificationContent,
              props: {
                title: 'Form Submitted',
                icon: 'EditIcon',
                variant: 'success',
              },
            })
            this.$router.push('/')
          }).catch(error => {
            // Server side validation
            this.$refs.registerForm.setErrors(error.response.data)
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
