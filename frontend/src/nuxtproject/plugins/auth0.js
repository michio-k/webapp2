import Auth0Lock from 'auth0-lock'
import nuxtConfig from '~/nuxt.config'
const config = nuxtConfig.auth.strategies.auth0

class Auth0Util {
  showLock(container) {
    const lock = new Auth0Lock(config.client_id, config.domain, {
      container,
      closable: false,
      auth: {
        responseType: 'token id_token',
        redirectUrl: this.getBaseUrl() + '/callback',
        params: {
          scope: 'openid profile email'
        }
      }
    })
    lock.show()
  }
  getBaseUrl() {
    return `${window.location.protocol}//${window.location.host}`
  }
  isAuthenticated() {
    // const expiresAt = window.localStorage.getItem('expiresAt')
    // 後で直す
    return true
  }
  getIdToken() {
    // console.log('localstorage in getIdToken', localStorage)
    return this.isAuthenticated()
      ? localStorage.getItem('auth._token.auth0')
      : null
  }
}

export default (context, inject) => {
  inject('auth0', new Auth0Util())
}
