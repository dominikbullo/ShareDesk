<template>
  <div>
    <b-modal
      id="modal-add-user-to-team"
      title="Basic Modal"
      ok-title="submit"
      cancel-variant="outline-secondary"
      centered
    >
      {{ teamData }}
      <vue-autosuggest
        ref="autocomplete"
        v-model="query"
        :suggestions="suggestions"
        :input-props="inputProps"
        :section-configs="sectionConfigs"
        :render-suggestion="renderSuggestion"
        :get-suggestion-value="getSuggestionValue"
        @input="fetchResults"
      />

      <pre>{{ JSON.stringify(selected, null, 4) }}</pre>

    </b-modal>
  </div>
</template>

<script>
import {
  BButton, BCard, BCardText, BAvatar, BModal, VBModal, BForm, BFormInput, BFormGroup,
} from 'bootstrap-vue'
import vSelect from 'vue-select'
import Ripple from 'vue-ripple-directive'
import { VueAutosuggest } from 'vue-autosuggest'
import axios from '@/libs/axios'

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
      timeout: null,
      selected: null,
      debounceMilliseconds: 250,
      usersUrl: 'https://jsonplaceholder.typicode.com/users',
      photosUrl: 'https://jsonplaceholder.typicode.com/photos',
      inputProps: {
        id: 'autosuggest__input_ajax',
        placeholder: 'Do you feel lucky, punk?',
        class: 'form-control',
        name: 'ajax',
      },
      suggestions: [],
      sectionConfigs: {
        destinations: {
          limit: 6,
          label: 'Destination',
          onSelected: selected => {
            this.selected = selected.item
          },
        },
        hotels: {
          limit: 6,
          label: 'Hotels',
          onSelected: selected => {
            this.selected = selected.item
          },
        },
      },
    }
  },
  methods: {
    fetchResults() {
      const { query } = this

      clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        const photosPromise = axios.get(this.photosUrl)
        const usersPromise = axios.get(this.usersUrl)

        Promise.all([photosPromise, usersPromise]).then(values => {
          this.suggestions = []
          this.selected = null

          const photos = this.filterResults(values[0].data, query, 'title')
          const users = this.filterResults(values[1].data, query, 'name')
          users.length && this.suggestions.push({ name: 'destinations', data: users })
          photos.length && this.suggestions.push({ name: 'hotels', data: photos })
        })
      }, this.debounceMilliseconds)
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
      if (suggestion.name === 'hotels') {
        const image = suggestion.item
        return (
          <div class="d-flex">
            <div>
              <b-avatar src={image.thumbnailUrl} class="mr-50"></b-avatar>
            </div>
            <div>
              <span>{image.title}</span>
            </div>
          </div>
        )
      }
      return suggestion.item.name
    },
    getSuggestionValue(suggestion) {
      const { name, item } = suggestion
      return name === 'hotels' ? item.title : item.name
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/libs/vue-autosuggest.scss';
</style>
