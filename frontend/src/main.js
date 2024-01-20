import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import Vue from 'vue';
// import VueParallaxJs from 'vue-parallax-js';

// If you're using a default export Vue component:
// Vue.use(VueParallaxJs);
// If you're using named exports or a library without default exports:
// Vue.use(VueParallaxJs, { someOption: true });


const app = createApp(App);

app.use(router);

app.mount('#app');