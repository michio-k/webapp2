<template>
  <el-container>
    <el-form>
      <el-button @click="loginWithAuthZero" type="primary">
        Auth0でログイン
      </el-button>
    </el-form>
  </el-container>
</template>

<script>
export default {
  created() {
    this.$auth.loginWith('auth0')
  }
}
</script>
