<template>
  <b-card>
    <b-card-header class="pb-50">
      <h5>
        Filters
      </h5>
    </b-card-header>
    <b-card-body>
      <b-row>
        <b-col
          cols="12"
          md="3"
          class="mb-md-0 mb-2"
        >
          <label>{{ $t("Date") }}</label>
          <b-form-datepicker
            id="example-datepicker"
            :value="dateFilter"
            :date-disabled-fn="dateDisabled"
            :start-weekday="1"
            today-button
            reset-button
            close-button
            :state="datePickerValidation"
            class="mb-2"
            nav-prev-year="disabled"
            @input="(val) => $emit('update:dateFilter', val)"
          />
        </b-col>
        <b-col
          cols="12"
          md="3"
          class="mb-md-0 mb-2"
        >
          <label>{{ $t("Building") }}</label>
          <v-select
            :value="workspaceFilter"
            :options="workspaceOptions"
            class="w-100"
            label="name"
            :reduce="val => val.id"
            @input="(val) => $emit('update:workspaceFilter', val)"
          />
        </b-col>
        <b-col
          cols="12"
          md="3"
          class="mb-md-0 mb-2"
        >
          <label>{{ $t("Floor") }}</label>
          <v-select
            :value="floorFilter"
            :options="floorOptions"
            class="w-100"
            label="name"
            :reduce="val => val.id"
            @input="(val) => $emit('update:floorFilter', val)"
          />
        </b-col>
        <b-col
          cols="12"
          md="3"
          class="mb-md-0 mb-2"
        >
          <label>{{ $t("Room") }}</label>
          <v-select
            :value="roomFilter"
            :options="roomOptions"
            class="w-100"
            label="name"
            :reduce="val => val.id"
            @input="(val) => $emit('update:roomFilter', val)"
          />
        </b-col>
      </b-row>
    </b-card-body>
  </b-card>
</template>

<script>
import {
  BCard, BCardHeader, BCardBody, BRow, BCol, BFormDatepicker,
} from 'bootstrap-vue'
import vSelect from 'vue-select'

export default {
  components: {
    BRow,
    BCol,
    BCard,
    BCardHeader,
    BCardBody,
    BFormDatepicker,
    vSelect,
  },
  props: {
    dateFilter: {
      type: [String, null],
      default: null,
    },
    workspaceFilter: {
      type: [Number, null],
      default: null,
    },
    floorFilter: {
      type: [Number, null],
      default: null,
    },
    roomFilter: {
      type: [Number, null],
      default: null,
    },
    workspaceOptions: {
      type: Array,
      required: true,
    },
    floorOptions: {
      type: Array,
      required: true,
    },
    roomOptions: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      test: '',
    }
  },
  computed: {
    datePickerValidation() {
      if (this.dateFilter) return true
      if (!this.roomFilter && !this.dateFilter) return null
      return !(this.roomFilter && !this.dateFilter)
    },
  },
  methods: {
    dateDisabled(ymd, date) {
      return false
      // Disable weekends (Sunday = `0`, Saturday = `6`) and
      // disable days that fall on the 13th of the month
      const weekday = date.getDay()
      const day = date.getDate()
      // Return `true` if the date should be disabled
      return weekday === 0 || weekday === 6
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/libs/vue-select.scss';
</style>
