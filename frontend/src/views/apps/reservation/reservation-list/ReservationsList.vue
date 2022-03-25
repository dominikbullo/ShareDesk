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
        <!--        <pre>{{ roomData }}</pre>-->
        <pre>{{ roomData.spots }}</pre>
        <pre>{{ roomData.layout }}</pre>
        <b-col
          md="7"
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
                    <!--                      v-if="!isEnabled(idxr, idxc)"-->
                    <div
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
          md="5"
          class="pt-3"
          align-content="center"
        >
          <div
            v-show="selectedSeat !=null"
            class="card"
            style="display: none;"
          >
            <div class="card-body">
              <ul class="list-group">
                <li
                  class="list-group-item"
                  :class="seatStatus('RA')"
                  @click="changeSeatStatus('RA')"
                >
                  <div
                    class="float-left bg-white"
                    style="width: 25px;"
                  >
                    <div
                      class="cls-ra"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                    />
                  </div>
                  <span class="px-3">Available</span>
                </li>
                <li
                  class="list-group-item"
                  :class="seatStatus('RB')"
                  @click="changeSeatStatus('RB')"
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
  </div>
</template>

<script>

import {
  BButton, BCard, BCardHeader, BCardText, BCol, BModal, BRow,
} from 'bootstrap-vue'
import ReservationsListFilters from '@/views/apps/reservation/reservation-list/ReservationsListFilters'
import store from '@/store'
import { onUnmounted, ref, watch } from '@vue/composition-api/dist/vue-composition-api'
import useReservationsList from '@/views/apps/reservation/reservation-list/useReservationList'
import reservationStoreModule from '@/views/apps/reservation/reservationStoreModule'
import BCardCode from '@core/components/b-card-code'
import Ripple from 'vue-ripple-directive'

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

      // Extra Filters
      dateFilter,
      workspaceFilter,
      floorFilter,
      roomFilter,
    } = useReservationsList()

    return {
      fetchAllWorkspaces,

      workspacesList,
      floorsList,
      roomsList,

      roomData,

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
      this.generateSeats(val.layout.rows, val.layout.columns)
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
    generateSeats(r, c) {
      for (let y = 1; y <= r; ++y) {
        for (let x = 1; x <= c; ++x) {
          if (this.isInData(y, x)) {
            // TODO: selecting first one -> resolve if conflict
            const seat = this.getSeatFromData(y, x)[0]
            console.log(seat)
            this.seats.push({
              position: { r: seat.row, c: seat.column },
              status: seat.status,
            })
          } else {
            this.seats.push({
              position: { r: y, c: x },
              status: 'RA',
            })
          }
        }
      }
    },
    classifier(r, c) {
      const seat = this.getSeat(r, c)
      // console.log(seat.position.r)
      // console.log(seat.position.c)
      // if (this.selectedSeat) {
      //   console.log(this.selectedSeat.position.r)
      //   console.log(this.selectedSeat.position.c)
      //   console.log(this.selectedSeat.status)
      // }
      // console.log(this.selectedSeat)
      if (seat != null) {
        if (this.selectedSeat != seat) {
          switch (seat.status) {
            case 'RA':
              return 'cls-ra'
            case 'RB':
              return 'cls-rb'
            case 'FA':
              return 'cls-fa'
            case 'FB':
              return 'cls-fb'
            case 'MA':
              return 'cls-ma'
            case 'MB':
              return 'cls-mb'
            default:
              return 'cls-ra'
          }
        }
        return 'cls-selected'
      }
    },
    getSeatFromData(r, c) {
      // "enabled": true,
      // "row": 1,
      // "column": 1,
      return this.spots.filter(spot => (spot.row === r && spot.column === c && spot.enabled === true))
    },
    isInData(r, c) {
      return this.getSeatFromData(r, c).length > 0
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
.full-width .card-header-tabs {
   margin-right: -21px;
   margin-left: -21px;
}

.full-width .nav-tabs .nav-item {
   margin-bottom: -1px;
   flex-grow: 1;
   text-align: center;
}
.cls-selected{background-color:green;}
.cls-ra{background-color:#fff;}
.cls-rb{background-color:gray;}
.cls-fa{background-color:#fff; border: 2px solid pink !important;}
.cls-fb{background-color:pink;}
.cls-ma{background-color:#fff;border: 2px solid royalblue !important;}
.cls-mb{background-color:royalblue;}
</style>
