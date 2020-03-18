require('dotenv').config({ path: '../../.env' })

export default function({ $axios, store }) {
  // get access token
  $axios
    .post(
      'https://' + process.env.AUTH0_DOMAIN + '/oauth/token',
      { header: 'content-type: application/json' },
      {
        data: {
          client_id: process.env.AUTH0_CLIENT_ID,
          client_secret: process.env.AUTH0_CLIENT_SECRET,
          audience: process.env.API_IDENTIFIER,
          grant_type: 'client_credentials'
        }
      }
    )
    .then((res) => {
      console.log('success for getting token')
      $axios.setToken('Bearer ' + res.data.access_token)
    })
    .catch((err) => {
      console.log(err)
      $axios.setToken(null)
    })
  // exec request to api
  $axios.onRequest((config) => {
    console.log('Making request to ' + config.url)
  })
}
