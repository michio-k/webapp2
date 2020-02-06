<template>
  <div>
    <p>test</p>
  </div>
</template>

<script>
export default {
  // async asyncData({ $axios, error }) {
  //   try {
  //     // const response = await $axios.$get('http://backend:8000/core/users')
  //     const response = await $axios.$get('/core/users/')
  //     return { users: response }
  //   } catch (err) {
  //     error({
  //       statusCode: err.response.status,
  //       message: err.response.data.message
  //     })
  //   }
  // }
  async mounted() {
    const url = '/core/users/'
    const response = await this.$axios.get(url)
    // console.log(response)
    this.dat = response.data
    console.log(this.dat)
  }
}
</script>
