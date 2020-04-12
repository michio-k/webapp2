<template>
  <div>
    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>{{ title }}</v-toolbar-title>
      <v-spacer />
      <v-btn
        v-if="!this.$auth.$state.loggedIn"
        @click="$auth.loginWith('auth0')"
        >login/signup by auth0
      </v-btn>
      <v-btn v-if="this.$auth.$state.loggedIn" @click="$auth.logout()">
        Logout
      </v-btn>
    </v-app-bar>

    <!-- <v-app-bar :clipped-left="clipped" fixed app>
      <v-row class="header">
        <v-navigation-drawer></v-navigation-drawer>
        <v-icon>home</v-icon>
        <v-toolbar-title>&nbsp;&nbsp;&nbsp;{{ title }}</v-toolbar-title>
      </v-row>
      <v-spacer />
      <v-btn
        v-if="!this.$auth.$state.loggedIn"
        @click="$auth.loginWith('auth0')"
        >login/signup
      </v-btn>
      <v-btn v-if="this.$auth.$state.loggedIn" @click="$auth.logout()">
        Logout
      </v-btn>
    </v-app-bar> -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire'
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'FoodBook'
    }
  }
}
</script>

<style>
.header {
  white-space: nowrap;
  font-size: 45sp;
}
</style>
