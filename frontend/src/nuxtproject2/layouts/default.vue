<template>
  <v-app id="inspire">
    <Navigation />
    <Header />
    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Header from '~/components/Header'
import Navigation from '~/components/Navigation'

export default {
  components: {
    Header,
    Navigation
  },
  props: {
    source: String
  },
  data: () => ({
    drawer: null
  }),
  created() {
    this.$vuetify.theme.dark = false
  }
}
</script>
