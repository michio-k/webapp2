<template>
  <div>
    <h1>MyPage</h1>
    <h1>こんにちは、{{ this.$auth.$state.user.family_name }}さん</h1>
    <v-btn @click="$auth.logout()" color="gray">Log out</v-btn>
    <v-form ref="form">
      <v-text-field
        v-model="dishName"
        label="今、何食べてる？"
        required
      ></v-text-field>
      <v-text-field v-model="protain" label="たんぱく質"></v-text-field>
      <v-text-field v-model="fat" label="脂質" required></v-text-field>
      <v-text-field v-model="carbo" label="糖質" required></v-text-field>
      <v-file-input
        v-model="inputImage"
        label="画像アップロード"
      ></v-file-input>
    </v-form>
    <v-btn @click="onSubmit">投稿する</v-btn>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dishName: null,
      protain: 0,
      fat: 0,
      carbo: 0,
      inputImage: null
    }
  },
  methods: {
    logout() {
      this.$auth.logout()
    },
    onChange() {
      console.log('change')
    },
    onSubmit() {
      console.log('submit')
    }
  }
}
</script>
