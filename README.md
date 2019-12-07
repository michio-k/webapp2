- 手元の環境
    - macOS Catalina v10.15.1
    - Docker version 18.09.2, build 6247962
    - docker-compose version 1.23.2, build 1110ad01

- コンテナ起動
`docker-compose up -d`

- コンテナ停止
`docker-compose stop`

- コンテナに入る
`docker exec -it backend bash`
`docker exec -it frontend sh`

- nuxtプロジェクト作成時のメモ
```
create-nuxt-app v2.12.0
✨  Generating Nuxt.js project in nuxtproject
? Project name nuxtproject
? Project description My first-class Nuxt.js project
? Author name michio-k
? Choose the package manager Npm
? Choose UI framework Vuetify.js
? Choose custom server framework None (Recommended)
? Choose Nuxt.js modules Axios
? Choose linting tools ESLint, Prettier
? Choose test framework None
? Choose rendering mode Universal (SSR)
? Choose development tools jsconfig.json (Recommended for VS Code)
```
