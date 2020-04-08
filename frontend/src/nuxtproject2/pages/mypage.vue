<template>
  <div>
    <v-container fluid>
      <Navigation />
      <v-row>
        <v-layout align-center justify-center>
          <v-col cols="10">
            <v-card outlined tile>
              <h3>こんにちは、{{ this.$auth.$state.user.nickname }}さん!</h3>
              <!-- <p>{{ this.$auth.$state }}</p> -->
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
              <img :src="dish.tmpImage" />
            </v-card>
            <div v-for="(data, index) in postedData" :key="index">
              <v-card outlined tile>
                <v-card-text class="headline">
                  コメント: {{ data.comment }}
                </v-card-text>
                <v-card-text>投稿日時: {{ data.created_at }}</v-card-text>
                <v-card-text>更新日時: {{ data.updated_at }}</v-card-text>
                <img :src="data.image" />
                <v-card-actions>
                  <!-- 投稿を編集 -->
                  <v-btn
                    color="secondary"
                    size="x-small"
                    @click="showModal = true"
                    >編集
                  </v-btn>
                  <!-- 編集画面のモーダル -->
                  <Modal v-if="showModal" @closeModal="showModal = false" />
                  <!-- 投稿を削除 -->
                  <v-btn
                    color="accent"
                    size="x-small"
                    @click="deletePost(data[0])"
                    >削除
                  </v-btn>
                </v-card-actions>
              </v-card>
            </div>
          </v-col>
        </v-layout>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Navigation from '~/components/Navigation'
import Modal from '~/components/Modal'

export default {
  components: {
    Navigation,
    Modal
  },
  data() {
    return {
      dish: {
        comment: null,
        image: null,
        tmpImage: null
      },
      message: null,
      postedData: [],
      config: null,
      showModal: false
    }
  },
  mounted() {
    console.log('moutend')
    const url = '/core/posts/'
    const params = {
      params: { sub_id: this.$auth.user.sub }
    }
    const config = { responseType: 'arraybuffer' }
    this.$axios
      .$get(url, params)
      .then((res) => {
        for (let i = 0; i < res.length; i++) {
          const tmpData = {
            id: res[i].id,
            comment: res[i].comment,
            image: null,
            created_at: res[i].created_at.toLocaleString('ja-JP'),
            updated_at: res[i].updated_at.toLocaleString('ja-JP')
          }
          if (res[i].image !== null) {
            const imageUrl = res[i].image.replace('backend', 'localhost')
            this.$axios
              .$get(imageUrl, config)
              .then((res) => {
                const blob = new Blob([res], { type: 'image/*' })
                const blobObj = window.URL.createObjectURL(blob)
                tmpData.image = blobObj
              })
              .catch((err) => {
                console.log(err)
              })
          }
          this.postedData.unshift(tmpData)
        }
      })
      .catch((err) => {
        console.log(err)
      })
  },
  methods: {
    selectImageFile(file) {
      if (file !== undefined) {
        this.dish.image = file
        this.dish.tmpImage = window.URL.createObjectURL(file)
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
    // openModal() {
    //   this.$modal.show('modal-content')
    // },
    // closeModal() {
    //   this.$modal.hide('modal-content')
    // },
    async editPost(post) {
      console.log('edit', post)
      const url = '/core/posts/'
      const config = {
        headers: { 'content-type': 'multipart/form-data' }
      }
      const formData = new FormData()
      formData.append('sub_id', this.$auth.user.sub)
      formData.append('comment', this.dish.comment)
      formData.append('image', this.dish.image)
      await this.$axios
        .put(url + post.id, formData, config)
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    async deletePost(postId) {
      console.log('delete', postId)
      const url = '/core/posts/'
      const params = {
        params: { sub_id: this.$auth.user.sub }
      }
      await this.$axios
        .$delete(url + postId, params)
        .then((res) => {
          console.log(res)
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
      const formData = new FormData()
      formData.append('sub_id', this.$auth.user.sub)
      formData.append('comment', this.dish.comment)
      formData.append('image', this.dish.image)
      await this.$axios
        .$post(url, formData, config)
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
