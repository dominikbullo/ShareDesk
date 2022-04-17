<template>
  <b-sidebar
    id="add-new-user-sidebar"
    :visible="isAddNewIssueSidebarActive"
    bg-variant="white"
    sidebar-class="sidebar-lg"
    shadow
    backdrop
    no-header
    right
    @hidden="resetForm"
    @change="(val) => $emit('update:is-add-new-issue-sidebar-active', val)"
  >
    <template #default="{ hide }">
      <!-- Header -->
      <div class="d-flex justify-content-between align-items-center content-sidebar-header px-2 py-1">
        <h5 class="mb-0">
          Add New Issue
        </h5>

        <feather-icon
          class="ml-1 cursor-pointer"
          icon="XIcon"
          size="16"
          @click="hide"
        />

      </div>

      <!-- BODY -->
      <validation-observer
        #default="{ handleSubmit }"
        ref="refFormObserver"
      >
        <!-- Form -->
        <b-form
          class="p-2"
          @submit.prevent="handleSubmit(onSubmit)"
          @reset.prevent="resetForm"
        >

          <validation-provider
            #default="validationContext"
            name="Subject"
            rules="required|alpha-num"
          >
            <b-form-group
              label="Subject"
              label-for="subject"
            >
              <b-form-input
                id="subject"
                v-model="newIssueData.subject"
                autofocus
                :state="getValidationState(validationContext)"
                trim
              />

              <b-form-invalid-feedback>
                {{ validationContext.errors[0] }}
              </b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <validation-provider
            #default="validationContext"
            name="Description"
            rules="required|alpha-num"
          >
            <b-form-group
              label="Description"
              label-for="description"
            >
              <b-form-textarea
                id="description"
                v-model="newIssueData.description"
                :state="getValidationState(validationContext)"
                rows="6"
              />

              <b-form-invalid-feedback>
                {{ validationContext.errors[0] }}
              </b-form-invalid-feedback>
            </b-form-group>
          </validation-provider>

          <!-- Form Actions -->
          <div class="d-flex mt-2">
            <b-button
              variant="primary"
              class="mr-2"
              type="submit"
            >
              {{ $t("Submit") }}
            </b-button>

            <b-button
              type="button"
              variant="outline-secondary"
              @click="hide"
            >
              {{ $t("Cancel") }}
            </b-button>
          </div>

        </b-form>
      </validation-observer>
    </template>
  </b-sidebar>
</template>

<script>
import {
  BSidebar, BForm, BFormTextarea, BFormGroup, BFormInput, BFormInvalidFeedback, BButton,
} from 'bootstrap-vue'
import { ValidationProvider, ValidationObserver } from 'vee-validate'
import { ref, onUnmounted } from '@vue/composition-api'
import { required, alphaNum, email } from '@validations'
import formValidation from '@core/comp-functions/forms/form-validation'
import Ripple from 'vue-ripple-directive'
import vSelect from 'vue-select'
import store from '@/store'
import ToastificationContent from '@core/components/toastification/ToastificationContent'
import { useToast } from 'vue-toastification/composition'
import workspaceStoreModule from '../workspaceStoreModule'

export default {
  components: {
    BSidebar,
    BForm,
    BFormGroup,
    BFormInput,
    BFormTextarea,
    BFormInvalidFeedback,
    BButton,
    vSelect,

    // Form Validation
    ValidationProvider,
    ValidationObserver,
  },
  directives: {
    Ripple,
  },
  model: {
    prop: 'isAddNewIssueSidebarActive',
    event: 'update:is-add-new-user-sidebar-active',
  },
  props: {
    isAddNewIssueSidebarActive: {
      type: Boolean,
      required: true,
    },
    spotId: {
      type: [Number, String],
      required: true,
    },
  },
  data() {
    return {
      required,
      alphaNum,
      email,
    }
  },
  setup(props, { emit }) {
    const toast = useToast()

    const WORKSPACE_APP_STORE_MODULE_NAME = 'app-workspace'

    // Register module
    if (!store.hasModule(WORKSPACE_APP_STORE_MODULE_NAME)) store.registerModule(WORKSPACE_APP_STORE_MODULE_NAME, workspaceStoreModule)

    const blankIssueData = {
      subject: '',
      description: '',
      spot: props.spotId,
    }

    const newIssueData = ref(JSON.parse(JSON.stringify(blankIssueData)))
    const resetIssueData = () => {
      newIssueData.value = JSON.parse(JSON.stringify(blankIssueData))
    }

    const onSubmit = () => {
      store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/addSpotIssue`, newIssueData.value)
        .then(() => {
          toast({
            component: ToastificationContent,
            props: {
              title: 'New spot issue submitted',
              icon: 'CheckIcon',
              text: "You're issue has been submitted. Thank you!",
              variant: 'success',
            },
          })
          emit('update:is-add-new-issue-sidebar-active', false)
        }).catch(() => {
          toast({
            component: ToastificationContent,
            props: {
              title: 'Notification',
              icon: 'CheckIcon',
              text: 'Something went wrong creating new issue',
              variant: 'danger',
            },
          })
        })
    }

    const {
      refFormObserver,
      getValidationState,
      resetForm,
    } = formValidation(resetIssueData)

    return {
      newIssueData,
      onSubmit,

      refFormObserver,
      getValidationState,
      resetForm,
    }
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/libs/vue-select.scss';

#add-new-user-sidebar {
  .vs__dropdown-menu {
    max-height: 200px !important;
  }
}
</style>
