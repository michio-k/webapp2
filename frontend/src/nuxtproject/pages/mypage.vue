<template>
  <div>
    <h1>MyPage</h1>
    <p>こんにちは、{{ this.$auth.$state.user.family_name }}さん</p>
    <v-btn @click="$auth.logout()">Log out</v-btn>
    <!-- <a v-if="$auth.loggedIn" @click="$auth.logout()">Sign Off</a> -->
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$auth.logout()
    }
  }
}
</script>
