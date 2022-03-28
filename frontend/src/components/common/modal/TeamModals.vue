<template>
  <div>
    <b-modal
      id="modal-add-user-to-team"
      title="Basic Modal"
      ok-title="submit"
      cancel-variant="outline-secondary"
      centered
      @click="fetchResults"
      @hide="selected=[]"
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
        @click="fetchResults"
      />

      <!-- media -->
      <b-row class="mt-5">
        <b-media
          v-for="media in selected"
          :key="media.id"
          no-body
          class="mb-1"
        >
          <b-media-aside class="mr-1">
            <b-avatar
              rounded
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
      </b-row>
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
      results: [],
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
          },
        },
      },
    }
  },
  methods: {
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
          users.length && this.suggestions.push({ name: 'users', data: users })
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
    filterResults(data, text, field) {
      // TODO: also selected
      console.log(data)
      console.log(text)
      console.log(field)
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
