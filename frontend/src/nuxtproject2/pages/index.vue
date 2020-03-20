<template>
  <div>
    <v-container>
      <v-row>
        <div class="title">
          <div><h1>毎日の食事を記録して、食生活を改善しよう</h1></div>
          <div><h2>Follow your favorite foods.</h2></div>
          <div><h2>improve your body for healthy.</h2></div>
          <div>
            <v-btn large>login / singnup by auth0</v-btn>
          </div>
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
  top: 25%;
  left: 20%;
  color: #ffffff;
  line-height: 300%;
}
.title h1 {
  font-size: 45px;
}
.title h2 {
  font-size: 40px;
}
.title div {
  line-height: 300%;
}
</style>
