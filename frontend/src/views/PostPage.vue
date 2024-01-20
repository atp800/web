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

.post {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-left: 5%;  /* Adjust to your preference */
  padding-right: 5%; /* Adjust to your preference */
}
.post h1 {
  padding-top: 40px;
  padding-bottom: 20px;
  color: #fbf7f5;  /* White color */
}

.post img {
  max-width: 70%;
}

.post-content {
  padding-top: 40px;
  color: #fbf7f5;  /* Off-white color */
  width: 80%;
  /* text-align: left; */

  /* DELETE width:6.109in; FROM THE DIV STYLE LINES 
  AT THE TOP OF THE HTML CODE OF EACH ARTICLE IN CKEDITOR
  TO ALLOW TEXT OVERFLOW */
}
</style>