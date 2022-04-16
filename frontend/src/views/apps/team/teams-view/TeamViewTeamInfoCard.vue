<template>
  <b-card>

    <b-row>

      <!-- User Info: Left col -->
      <b-col
        cols="21"
        xl="6"
        class="d-flex justify-content-between flex-column"
      >
        <div class="d-flex justify-content-start">
          <div class="d-flex flex-column ml-1">
            <div class="mb-1">
              <h4 class="mb-0">
                {{ teamData.name }}
              </h4>
              <span class="card-text">{{ teamData.email }}</span>
            </div>
            <div class="d-flex flex-wrap">
              <b-button
                :to="{ name: 'apps-users-edit', params: { id: teamData.id } }"
                variant="primary"
              >
                Edit
              </b-button>
              <b-button
                variant="outline-danger"
                class="ml-1"
              >
                Delete
              </b-button>
            </div>
          </div>
        </div>
      </b-col>

      <!-- Right Col: Table -->
      <b-col
        cols="12"
        xl="6"
      >
        <table class="mt-2 mt-xl-0 w-100">
          <tr>
            <th class="pb-50">
              <feather-icon
                icon="UserIcon"
                class="mr-75"
              />
              <span class="font-weight-bold">{{ $t('Name') }}</span>
            </th>
            <td class="pb-50">
              {{ teamData.name }}
            </td>
          </tr>
          <tr>
            <th class="pb-50">
              <feather-icon
                icon="UsersIcon"
                class="mr-75"
              />
              <span class="font-weight-bold">{{ $t('Size') }}</span>
            </th>
            <td class="pb-50 text-capitalize">
              {{ teamData.members_count }}
            </td>
          </tr>
          <tr>
            <th class="pb-50">
              <feather-icon
                icon="CalendarIcon"
                class="mr-75"
              />
              <span class="font-weight-bold">{{ $t('Creation date') }}</span>
            </th>
            <td class="pb-50 text-capitalize">
              {{ formatDate(teamData.created_at) }}
            </td>
          </tr>
        </table>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
import {
  BCard, BButton, BAvatar, BRow, BCol,
} from 'bootstrap-vue'
import { avatarText } from '@core/utils/filter'
import { formatDate } from '@/utils/filter'

export default {
  components: {
    BCard, BButton, BRow, BCol, BAvatar,
  },
  props: {
    teamData: {
      type: Object,
      required: true,
    },
  },
  setup() {
    return {
      avatarText,
      formatDate,
    }
  },
}
</script>

<style>

</style>
