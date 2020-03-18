<template>
  <v-app-bar app color="green" light>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title>Application</v-toolbar-title>
    <div class="flex-grow-1"></div>
    <div v-if="this.$auth.loggedIn">
      <v-btn @click="logoutByAuth0" color="gray">LogOut1</v-btn>
    </div>
    <v-btn @click="logoutByAuth0">LogOut2</v-btn>
  </v-app-bar>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$auth0.unsetToken()
      this.$router.replace('/')
    },
    logoutByAuth0() {
      console.log('logout')
      this.$auth.logout()
      window.location.href =
        'https://dev-gbwk1j7c.auth0.com/v2/logout?returnTo=http://localhost:3000'
    }
  }
}
</script>
