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

    <b-card>
      <b-card-header class="pb-50">
        <h5>
          Filters
        </h5>
      </b-card-header>
      <b-row>
        {{ roomData }}
        <b-col
          md="7"
          class="pt-5"
        >
          <div>
            <table>
              <tbody>
                <tr v-for="idxr, r in rows">
                  <td
                    v-for="idxc, c in cols"
                    class="pl-2"
                    style="width: 50px;"
                  >
                    <div
                      v-if="!isAisle(idxr, idxc)"
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
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>

import {
  BCard, BCardHeader, BCol, BRow,
} from 'bootstrap-vue'
import ReservationsListFilters from '@/views/apps/reservation/reservation-list/ReservationsListFilters'
import store from '@/store'
import { onUnmounted, ref } from '@vue/composition-api/dist/vue-composition-api'
import useReservationsList from '@/views/apps/reservation/reservation-list/useReservationList'
import reservationStoreModule from '@/views/apps/reservation/reservationStoreModule'

export default {
  components: {
    ReservationsListFilters,
    BCard,
    BRow,
    BCardHeader,
    BCol,
  },
  data() {
    return {
      errors: [],
      o: [],
      selectedSeat: null,
      rows: 8,
      cols: 12,
      seats: [],
      country: 'id',
      countryOption: ['test', 'test2', 'test3'],
    }
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
  created() {
    this.fetchAllWorkspaces()
  },
  mounted() {
    this.generateSeats()
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
    generateSeats() {
      for (let y = 1; y <= this.rows; ++y) {
        for (let x = 1; x <= this.cols; ++x) {
          if (!this.isAisle(y, x)) {
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
    isAisle(r, c) {
      // TODO: showing grid like this
      return false
      if (r == 3) {
        if (c >= 1 && c <= 11) {
          return true
        }
      }
      return false
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
