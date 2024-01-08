<template>
  <div>
    <h1>Welcome to (travel?) blog</h1>
    <div class="grid">
      <router-link v-for="post in posts" :key="post.id" :to="`/post/${post.id}`" class="grid-item">
        <img :src="`http://localhost:8000${post.image}`" :alt="post.title">
        <div class="centered-text">{{ post.title }}</div>
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ArticlesPage',
  data() {
    return {
      posts: [],
    };
  },
  created() {
    axios.get('http://localhost:8000/articles/')
      .then(response => {
        this.posts = response.data;
      })
      .catch(error => {
        console.log(error);
      })
  }
};
</script>

<style scoped>
.grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.grid-item {
  width: calc(100% / 3 - 10px); /* calculates the width for 3 items per row */
  margin: 5px;  /* for some space around each item */
  position: relative;
}

.grid-item img {
  width: 100%;
  height: auto;
  display: block;
}

.centered-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  text-align: center;
}
</style>