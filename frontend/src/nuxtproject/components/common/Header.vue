<template>
  <v-app-bar app clipped-left color="green" dense>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
    <v-icon class="mx-4">fab fa-youtube</v-icon>
    <v-toolbar-title class="mr-12 align-center">
      <span class="title">食事管理アプリ</span>
    </v-toolbar-title>
    <v-spacer />
    <v-row align="center" style="max-width: 500px">
      <v-text-field
        :append-icon-cb="() => {}"
        placeholder="Search..."
        single-line
        append-icon="search"
        color="white"
        hide-details
      />
    </v-row>
  </v-app-bar>
</template>
