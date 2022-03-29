<template>
  <div>
    <b-modal
      id="modal-add-user-to-team"
      title="Add users to team"
      :ok-title="this.$t('Add users')"
      :ok-disabled="selected.length<=0"
      cancel-variant="outline-secondary"
      centered
      @show="fetchResults"
      @hide="resetModal"
      @ok="handleOk"
    >
      <vue-autosuggest
        ref="autocomplete"
        v-model="query"
        class="mb-2"
        :suggestions="suggestions"
        :input-props="inputProps"
        :section-configs="sectionConfigs"
        :render-suggestion="renderSuggestion"
        :get-suggestion-value="getSuggestionValue"
        @input="filterOnClientSide"
      />

      <!-- media -->
      <b-media
        v-for="media in selected"
        :key="media.id"
        no-body
        class="my-1"
      >
        <b-media-aside class="mr-1">
          <b-avatar
            variant="light-primary"
            size="34"
            :src="media.avatar"
          />
        </b-media-aside>
        <b-media-body>
          <h6 class="mb-0">
            {{ media.full_name }}
          </h6>
          <small>{{ media.email }}</small>
        </b-media-body>
      </b-media>
    </b-modal>
  </div>
</template>

<script>
import {
  BButton,
  BCard,
  BCardText,
  BAvatar,
  BModal,
  VBModal,
  BForm,
  BFormInput,
  BFormGroup,
  BMedia,
  BMediaAside,
  BRow,
  BAvatarGroup,
  BMediaBody,
} from 'bootstrap-vue'
import vSelect from 'vue-select'
import Ripple from 'vue-ripple-directive'
import { VueAutosuggest } from 'vue-autosuggest'
import axios from '@/libs/axios'
import ToastificationContent from '@core/components/toastification/ToastificationContent'

export default {
  components: {
    VueAutosuggest,
    BButton,
    BModal,
    BCard,
    BCardText,
    BAvatar,
    BForm,
    BFormInput,
    BMedia,
    BMediaAside,
    BAvatar,
    BAvatarGroup,
    BMediaBody,
    BFormGroup,
    BRow,
    vSelect,
  },
  directives: {
    'b-modal': VBModal,
    Ripple,
  },
  props: {
    teamData: {
      type: Object,
      default: () => {
      },
      required: true,
    },
  },

  data() {
    return {
      query: '',
      datasuggest: [],
      selected: [],
      inputProps: {
        id: 'autosuggest__input_ajax',
        placeholder: 'Search for users by name',
        class: 'form-control',
        name: 'ajax',
      },
      suggestions: [],
      sectionConfigs: {
        users: {
          label: 'Users',
          onSelected: selected => {
            console.log(selected.item)
            this.query = ''
            this.selected.push(selected.item)
            this.filterOnClientSide()
          },
        },
      },
    }
  },
  methods: {
    handleOk() {
      axios
        .put(`/team/${this.teamData.id}`, {
          name: this.teamData.name,
          members: [...this.teamData.members, ...this.selected.map(x => x.id)],
        })
        .then(response => {
          this.$toast({
            component: ToastificationContent,
            props: {
              title: 'Notification',
              icon: 'CheckIcon',
              text: 'Users has been added to team',
              variant: 'success',
            },
          })
          this.$emit('update:team-data', response.data)
          this.$emit('refetch-data')
        })
        .catch(() => {
          this.$toast({
            component: ToastificationContent,
            props: {
              title: 'Notification',
              icon: 'AlertTriangleIcon',
              text: 'Something went wrong. Cannot add users to team',
              variant: 'danger',
            },
          })
        })
    },
    resetModal() {
      this.selected = []
    },
    fetchResults() {
      axios
        .get('/users/', {
          params: {
            teams__not: this.teamData.id,
          },
        })
        .then(response => {
          this.suggestions = []
          const users = this.filterResults(response.data.results, this.query, 'full_name')
          this.suggestions = [{ name: 'users', data: users }]
          this.datasuggest = { users: response.data.results }
          if (users.length <= 0) {
            this.$toast({
              component: ToastificationContent,
              props: {
                title: 'No users',
                icon: 'AlertTriangleIcon',
                text: 'Not found any users that can be added to this team',
                variant: 'danger',
              },
            })
          }
        })
    },
    filterOnClientSide() {
      const usersDataWithoutSelected = this.datasuggest.users.filter(item => Object.values(this.selected).filter(value => value.id === item.id).length <= 0)
      const users = this.filterResults(usersDataWithoutSelected, this.query, 'full_name')
      this.suggestions = [{ name: 'users', data: users }]
      if (users.length <= 0) {
        this.$toast({
          component: ToastificationContent,
          props: {
            title: 'No users',
            icon: 'AlertTriangleIcon',
            text: 'Not found any users that can be added to this team',
            variant: 'danger',
          },
        })
      }
    },
    filterResults(data, text, field) {
      return data.filter(item => {
        if (item[field].toLowerCase().indexOf(text.toLowerCase()) > -1) {
          return item[field]
        }
        return false
      }).sort()
    },
    renderSuggestion(suggestion) {
      if (suggestion.name === 'users') {
        const image = suggestion.item.avatar
        return (
          <div class="d-flex">
            <div>
              <b-avatar src={image} class="mr-50"></b-avatar>
            </div>
            <div>
              <span class="font-weight-bold d-block text-nowrap">{suggestion.item.full_name}</span>
              <small className="text-muted">{suggestion.item.email}</small>
            </div>
          </div>
        )
      }
      return suggestion.item
    },
    getSuggestionValue(suggestion) {
      return ''
      // const { name, item } = suggestion
      // return name === 'users' ? item.full_name : item
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/libs/vue-autosuggest.scss';
</style>
