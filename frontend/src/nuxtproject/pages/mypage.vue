<template>
  <div>
    <h1>MyPage</h1>
    <h1>こんにちは、{{ this.$auth.$state.user.family_name }}さん</h1>
    <v-btn @click="$auth.logout()" color="gray">Log out</v-btn>
    <h3>今、何食べてる？</h3>
    <v-form ref="form">
      <v-text-field label="料理名" required></v-text-field>
      <v-text-field label="たんぱく質" required></v-text-field>
      <v-text-field label="脂質" required></v-text-field>
      <v-text-field label="糖質" required></v-text-field>
    </v-form>
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
