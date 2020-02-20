<template>
  <v-app-bar app color="green" light>
    <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
    <v-toolbar-title>Application</v-toolbar-title>
    <div class="flex-grow-1"></div>
    <v-btn @click="$auth.logout()" color="gray">Log out</v-btn>
  </v-app-bar>
</template>
