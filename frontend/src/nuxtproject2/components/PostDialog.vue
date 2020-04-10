<template>
  <div>
    <v-dialog v-model="isDisplay" width="60%" height="auto" scrollable>
      <v-card>
        <p>{{ target }}</p>
        <p>{{ editedDish }}</p>
        <v-card-title>投稿編集</v-card-title>
        <v-card-text>投稿日時:{{ target.created_at }}</v-card-text>
        <v-card-text>更新日時:{{ target.updated_at }}</v-card-text>
        <v-text-field
          label="今、何食べてる？"
          v-model="editedDish.comment"
        ></v-text-field>
        <v-file-input
          label="画像ファイルを選択"
          accept="image/*"
          v-model="editedDish.image"
        ></v-file-input>
        <img :src="editedDish.image" />
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="secondary" size="x-small" @click="editPost(target.id)">
            編集内容を保存
          </v-btn>
          <v-btn color="secondary" size="x-small">
            編集内容をキャンセル
          </v-btn>
          <v-btn color="accent" size="x-small" @click="deletePost(target.id)">
            投稿を削除
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  props: ['target'],
  data() {
    return {
      isDisplay: false,
      editedDish: {
        comment: this.target.comment,
        image: this.target.image,
        tmpImage: null
      }
    }
  },
  methods: {
    async editPost(targetId) {
      console.log('edit', this.editedDish)
      const url = `/core/posts/${targetId}/`
      const params = {
        params: { sub_id: this.$auth.user.sub }
      }
      const formData = new FormData()
      formData.append('sub_id', this.$auth.user.sub)
      formData.append('comment', this.editedDish.comment)
      if (this.dish.image !== null) {
        formData.append('image', this.dish.image)
      }
      await this.$axios
        .$put(url, formData, params)
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
    }
  }
}
</script>
