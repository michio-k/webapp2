<template>
  <v-app>
    <h1>MyPage</h1>
    <h1>こんにちは、{{ this.$auth.$state.user.family_name }}さん</h1>
    <!-- <p>{{ this.$auth.$state.user.sub }}</p> -->
    <v-content>
      <v-form ref="form">
        <v-text-field
          v-model="dishName"
          label="今、何食べてる？"
          required
        ></v-text-field>
        <v-file-input
          v-model="uploadImage"
          @change="onChange"
          label="画像アップロード"
        ></v-file-input>
      </v-form>
      <v-btn @click="onSubmit" color="green">投稿する</v-btn>
    </v-content>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      dishName: null,
      uploadImage: null
    }
  },
  methods: {
    logout() {
      this.$auth.logout()
    },
    async onChange(file) {
      try {
        console.log(file.name)
        this.uploadImage = await this.readFileAsync(file)
      } catch (e) {
        console.log(e)
      }
    },
    readFileAsync(file) {
      console.log('readfileasync')
      const reader = new FileReader()
      reader.onload = () => {
        console.log('reader')
      }
    },
    onSubmit() {
      console.log('submit')
    }
  }
}
</script>
