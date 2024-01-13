<template>
    <div v-if="post" class="post">
      <h1>{{ post.title }}</h1>
      <img :src="post.image" :alt="post.title">
      <div v-html="post.content" class="post-content"></div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import DOMPurify from 'dompurify';
  
  export default {
    data() {
      return {
        post: null,
      };
    },
    async created() {
      const postSlug = this.$route.params.slug;
      // Fetch post from the server using postSlug
      try {
        const response = await axios.get(`/articles/${postSlug}`);
        response.data.content = DOMPurify.sanitize(response.data.content);
        this.post = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  };
  </script>


<style scoped>
.post-content {
  color: #fbf7f5;  /* Off-white color */
  text-align: left;
}
</style>