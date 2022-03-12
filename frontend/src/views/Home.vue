<template>
  <b-row class="match-height">
    <b-col
      lg="4"
      md="6"
    >
      <card-advance-employee-task />
    </b-col>
    <b-col
      lg="4"
      md="6"
    >
      <card-advance-meetup />
    </b-col>
    <b-col
      lg="4"
      md="6"
    >
      <card-advance-profile />
    </b-col>
    <b-col
      lg="4"
      md="6"
    >
      <card-advance-transactions />
    </b-col>

    <!-- Timeline -->
    <b-col lg="8">
      <card-advance-timeline />
    </b-col>

    <b-col
      lg="4"
      md="6"
    >
      <card-advance-browser-states />
    </b-col>
  </b-row>
</template>

<script>
import {
  BCol, BRow,
} from 'bootstrap-vue'

import CardAdvanceEmployeeTask from './card/card-advance/CardAdvanceEmployeeTask.vue'
import CardAdvanceMeetup from './card/card-advance/CardAdvanceMeetup.vue'
import CardAdvanceProfile from './card/card-advance/CardAdvanceProfile.vue'
import CardAdvanceTransactions from './card/card-advance/CardAdvanceTransactions.vue'
import CardAdvanceBrowserStates from './card/card-advance/CardAdvanceBrowserStates.vue'
import CardAdvanceTimeline from './card/card-advance/CardAdvanceTimeline.vue'

export default {
  components: {
    BRow,
    BCol,

    CardAdvanceEmployeeTask,
    CardAdvanceMeetup,
    CardAdvanceProfile,
    CardAdvanceTransactions,
    CardAdvanceBrowserStates,
    CardAdvanceTimeline,
  },
}
</script>

<style>

</style>
