<template>
  <div>
    <v-container>
      <v-row>
        <div class="title-text">
          <div class="display-2">
            毎日の食事を記録して、食生活を改善しよう。
          </div>
          <div class="display-2">
            Follow your favorite foods.
          </div>
          <div class="display-2">
            And Improve your body for healthy.
          </div>
          <div class="login-btn">
            <v-btn
              v-if="!$auth.loggedIn"
              large
              @click="$auth.loginWith('auth0')"
            >
              login/signup by auth0
            </v-btn>
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
.title-text {
  position: absolute;
  top: 25%;
  left: 20%;
  color: #ffffff;
}
/* .title-text display-2 {
  line-height: 150%;
} */
.title-text .login-btn {
  line-height: 150%;
}
</style>
