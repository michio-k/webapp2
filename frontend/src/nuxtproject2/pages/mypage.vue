<template>
  <div>
    <v-container fluid>
      <Navigation />
      <v-row>
        <v-layout align-center justify-center>
          <v-col cols="8">
            <h3>こんにちは、{{ this.$auth.$state.user.nickname }}さん!</h3>
            <!-- <p>{{ this.$auth.$state }}</p> -->
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
    onSubmit() {
      console.log('submit')
    },
    // async onSubmit() {
    //   const res = await this.$axios('/core/api/public')
    //   console.log(res)
    // },
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
