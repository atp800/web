<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/blog">Blog</router-link> |
    <router-link to="/reviews">Reviews</router-link> |
    <router-link to="/wildlife">Wildlife</router-link> |
    <router-link to="/science">Science</router-link> |
    <router-link to="/philosophy">Philosophy</router-link> |
    <router-link to="/user-settings">Settings</router-link>
  </nav> -->
  <router-view/>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  // text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
  background: black;
  // overflow: hidden;
}
</style>
