<template>
  <div>
    <h1>MyPage</h1>
    <p>こんにちは、{{ this.$auth.$state.user.family_name }}さん</p>
    <button v-if="this.$auth.isAuthenticated" @click="logout">Log out</button>
    <v-btn @click="logout">logout</v-btn>
    <a v-if="$auth.loggedIn" @click="$auth.logout()">Sign Off</a>
  </div>
</template>

<script>
export default {
  logout() {
    this.$auth.logout()
  }
}
</script>
