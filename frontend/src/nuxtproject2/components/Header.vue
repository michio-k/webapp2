<template>
  <v-app-bar app color="green" light>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title>Application</v-toolbar-title>
    <div class="flex-grow-1"></div>
    <div v-if="this.$auth.loggedIn">
      <v-btn @click="logoutByAuth0" color="gray">LogOut</v-btn>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  methods: {
    logoutByAuth0() {
      console.log('logout')
      this.$auth.logout()
    }
  }
}
</script>
