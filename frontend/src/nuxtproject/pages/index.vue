<template>
  <div>
    <div class="line"></div>
    <el-menu
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
    >
      <v-btn @click="loginWithAuthZero">Log in</v-btn>
    </el-menu>
    <el-card>
      <el-container fluid fill-height>
        <nuxt />
      </el-container>
    </el-card>
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
