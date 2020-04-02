<template>
  <div>
    <v-container fluid>
      <Navigation />
      <v-row>
        <v-layout align-center justify-center>
          <v-col cols="8">
            <h3>こんにちは、{{ this.$auth.$state.user.nickname }}さん!</h3>
            <p>{{ this.$auth.$state }}</p>
            <!-- <p>{{ this.$store }}</p> -->
            <!-- <v-btn @click="pingPublic">pingPublic</v-btn>
            <v-btn @click="pingPrivate">pingPrivate</v-btn>
            <p>{{ message }}</p> -->
            <v-form ref="form">
              <v-text-field
                v-model="dish.comment"
                label="今、何食べてる？"
                required
              ></v-text-field>
              <v-file-input
                label="画像アップロード"
                accept="image/*"
                @change="selectImageFile"
              ></v-file-input>
              <div class="post-btn">
                <v-btn color="primary" @click="addUser">ユーザ追加</v-btn>
                <v-btn color="primary" @click="onSubmit">投稿</v-btn>
              </div>
            </v-form>
            <img :src="dish.image" />
          </v-col>
        </v-layout>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Navigation from '~/components/Navigation'

export default {
  components: {
    Navigation
  },
  data() {
    return {
      dish: {
        comment: null,
        image: null
      },
      message: null
    }
  },
  mounted() {
    console.log('moutend')
  },
  methods: {
    selectImageFile(file) {
      if (file !== undefined) {
        this.dish.image = window.URL.createObjectURL(file)
        console.log(file)
        // const img = new Image()
        // const reader = new FileReader()
        // const vm = this
        // reader.readAsDataURL(file)
        // reader.onload = (e) => {
        // }
        // const image = new Image()
        // const reader = new FileReader()
      } else {
        return null
      }
    },
    async addUser() {
      console.log('add user')
      const url = '/core/appusers/'
      const config = {
        headers: { 'content-type': 'application/json' }
      }
      const postData = { sub: this.$auth.user.sub }
      await this.$axios
        .$post(url, postData, config)
        .then(() => {
          console.log('success add user')
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async onSubmit() {
      const url = '/core/posts/'
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const postData = {
        sub_id: this.$auth.user.sub,
        comment: this.dish.comment,
        image: this.dish.image
      }
      console.log('postData', postData, config)
      await this.$axios
        .$post(url, postData, config)
        .then((res) => {
          console.log(res)
        })
        .catch((error) => {
          console.log(error)
        })
    },
    async pingPublic() {
      await this.$axios
        .$get('/core/api/public')
        .then((res) => {
          this.message = res
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async pingPrivate() {
      await this.$axios
        .$get('/core/api/private')
        .then((res) => {
          this.message = res
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
