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
    const res = await $axios.$get('https://icanhazip.com')
    // const res = await $axios.$get('/core/api/public')
    console.log(res)
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
      const url = '/core/posts/'
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      // const formData = new FormData()
      // formData.append('comment', this.dish.comment)
      // formData.append('image', this.dish.image)
      // for (const data in this.dish) {
      //   console.log(data, this.dish[data])
      //   formData.append(data, this.dish[data])
      // }
      const formData = {
        comment: this.dish.comment,
        image: this.dish.image
      }
      console.log('formData', formData, config)
      const response = await this.$axios
        .$post(url, formData, config)
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
      console.log(response)
    }
  }
}
</script>
