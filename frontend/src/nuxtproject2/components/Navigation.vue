<template>
  <v-navigation-drawer v-model="drawer" app clipped>
    <v-list>
      <v-list-item @click="clickHome">
        <v-list-item-action>
          <v-icon>home</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          Home
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="clickHome">
        <v-list-item-action>
          <v-icon>dashboard</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Dashboard</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item @click="clickSetting">
        <v-list-item-action>
          <v-icon>settings</v-icon>
        </v-list-item-action>
        <v-list-item-content>
          <v-list-item-title>Settings</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      drawer: false
    }
  },
  methods: {
    clickHome() {
      console.log('clicked home')
    },
    clickSetting() {
      console.log('clicked setting')
    }
  }
}
</script>
