<template>
  <div>
    <h1>こんにちは、{{ this.$auth.$state.user.nickname }}さん!</h1>
    <v-btn @click="pingPublic">pingPublic</v-btn>
    <v-btn @click="pingPrivate">pingPrivate</v-btn>
    <p>{{ message }}</p>
    <v-btn v-if="this.$auth.$state.loggedIn" @click="$auth.logout()">
      Logout
    </v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: null
    }
  },
  mounted() {
    console.log(this.$auth)
  },
  methods: {
    async pingPublic() {
      await this.$axios
        .$get('/core/api/public')
        .then((res) => {
          this.message = res
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async pingPrivate() {
      await this.$axios
        .$get('/core/api/private')
        .then((res) => {
          this.message = res
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
