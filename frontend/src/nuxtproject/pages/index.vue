<template>
  <div>
    <h2>Welcom to FoodBook!</h2>
    <v-btn @click="loginByAuth0Lock">LogIn/SignUp By Auth0-lock</v-btn>
    <v-btn @click="loginByAuth0">LogIn/SignUp By Auth0</v-btn>
    <div id="show-auth" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      token: null
    }
  },
  mounted() {
    console.log('home page')
    console.log('auth state', this.$auth.$state)
  },
  methods: {
    loginByAuth0Lock() {
      this.$auth0.showLock('show-auth')
    },
    loginByAuth0($auth) {
      this.$auth.loginWith('auth0')
    }
  }
}
</script>

<style scoped>
#show-auth {
  margin-top: 20px;
}
</style>
