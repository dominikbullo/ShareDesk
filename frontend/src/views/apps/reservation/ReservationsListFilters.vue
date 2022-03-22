<template>
  <b-card no-body>
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
            v-model="value"
            :date-disabled-fn="dateDisabled"
            :start-weekday="1"
            class="mb-2"
            nav-prev-year="disabled"
          />
        </b-col>
        <b-col
          cols="12"
          md="3"
          class="mb-md-0 mb-2"
        >
          <label>{{ $t("Building") }}</label>
          <v-select
            :value="roleFilter"
            :options="roleOptions"
            class="w-100"
            :reduce="val => val.value"
            @input="(val) => $emit('update:roleFilter', val)"
          />
        </b-col>
        <b-col
          cols="12"
          md="3"
          class="mb-md-0 mb-2"
        >
          <label>{{ $t("Floor") }}</label>
          <v-select
            :value="planFilter"
            :options="planOptions"
            class="w-100"
            :reduce="val => val.value"
            @input="(val) => $emit('update:planFilter', val)"
          />
        </b-col>
        <b-col
          cols="12"
          md="3"
          class="mb-md-0 mb-2"
        >
          <label>{{ $t("Room") }}</label>
          <v-select
            :value="statusFilter"
            :options="statusOptions"
            class="w-100"
            :reduce="val => val.value"
            @input="(val) => $emit('update:statusFilter', val)"
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
    roleFilter: {
      type: [String, null],
      default: null,
    },
    planFilter: {
      type: [String, null],
      default: null,
    },
    statusFilter: {
      type: [String, null],
      default: null,
    },
    roleOptions: {
      type: Array,
      required: true,
    },
    planOptions: {
      type: Array,
      required: true,
    },
    statusOptions: {
      type: Array,
      required: true,
    },
  },
  methods: {
    dateDisabled(ymd, date) {
      // Disable weekends (Sunday = `0`, Saturday = `6`) and
      // disable days that fall on the 13th of the month
      const weekday = date.getDay()
      const day = date.getDate()
      // Return `true` if the date should be disabled
      return weekday === 0 || weekday === 6 || day === 13
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/libs/vue-select.scss';
</style>
