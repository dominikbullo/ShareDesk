<template>
  <div
    v-if="!isTouch()"
    class="container mb-2"
  >
    <h3>{{ $t("Legend") }}:</h3>
    <b-row class="d-flex mt-1">
      <b-col
        v-for="status in seatStatuses"
        class="mr-2"
      >
        <div
          v-b-popover.hover.top="status.label"
          style="width: 1.875rem; height: 1.875rem; border: 1px solid black;"
          :class="`cls-${status.cls.toLowerCase()} mb-1`"
        />
        <p>{{ status.label }}</p>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { BCol, BRow, VBPopover } from 'bootstrap-vue'
import { seatStatuses } from '@/views/apps/reservation/reservationsUtils'
import { isTouch } from '@/utils/utils'

export default {
  components: {
    BRow,
    BCol,
  },
  directives: {
    'b-popover': VBPopover,
  },
  setup() {
    return {
      seatStatuses,
      isTouch,
    }
  },
}
</script>
