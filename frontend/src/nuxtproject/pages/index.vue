<template>
  <div>
    <h2>Welcom to FoodBook!</h2>
    <v-btn @click="loginByAuth0">LogIn/SignUp</v-btn>
    <div id="show-auth" />
  </div>
</template>

<script>
export default {
  mounted() {
    console.log('home page')
  },
  methods: {
    loginByAuth0() {
      this.$auth0.showLock('show-auth')
    }
  }
}
</script>

<style scoped>
#show-auth {
  margin-top: 20px;
}
</style>
