<template>
  <div>
    <!-- Alert: No item found -->
    <b-alert
      variant="danger"
      :show="teamData === undefined"
    >
      <h4 class="alert-heading">
        Error fetching team data
      </h4>
      <div class="alert-body">
        No team found with this team id. Check
        <b-link
          class="alert-link"
          :to="{ name: 'apps-teams-list'}"
        >
          User List
        </b-link>
        for other teams.
      </div>
    </b-alert>

    <template v-if="teamData">
      <!-- First Row -->
      <b-row>
        <b-col>
          <team-view-team-info-card :team-data="teamData" />
        </b-col>
      </b-row>

      <b-row>
        <b-col
          cols="12"
          lg="6"
        >
          <team-view-team-timeline-card />
        </b-col>
        <b-col
          cols="12"
          lg="6"
        >
          <team-view-team-permissions-card />
        </b-col>
      </b-row>

    </template>

    <user-list
      :team-filter-prop.sync="this.$router.currentRoute.params.id"
    />
  </div>
</template>

<script>
import store from '@/store'
import router from '@/router'
import { ref, onUnmounted } from '@vue/composition-api'
import {
  BRow, BCol, BAlert, BLink,
} from 'bootstrap-vue'
import teamStoreModule from '@/views/apps/team/teamStoreModule'
import UserList from '@/views/apps/user/users-list/UsersList.vue'
import TeamViewTeamInfoCard from './TeamViewTeamInfoCard.vue'
import TeamViewTeamTimelineCard from './TeamViewTeamTimelineCard.vue'
import TeamViewTeamPermissionsCard from './TeamViewTeamPermissionsCard.vue'

export default {
  components: {
    BRow,
    BCol,
    BAlert,
    BLink,

    // Local Components
    TeamViewTeamInfoCard,
    TeamViewTeamTimelineCard,
    TeamViewTeamPermissionsCard,

    UserList,
  },
  data() {
    return { teamID: this.$router.currentRoute.params.id }
  },
  watch: {
    $route() {
      this.$router.go()
    },
  },
  setup() {
    const teamData = ref(null)

    const TEAM_APP_STORE_MODULE_NAME = 'app-team'

    // Register module
    if (!store.hasModule(TEAM_APP_STORE_MODULE_NAME)) store.registerModule(TEAM_APP_STORE_MODULE_NAME, teamStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(TEAM_APP_STORE_MODULE_NAME)) store.unregisterModule(TEAM_APP_STORE_MODULE_NAME)
    })

    store.dispatch('app-team/fetchTeam', { id: router.currentRoute.params.id })
      .then(response => {
        teamData.value = response.data
      })
      .catch(error => {
        if (error.response.status === 404) {
          teamData.value = undefined
        }
      })

    return {
      teamData,
    }
  },
}
</script>
