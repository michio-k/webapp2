<template>
  <v-app dark>
    <Header />
    <main class="content">
      <nuxt />
    </main>
    <Footer />
  </v-app>
</template>

<script>
import Header from '~/components/common/Header'
import Footer from '~/components/common/Footer'

export default {
  components: {
    Header,
    Footer
  },
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      items: [
        {
          icon: 'mdi-apps',
          title: 'Welcome',
          to: '/'
        },
        {
          icon: 'mdi-chart-bubble',
          title: 'Inspire',
          to: '/inspire'
        }
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'Vuetify.js'
    }
  }
}
</script>
