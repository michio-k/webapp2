// export default function({ $axios, redirect }) {
//   $axios.setToken('access_token')
//   // 注: ここの引数を今は使わないからと _ とかにするとエラーになる
//   $axios.onResponse((config) => {
//     $axios.setHeader('Access-Control-Allow-Origin', '*')
//   })
// }

export default function({ $axios }) {
  $axios.onRequest((config) => {
    console.log('Making request to ' + config.url)
    console.log('config', config)
    config.headers.common.Authorization = localStorage.getItem(
      'auth._token.auth0'
    )
  })
}
