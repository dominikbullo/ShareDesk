<template>
  <div>
    <team-list-add-new
      :is-add-new-team-sidebar-active.sync="isAddNewTeamSidebarActive"
      @refetch-data="refetchData"
    />

    <!-- Table Container Card -->
    <b-card
      no-body
      class="mb-0"
    >

      <div class="m-2">

        <!-- Table Top -->
        <b-row>

          <!-- Per Page -->
          <b-col
            cols="12"
            md="6"
            class="d-flex align-items-center justify-content-start mb-1 mb-md-0"
          >
            <label>Show</label>
            <v-select
              v-model="perPage"
              :options="perPageOptions"
              :clearable="false"
              class="per-page-selector d-inline-block mx-50"
            />
            <label>entries</label>
          </b-col>

          <!-- Search -->
          <b-col
            cols="12"
            md="6"
          >
            <div class="d-flex align-items-center justify-content-end">
              <b-form-input
                v-model="searchQuery"
                class="d-inline-block mr-1"
                placeholder="Search..."
              />
              <b-button
                variant="primary"
                @click="isAddNewTeamSidebarActive = true"
              >
                <span class="text-nowrap">Add Team</span>
              </b-button>
            </div>
          </b-col>
        </b-row>

      </div>

      <b-table
        ref="refTeamListTable"
        class="position-relative"
        :items="fetchTeams"
        responsive
        :fields="tableColumns"
        primary-key="id"
        :sort-by.sync="sortBy"
        show-empty
        empty-text="No matching records found"
        :sort-desc.sync="isSortDirDesc"
      >

        <template #cell(name)="data">
          <b-media vertical-align="center">
            <b-link
              :to="{ name: 'apps-teams-view', params: { id: data.item.id } }"
              class="font-weight-bold d-block text-nowrap"
            >
              {{ data.item.name }}
            </b-link>
            <!--            <small class="text-muted">{{ data.item.name }}</small>-->
          </b-media>
        </template>

        <!-- Column: Actions -->
        <template #cell(actions)="data">
          <b-dropdown
            variant="link"
            no-caret
          >

            <template #button-content>
              <feather-icon
                icon="MoreVerticalIcon"
                size="16"
                class="align-middle text-body"
              />
            </template>

            <b-dropdown-item
              v-b-modal:modal-add-user-to-team
              @click="teamData=data.item"
            >
              <feather-icon icon="UsersIcon" />
              <span class="align-middle ml-50">Add member</span>
            </b-dropdown-item>

            <b-dropdown-divider />

            <b-dropdown-item :to="{ name: 'apps-teams-view', params: { id: data.item.id } }">
              <feather-icon icon="FileTextIcon" />
              <span class="align-middle ml-50">Details</span>
            </b-dropdown-item>

            <b-dropdown-item @click="deleteTeamModal(data.item)">
              <feather-icon icon="TrashIcon" />
              <span class="align-middle ml-50">Delete</span>
            </b-dropdown-item>
          </b-dropdown>
        </template>

      </b-table>
      <div class="mx-2 mb-2">
        <b-row>

          <b-col
            cols="12"
            sm="6"
            class="d-flex align-items-center justify-content-center justify-content-sm-start"
          >
            <span class="text-muted">Showing {{ dataMeta.from }} to {{ dataMeta.to }} of {{
              dataMeta.of
            }} entries</span>
          </b-col>
          <!-- Pagination -->
          <b-col
            cols="12"
            sm="6"
            class="d-flex align-items-center justify-content-center justify-content-sm-end"
          >

            <b-pagination
              v-model="currentPage"
              :total-rows="totalTeams"
              :per-page="perPage"
              first-number
              last-number
              class="mb-0 mt-1 mt-sm-0"
              prev-class="prev-item"
              next-class="next-item"
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

          </b-col>

        </b-row>
      </div>
    </b-card>

    <!-- Add user to team modal-->
    <add-user-to-team
      :team-data.sync="teamData"
      @refetch-data="refetchData"
    />

  </div>
</template>

<script>
import {
  BCard, BRow, BCol, BFormInput, BButton, BTable, BMedia, BAvatar, BLink,
  BBadge, BDropdown, BDropdownItem, BPagination, BDropdownDivider,
} from 'bootstrap-vue'
import vSelect from 'vue-select'
import { ref, onUnmounted } from '@vue/composition-api'
import store from '@/store'
import AddUserToTeam from '@/components/common/modal/TeamModals.vue'
import useTeamsList from './useTeamsList'
import teamStoreModule from '../teamStoreModule'
import TeamListAddNew from './TeamListAddNew.vue'

export default {
  components: {
    TeamListAddNew,
    AddUserToTeam,

    BCard,
    BRow,
    BCol,
    BFormInput,
    BButton,
    BTable,
    BMedia,
    BAvatar,
    BLink,
    BBadge,
    BDropdown,
    BDropdownItem,
    BDropdownDivider,
    BPagination,

    vSelect,
  },
  data() {
    return {
      teamData: {},
    }
  },
  setup() {
    const TEAM_APP_STORE_MODULE_NAME = 'app-team'

    // Register module
    if (!store.hasModule(TEAM_APP_STORE_MODULE_NAME)) store.registerModule(TEAM_APP_STORE_MODULE_NAME, teamStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(TEAM_APP_STORE_MODULE_NAME)) store.unregisterModule(TEAM_APP_STORE_MODULE_NAME)
    })

    const isAddNewTeamSidebarActive = ref(false)

    const {
      fetchTeams,
      tableColumns,
      perPage,
      currentPage,
      totalTeams,
      dataMeta,
      perPageOptions,
      searchQuery,
      sortBy,
      isSortDirDesc,
      refTeamListTable,
      refetchData,

    } = useTeamsList()

    const deleteTeam = id => {
      store.dispatch(`${TEAM_APP_STORE_MODULE_NAME}/deleteTeam`, { id })
        .then(() => {
          // eslint-disable-next-line no-use-before-define
          refetchData()
        })
    }

    return {

      // Sidebar
      isAddNewTeamSidebarActive,

      fetchTeams,
      deleteTeam,
      tableColumns,
      perPage,
      currentPage,
      totalTeams,
      dataMeta,
      perPageOptions,
      searchQuery,
      sortBy,
      isSortDirDesc,
      refTeamListTable,
      refetchData,
    }
  },
  methods: {
    deleteTeamModal(item) {
      this.$bvModal
        .msgBoxConfirm('Please confirm that you want to delete everything.', {
          title: 'Please Confirm',
          size: 'sm',
          okVariant: 'danger',
          okTitle: 'Yes',
          cancelTitle: 'No',
          cancelVariant: 'outline-secondary',
          hideHeaderClose: false,
          centered: true,
        })
        .then(value => {
          if (value) this.deleteTeam(item.id)
        })
    },
  },
}
</script>

<style lang="scss" scoped>
.per-page-selector {
  width: 90px;
}
</style>

<style lang="scss">
@import '@core/scss/vue/libs/vue-select.scss';
</style>
