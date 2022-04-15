<template>
  <div>

    <!--    <spot-issue-list-add-new-->
    <!--      :is-add-new-issue-sidebar-active.sync="isAddNewIssueSidebarActive"-->
    <!--      :spot-id="1"-->
    <!--    />-->

    <b-card
      no-body
      class="py-2 px-1"
    >
      <!-- input search -->
      <div class="custom-search d-flex justify-content-end m-2">
        <div class="d-flex align-items-center justify-content-end">
          <b-form-input
            v-model="searchTerm"
            class="d-inline-block mr-1"
            placeholder="Search..."
          />
        </div>
      </div>

      <!-- table -->
      <vue-good-table
        :columns="tableColumns"
        :rows="issuesList"
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

          <!-- Column: Status -->
          <span v-if="props.column.field === 'status'">
            <b-badge :variant="`light-${resolveIssueStatusVariant(props.row.status).color}`">
              {{ resolveIssueStatusVariant(props.row.status).text }}
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
                  <span>{{ $t('Change status') }}</span>
                </b-dropdown-item>
                <b-dropdown-item @click="deleteIssue(props.row.id )">
                  <feather-icon
                    icon="TrashIcon"
                    class="mr-50"
                  />
                  <span>{{ $t('Delete') }}</span>
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
  </div>
</template>

<script>
import {
  BAvatar, BBadge, BButton, BCard, BPagination, BFormInput, BFormSelect, BDropdown, BDropdownItem,
} from 'bootstrap-vue'
// WARNING: VueGoodTable (3rd party - Not Vue 3 ready yet)
import {VueGoodTable} from 'vue-good-table'
import {onUnmounted, ref} from '@vue/composition-api/dist/vue-composition-api'
import ToastificationContent from '@core/components/toastification/ToastificationContent'
import axios from '@/libs/axios'
import useIssuesList from '@/views/apps/workplace/issues-list/useIssuesList'
import store from '@/store'
import workspaceStoreModule from '../workspaceStoreModule'
import SpotIssueListAddNew from './SpotIssueListAddNew.vue'

export default {
  components: {
    VueGoodTable,
    SpotIssueListAddNew,

    BAvatar,
    BBadge,
    BButton,
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
      searchTerm: '',
    }
  },
  created() {
    // This is needed because God Table not supporting Vue 3
    this.fetchIssues()
  },
  setup() {
    const WORKSPACE_APP_STORE_MODULE_NAME = 'app-workspace'

    // Register module
    if (!store.hasModule(WORKSPACE_APP_STORE_MODULE_NAME)) store.registerModule(WORKSPACE_APP_STORE_MODULE_NAME, workspaceStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(WORKSPACE_APP_STORE_MODULE_NAME)) store.unregisterModule(WORKSPACE_APP_STORE_MODULE_NAME)
    })

    const isAddNewIssueSidebarActive = ref(false)

    const {
      fetchIssues,
      issuesList,
      totalIssues,

      tableColumns,

      resolveIssueStatusVariant,
    } = useIssuesList()

    return {
      fetchIssues,
      issuesList,
      totalIssues,

      tableColumns,

      // UI
      resolveIssueStatusVariant,

      isAddNewIssueSidebarActive,
    }
  },
  methods: {
    deleteIssue(id) {
      axios.delete(`/spot-issue/${id}`)
        .then(res => {
          this.$toast({
            component: ToastificationContent,
            props: {
              title: 'Issue Deleted',
              icon: 'CheckIcon',
              variant: 'success',
            },
          })
          this.issuesList = this.issuesList.filter(el => (el.id !== id))
        })
        .catch(err => this.$toast({
          component: ToastificationContent,
          props: {
            title: 'Error',
            text: 'Cannot delete issue',
            icon: 'EditIcon',
            variant: 'danger',
          },
        }))
    },
  },
}
</script>

<style lang="scss">
@import '@/assets/scss/libs/vue-good-table.scss';
</style>
