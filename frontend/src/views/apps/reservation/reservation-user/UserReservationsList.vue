<template>
  <b-card
    no-body
    class="py-2 px-1"
  >
    <!-- input search -->
    <div class="custom-search d-flex justify-content-end mb-2">
      <b-form-group>
        <div class="d-flex align-items-center">
          <b-form-input
            v-model="searchTerm"
            placeholder="Search..."
            type="text"
            class="d-inline-block"
          />
        </div>
      </b-form-group>
    </div>

    <!-- table -->
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :search-options="{
        enabled: true,
        externalQuery: searchTerm }"
      :pagination-options="{
        enabled: true,
        perPage:pageLength
      }"
    >
      <template
        slot="table-row"
        slot-scope="props"
      >

        <!-- Column: Name -->
        <div
          v-if="props.column.field === 'permanent'"
        >

          <feather-icon
            :icon="props.row.permanent ? 'CheckIcon' : 'XIcon'"
            size="20"
            class="mx-1"
            :class="props.row.permanent ? 'text-success' : 'text-danger' "
          />

        </div>

        <!-- Column: Status -->
        <span v-else-if="props.column.field === 'status'">
          <b-badge :variant="statusVariant(props.row.status)">
            {{ props.row.status }}
          </b-badge>
        </span>

        <!-- Column: Action -->
        <span v-else-if="props.column.field === 'action'">
          <span>
            <b-dropdown
              variant="link"
              toggle-class="text-decoration-none"
              no-caret
            >
              <template v-slot:button-content>
                <feather-icon
                  icon="MoreVerticalIcon"
                  size="16"
                  class="text-body align-middle mr-25"
                />
              </template>
              <b-dropdown-item>
                <feather-icon
                  icon="Edit2Icon"
                  class="mr-50"
                />
                <span>Edit</span>
              </b-dropdown-item>
              <b-dropdown-item>
                <feather-icon
                  icon="TrashIcon"
                  class="mr-50"
                />
                <span>Delete</span>
              </b-dropdown-item>
            </b-dropdown>
          </span>
        </span>

        <!-- Column: Common -->
        <span v-else>
          {{ props.formattedRow[props.column.field] }}
        </span>
      </template>

      <!-- pagination -->
      <template
        slot="pagination-bottom"
        slot-scope="props"
      >
        <div class="d-flex justify-content-between flex-wrap">
          <div class="d-flex align-items-center mb-0 mt-1">
            <span class="text-nowrap">
              Showing 1 to
            </span>
            <b-form-select
              v-model="pageLength"
              :options="['3','5','10']"
              class="mx-1"
              @input="(value)=>props.perPageChanged({currentPerPage:value})"
            />
            <span class="text-nowrap "> of {{ props.total }} entries </span>
          </div>
          <div>
            <b-pagination
              :value="1"
              :total-rows="props.total"
              :per-page="pageLength"
              first-number
              last-number
              align="right"
              prev-class="prev-item"
              next-class="next-item"
              class="mt-1 mb-0"
              @input="(value)=>props.pageChanged({currentPage:value})"
            >
              <template #prev-text>
                <feather-icon
                  icon="ChevronLeftIcon"
                  size="18"
                />
              </template>
              <template #next-text>
                <feather-icon
                  icon="ChevronRightIcon"
                  size="18"
                />
              </template>
            </b-pagination>
          </div>
        </div>
      </template>
    </vue-good-table>
  </b-card>
</template>

<script>

import axios from '@/libs/axios'
import { VueGoodTable } from 'vue-good-table'
import {
  BAvatar,
  BBadge,
  BButton,
  BCard,
  BFormGroup,
  BDropdown,
  BDropdownItem,
  BFormInput,
  BFormSelect,
  BPagination,
} from 'bootstrap-vue'

export default {
  components: {
    VueGoodTable,

    BAvatar,
    BBadge,
    BButton,
    BFormGroup,
    BCard,
    BPagination,
    BFormInput,
    BFormSelect,
    BDropdown,
    BDropdownItem,
  },
  data() {
    return {
      pageLength: 10,
      test: '123',
      columns: [
        {
          label: this.$t('Start'),
          field: 'reservation.datetime_from',
          type: 'date',
          dateInputFormat: 'yyyy-MM-dd\'T\'HH:mm:ss\'Z\'',
          dateOutputFormat: 'dd.MM.yyyy HH:mm',
          filterOptions: {
            enabled: true,
            placeholder: 'Search Email',
          },
        },
        {
          label: this.$t('End'),
          field: 'reservation.datetime_to',
          type: 'date',
          dateInputFormat: 'yyyy-MM-dd\'T\'HH:mm:ss\'Z\'',
          dateOutputFormat: 'dd.MM.yyyy HH:mm',
          filterOptions: {
            enabled: true,
            placeholder: 'Search Email',
          },
        },
        {
          label: 'Name',
          field: 'spots',
          filterOptions: {
            enabled: true,
            placeholder: 'Search Name',
          },
        },
        {
          label: this.$t('Permanent'),
          field: 'permanent',
          tdClass: 'text-center',
          filterOptions: {
            enabled: true,
            placeholder: 'Search Email',
          },
        },
        {
          label: this.$t('Type'),
          field: 'resourcetype',
          filterOptions: {
            enabled: true,
            placeholder: 'Search Status',
          },
        },
        // {
        //   label: this.$t('Reservation to'),
        //   field: 'reservation_for',
        //   filterOptions: {
        //     enabled: true,
        //     placeholder: 'Search Status',
        //   },
        // },
        {
          label: 'Action',
          field: 'action',
        },
      ],
      rows: [],
      searchTerm: '',
    }
  },
  computed: {
    statusVariant() {
      const statusColor = {
        /* eslint-disable key-spacing */
        booked: 'light-danger',
        broken: 'light-warning',
        free: 'light-success',
        permanent: 'light-primary',
        // broken: 'light-info',
        /* eslint-enable key-spacing */
      }

      return status => statusColor[status]
    },
  },
  created() {
    return new Promise((resolve, reject) => {
      axios
        .get('/reservations/my_reservations/')
        .then(response => {
          this.rows = response.data
          resolve(response)
        })
        .catch(error => reject(error))
    })
  },
}
</script>

  <style lang="scss">
    @import '@core/scss/vue/libs/vue-good-table.scss';
  </style>
</template>
