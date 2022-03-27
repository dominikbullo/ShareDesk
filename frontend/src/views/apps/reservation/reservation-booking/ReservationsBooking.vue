<template>
  <div>
    <reservations-list-filters
      :date-filter.sync="dateFilter"
      :workspace-filter.sync="workspaceFilter"
      :floor-filter.sync="floorFilter"
      :room-filter.sync="roomFilter"
      :workspace-options="workspacesList"
      :floor-options="floorsList"
      :room-options="roomsList"
    />

    <b-card v-if="roomData">
      <b-card-header class="pb-50">
        <h5>
          {{ $t("Select spot") }}
        </h5>
      </b-card-header>
      <b-row>
        <b-col
          class="pt-5"
        >
          <div v-if="roomData.layout">
            <table>
              <tbody>
                <tr v-for="idxr, r in roomData.layout.rows">
                  <td
                    v-for="idxc, c in roomData.layout.columns"
                    class="pl-2"
                    style="width: 50px;"
                  >
                    <div
                      v-if="isEnabled(idxr, idxc)"
                      :class="classifier(idxr, idxc)"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                      @click="onSeatSelected(idxr, idxc)"
                    />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </b-col>
        <b-col
          class="pt-3"
          align-content="center"
        >
          <div
            v-show="selectedSeat"
            class="card"
            style="display: none;"
          >
            <div class="card-body">
              <div v-if="selectedSeat">
                <h3>Seat reservation data:</h3>
                <pre>{{ selectedSeat.reservationData }}</pre>
              </div>

              <ul class="list-group">
                <li
                  class="list-group-item"
                  :class="seatStatus(seatStatusString.available.full)"
                  @click="changeSeatStatus(seatStatusString.available.full)"
                >
                  <div
                    class="float-left bg-white"
                    style="width: 25px;"
                  >
                    <div
                      class="cls-fa"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                    />
                  </div>
                  <span class="px-3">Available</span>
                </li>
                <li
                  class="list-group-item"
                  :class="seatStatus(seatStatusString.booked.default)"
                  @click="changeSeatStatus(seatStatusString.booked.default)"
                >
                  <div
                    class="float-left"
                    style="width: 25px;"
                  >
                    <div
                      class="cls-rb"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                    />
                  </div>
                  <span class="px-3">Booked</span>
                </li>
                <li
                  class="list-group-item"
                  :class="seatStatus('FA')"
                  @click="changeSeatStatus('FA')"
                >
                  <div
                    class="float-left"
                    style="width: 25px;"
                  >
                    <div
                      class="cls-fa"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                    />
                  </div>
                  <span class="px-3">Reserve for Female</span>
                </li>
                <li
                  class="list-group-item"
                  :class="seatStatus('FB')"
                  @click="changeSeatStatus('FB')"
                >
                  <div
                    class="float-left"
                    style="width: 25px;"
                  >
                    <div
                      class="cls-fb"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                    />
                  </div>
                  <span class="px-3">Reserve for Female - Booked</span>
                </li>
                <li
                  class="list-group-item"
                  :class="seatStatus('MA')"
                  @click="changeSeatStatus('MA')"
                >
                  <div
                    class="float-left"
                    style="width: 25px;"
                  >
                    <div
                      class="cls-ma"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                    />
                  </div>
                  <span class="px-3">Reserve for Male</span>
                </li>
                <li
                  class="list-group-item"
                  :class="seatStatus('MB')"
                  @click="changeSeatStatus('MB')"
                >
                  <div
                    class="float-left"
                    style="width: 25px;"
                  >
                    <div
                      class="cls-mb"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                    />
                  </div>
                  <span class="px-3">Reserve for Male - Booked</span>
                </li>
              </ul>
            </div>
          </div>
          <!-- button -->
          <b-button
            v-ripple.400="'rgba(113, 102, 240, 0.15)'"
            variant="outline-primary"
            @click="modalShow = !modalShow"
          >
            {{ $t("Book for user") }}
          </b-button>

          <b-button
            v-ripple.400="'rgba(113, 102, 240, 0.15)'"
            class="ml-2"
            variant="outline-primary"
            @click="modalShow = !modalShow"
          >
            {{ $t("Book for team") }}

          </b-button>

          <!-- modal -->
          <b-modal
            v-model="modalShow"
            centered
            size="lg"
            title="Vertically Centered"
            :ok-title="$t('Book this spot')"
          >
            <b-card-text>
              Bonbon caramels muffin.
              Chocolate bar oat cake cookie pastry dragée pastry.
              Carrot cake chocolate tootsie roll chocolate bar candy canes biscuit.
              Gummies bonbon apple pie fruitcake icing biscuit apple pie jelly-o sweet roll.
              Toffee sugar plum sugar plum jelly-o jujubes bonbon dessert carrot cake.
              Cookie dessert tart muffin topping donut icing fruitcake. Sweet roll cotton candy dragée danish Candy canes chocolate bar cookie.
              Gingerbread apple pie oat cake. Carrot cake fruitcake bear claw. Pastry gummi bears marshmallow jelly-o.
            </b-card-text>
          </b-modal>
        </b-col>
      </b-row>
    </b-card>

    <b-row v-if="roomData">
      <!-- Spots pre zistenie, či je ten spot disabled alebo nie, resp pre layout-->
      <!--        <pre>{{ roomData }}</pre>-->
      <!-- roomSpotsReservationsData pre viac info o mieste + je ho classifier -->
      <!--        <pre>{{ roomSpotsReservationsData }}</pre>-->
      <b-col>
        <pre>{{ spots }}</pre>
      </b-col>
      <b-col>
        <pre>{{ reservations }}</pre>
      </b-col>
      <b-col>
        <pre>{{ seats }}</pre>
      </b-col>
    </b-row>
  </div>
</template>

<script>

import {
  BButton, BCard, BCardHeader, BCardText, BCol, BModal, BRow,
} from 'bootstrap-vue'
import store from '@/store'
import Ripple from 'vue-ripple-directive'
import { onUnmounted } from '@vue/composition-api/dist/vue-composition-api'
import { compareStringNoCaseSensitive } from '@/utils/utils'
import useReservationsList from '@/views/apps/reservation/reservation-booking/useReservationBooking'
import reservationStoreModule from '@/views/apps/reservation/reservationStoreModule'
import ReservationsListFilters from '@/views/apps/reservation/reservation-booking/ReservationsBoklingFilters.vue'

export default {
  components: {
    ReservationsListFilters,
    BCard,
    BRow,
    BCardHeader,
    BCol,
    BButton,
    BModal,
    BCardText,
  },
  directives: {
    Ripple,
  },
  data() {
    return {
      modalShow: false,
      errors: [],
      o: [],
      selectedSeat: null,
      seats: [],
    }
  },
  computed: {
    rows() {
      return this.roomData.layout.rows
    },
    cols() {
      return this.roomData.layout.columns
    },
    spots() {
      return this.roomData.spots
    },
    reservations() {
      return this.roomSpotsReservationsData
    },
  },
  setup() {
    const RESERVATIONS_APP_STORE_MODULE_NAME = 'app-workspace'

    // Register module
    if (!store.hasModule(RESERVATIONS_APP_STORE_MODULE_NAME)) store.registerModule(RESERVATIONS_APP_STORE_MODULE_NAME, reservationStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(RESERVATIONS_APP_STORE_MODULE_NAME)) store.unregisterModule(RESERVATIONS_APP_STORE_MODULE_NAME)
    })

    const {
      fetchAllWorkspaces,

      workspacesList,
      floorsList,
      roomsList,

      roomData,
      roomSpotsReservationsData,

      // Extra Filters
      dateFilter,
      workspaceFilter,
      floorFilter,
      roomFilter,
    } = useReservationsList()

    return {
      seatStatusString: {
        booked: {
          team: 'TB',
          user: 'UB',
          permanent: 'PB',
          default: 'DB',
        },
        available: {
          full: 'FA',
          partial: 'PA',
        },
      },
      fetchAllWorkspaces,

      workspacesList,
      floorsList,
      roomsList,

      roomData,
      roomSpotsReservationsData,

      // Extra Filters
      dateFilter,
      workspaceFilter,
      floorFilter,
      roomFilter,
    }
  },
  watch: {
    roomData(val) {
      // Generate seats on room data change
      if (this.roomData) this.generateSeats(val.layout.rows, val.layout.columns)
    },
    roomSpotsReservationsData() {
      // Generate seats on room roomSpotsReservationsData change
      if (this.roomData) this.generateSeats(this.roomData.layout.rows, this.roomData.layout.columns)
    },
  },
  created() {
    this.fetchAllWorkspaces()
  },
  methods: {
    getSeat(r, c) {
      for (let i = 0; i < this.seats.length; i++) {
        if (this.seats[i].position.r == r && this.seats[i].position.c == c) {
          return this.seats[i]
        }
      }
      return null
    },
    isEnabled(r, c) {
      const seat = this.getSeatFromData(r, c)
      return seat ? seat.enabled : true
    },
    resolveSeatStatusVariant(seatReservationList) {
      // TODO better decisions and statuses for example by dates, or multiple events
      const seatReservation = seatReservationList[0]

      if (seatReservation.permanent) return this.seatStatusString.booked.permanent
      if (compareStringNoCaseSensitive(seatReservation.resourcetype, 'UserSpotReservation')) return this.seatStatusString.booked.user
      if (compareStringNoCaseSensitive(seatReservation.resourcetype, 'TeamSpotReservation')) return this.seatStatusString.booked.team
      return this.seatStatusString.booked.default
    },
    generateSeats(r, c) {
      this.seats = []
      for (let y = 1; y <= r; ++y) {
        for (let x = 1; x <= c; ++x) {
          const seatReservation = this.getSeatReservationFromData(y, x)
          if (seatReservation.length > 0) {
            this.seats.push({
              position: { r: y, c: x },
              status: this.resolveSeatStatusVariant(seatReservation),
              reservationData: seatReservation,
            })
          } else {
            this.seats.push({
              position: { r: y, c: x },
              status: this.seatStatusString.available.full,
              reservationData: [],
            })
          }
        }
      }
    },
    classifier(r, c) {
      const seat = this.getSeat(r, c)
      if (seat != null) {
        if (this.selectedSeat != seat) {
          return seat.status ? `cls-${seat.status.toLowerCase()}` : 'cls-fa'
        }
        return 'cls-selected'
      }
    },
    getSeatFromData(r, c) {
      return this.spots.filter(spot => (spot.row === r && spot.column === c))[0]
    },
    getSeatReservationFromData(r, c) {
      if (!this.roomSpotsReservationsData || this.roomSpotsReservationsData.length <= 0) return []
      // Pozor na toom, lebo ten spot síce v tej rezervacií byť môže ale v inej room
      return this.roomSpotsReservationsData.filter(element => element.spots.filter(item => (item.room === this.roomFilter && item.row === r && item.column === c)).length > 0)
    },
    isInReservationData(r, c) {
      return this.roomSpotsReservationsData.filter(item => (item.spots.room === this.roomFilter && item.spots.row === r && item.spots.column === c))
    },
    isInSeatData(r, c) {
      return this.spots.filter(spot => (spot.row === r && spot.column === c)) > 0
    },
    onSeatSelected(r, c) {
      if (this.selectedSeat == this.getSeat(r, c)) {
        this.selectedSeat = null
      } else {
        this.selectedSeat = this.getSeat(r, c)
      }
    },
    seatStatus(status) {
      if (this.selectedSeat != null) {
        if (this.selectedSeat.status == status) return 'active'
      }
      return ''
    },
    changeSeatStatus(status) {
      if (this.selectedSeat != null) {
        for (let i = 0; i < this.seats.length; i++) {
          if (this.seats[i].position.r == this.selectedSeat.position.r && this.seats[i].position.c == this.selectedSeat.position.c) {
            this.seats[i].status = status
            this.selectedSeat = null
            break
          }
        }
      }
    },
  },
}
</script>

<style lang="scss">
// Core variables and mixins
@import '~@core/scss/base/bootstrap-extended/include';
// Overrides user variable
@import '~@core/scss/base/components/include';
// good table variable override to change the color of table

.full-width .card-header-tabs {
   margin-right: -21px;
   margin-left: -21px;
}

.full-width .nav-tabs .nav-item {
   margin-bottom: -1px;
   flex-grow: 1;
   text-align: center;
}
.cls-selected{background-color:$success}
.cls-tb{background-color: $secondary}
.cls-ub{background-color:$secondary; border: 2px solid $primary !important;}
.cls-pb{background-color:$danger}
.cls-db{background-color:$secondary}
.cls-fa{background-color:$light;}
.cls-pa{background-color:$light;border: 2px solid $warning !important;}
</style>
