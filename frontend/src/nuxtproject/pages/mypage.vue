<template>
  <v-app>
    <h1>MyPage</h1>
    <h1>こんにちは、{{ this.$auth.$state.user.family_name }}さん</h1>
    <!-- <p>{{ this.$auth.$state.user.sub }}</p> -->
    <v-form ref="form">
      <v-text-field
        v-model="dish.comment"
        label="今、何食べてる？"
        required
      ></v-text-field>
      <v-file-input
        v-model="dish.image"
        @change="onChange"
        label="画像アップロード"
      ></v-file-input>
      <div class="post-btn">
        <v-btn @click="onSubmit" color="primary">投稿</v-btn>
      </div>
    </v-form>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      dish: {
        comment: null,
        image: null
      }
    }
  },
  async asyncData({ $axios }) {
    console.log('asyncdata')
    const url = '/core/posts/1'
    const response = await $axios.$get(url)
    console.log(response)
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
    async onSubmit() {
      // const url = '/core/posts/1'
      // const config = {
      //   headers: { 'content-type': 'multipart/form-data' }
      // }
      // const formData = new FormData()
      // for (const data in this.dish) {
      //   console.log(data, this.dish[data])
      //   this.formData.append(data, this.dish[data])
      // }
      const formData = {
        comment: this.dish.comment,
        image: this.dish.image
      }
      console.log('onSubmit')
      console.log('formData', formData)
      // const res = await this.$axios.$get(url)
      // console.log(res)
      // try {
      //   // const res = await this.$axios.$post(url, formData, config)
      //   const response = await $axios.$get(url)
      //   console.log(response)
      // } catch (error) {
      //   console.log(error)
      // }
      const url = '/core/posts/2'
      const response = await this.$axios.$get(url)
      // .then((response) => {
      //   console.log('success')
      //   console.log(response)
      // })
      // .catch((error) => {
      //   console.log('errorだよ')
      //   console.log(error)
      // })
      console.log(response)
    }
  }
}
</script>
