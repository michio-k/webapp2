<template>
  <div>
    <button @click="loginWithAuthZero">
      login
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    loginWithAuthZero() {
      this.$auth.loginWith('auth0')
    }
  }
}
</script>
