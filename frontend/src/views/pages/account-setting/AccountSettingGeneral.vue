<template>
  <b-card>
    {{ optionsLocal }}
    <!-- form -->
    <validation-observer ref="appSettingsGeneralForm">
      <b-form class="mt-2">
        <b-row>
          <b-col sm="6">
            <b-form-group
              label="First Name"
              label-for="app-settings-first-name"
            >
              <validation-provider
                #default="{ errors }"
                name="first_name"
                rules="required|alpha"
              >
                <b-form-input
                  id="app-settings-first-name"
                  v-model="optionsLocal.first_name"
                  placeholder="First Name"
                  :state="errors.length > 0 ? false:null"
                />
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <!-- Last name -->
            <b-form-group
              label="Last Name"
              label-for="app-settings-last-name"
            >
              <validation-provider
                #default="{ errors }"
                name="last_name"
                rules="required|alpha"
              >
                <b-form-input
                  id="app-settings-last-name"
                  v-model="optionsLocal.last_name"
                  placeholder="Last Name"
                  :state="errors.length > 0 ? false:null"
                />
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>
          </b-col>
          <b-col sm="6">
            <!-- email -->
            <b-form-group
              label="Email"
              label-for="app-settings-email"
            >
              <validation-provider
                #default="{ errors }"
                name="email"
                rules="required|email"
              >
                <b-form-input
                  id="app-settings-email"
                  v-model="optionsLocal.email"
                  :state="errors.length > 0 ? false:null"
                  name="register-email"
                  placeholder="john@example.com"
                />
                <small class="text-danger">{{ errors[0] }}</small>
              </validation-provider>
            </b-form-group>
          </b-col>

          <b-col cols="12">
            <b-button
              v-ripple.400="'rgba(255, 255, 255, 0.15)'"
              variant="primary"
              class="mt-2 mr-1"
              @click="updateProfile"
            >
              {{ $t("Save changes") }}
            </b-button>
            <b-button
              v-ripple.400="'rgba(186, 191, 199, 0.15)'"
              variant="outline-secondary"
              type="reset"
              class="mt-2"
              @click.prevent="resetForm"
            >
              {{ $t("Reset") }}
            </b-button>
          </b-col>
        </b-row>
      </b-form>
    </validation-observer>
  </b-card>
</template>

<script>
import { required, email } from '@validations'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import {
  BFormFile,
  BButton,
  BForm,
  BFormGroup,
  BFormInput,
  BRow,
  BCol,
  BAlert,
  BCard,
  BCardText,
  BMedia,
  BMediaAside,
  BMediaBody,
  BLink,
  BImg,
} from 'bootstrap-vue'
import Ripple from 'vue-ripple-directive'
import { useInputImageRenderer } from '@core/comp-functions/forms/form-utils'
import { ref } from '@vue/composition-api'
import useJwt from '@/auth/jwt/useJwt'
import ToastificationContent from '@core/components/toastification/ToastificationContent'
import axios from '@/libs/axios'

export default {
  components: {
    BButton,
    BForm,
    BImg,
    BFormFile,
    BFormGroup,
    BFormInput,
    BRow,
    BCol,
    BAlert,
    BCard,
    BCardText,
    BMedia,
    BMediaAside,
    BMediaBody,
    BLink,

    // validations
    ValidationProvider,
    ValidationObserver,
  },
  directives: {
    Ripple,
  },
  props: {
    generalData: {
      type: Object,
      default: () => {
      },
    },
  },
  data() {
    return {
      optionsLocal: JSON.parse(JSON.stringify(this.generalData)),
      profileFile: null,

      // validation rules
      required,
      email,
    }
  },
  watch: {
    generalData() {
      this.resetForm()
    },
  },
  methods: {
    resetForm() {
      this.optionsLocal = JSON.parse(JSON.stringify(this.generalData))
    },
    updateProfile() {
      this.$refs.appSettingsGeneralForm.validate().then(success => {
        if (success) {
          axios
            .patch(`/user/${this.generalData.id}`, {
              first_name: this.optionsLocal.first_name,
              last_name: this.optionsLocal.last_name,
              email: this.optionsLocal.email,
            }).then(res => {
              this.optionsLocal.full_name = `${this.optionsLocal.first_name} ${this.optionsLocal.last_name}`
              localStorage.setItem('userData', JSON.stringify(this.optionsLocal))
              this.$router.go()
              this.$toast({
                component: ToastificationContent,
                props: {
                  title: 'Form Submitted',
                  icon: 'EditIcon',
                  text: 'Changes will be applied after logout',
                  variant: 'success',
                },
              })
            }).catch(error => {
            // Server side validation
              this.$refs.registerForm.setErrors(error.response.data)
            })
        }
      })
    },
  },
  setup() {
    const refInputEl = ref(null)
    const previewEl = ref(null)

    const { inputImageRenderer } = useInputImageRenderer(refInputEl, previewEl)

    return {
      refInputEl,
      previewEl,
      inputImageRenderer,
    }
  },
}
</script>
