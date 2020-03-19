<template>
  <div>
    <v-container>
      <v-row>
        <div class="title">
          <h1>毎日の食事を記録しよう！</h1>
        </div>
      </v-row>
      <!-- <v-row>
        <v-btn @click="pingPublic">pingPublic</v-btn>
        <v-btn @click="pingPrivate">pingPrivate</v-btn>
        <p>{{ message }}</p>
      </v-row> -->
    </v-container>
    <main></main>
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
    console.log(this.$auth)
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

<style>
main {
  background-image: url('~@/assets/bread-2178874_1920.jpg');
  background-position: center;
  background-size: cover;
  position: relative;
}
.title {
  position: absolute;
  top: 50%;
  left: 20%;
  color: #ffffff;
}
.title h1 {
  font-size: 40px;
}
</style>
