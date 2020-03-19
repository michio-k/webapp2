<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="3">
          <v-icon>mdi-search</v-icon>
          <p>test</p>
        </v-col>
        <v-col cols="6">
          <h3>こんにちは、{{ this.$auth.$state.user.nickname }}さん!</h3>
          <!-- <v-btn @click="pingPublic">pingPublic</v-btn>
          <v-btn @click="pingPrivate">pingPrivate</v-btn>
          <p>{{ message }}</p> -->
          <p>main</p>
        </v-col>
        <v-col cols="3">
          <p>main</p>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: null
    }
  },
  mounted() {
    console.log('moutend')
  },
  methods: {
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
