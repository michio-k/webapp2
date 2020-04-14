# FROM node:12.13-alpine
FROM node:13.7-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && \
    apk upgrade && \
    apk add git && \
    apk add curl
RUN apk add python make g++
RUN npm install -g npm && \
    npm install -g core-js@latest && \
    npm install -g @vue/cli && \
    npm install -g @vue/cli-init && \
    npm install -g nuxt create-nuxt-app && \
    npm install -g eslint && \
    npm install -g @nuxtjs/auth && \
    npm install -g @mdi/font -D && \
    npm install -g @nuxtjs/dotenv

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV HOST 0.0.0.0
EXPOSE 3000

# for production
# CMD [ "npm", "prod" ]