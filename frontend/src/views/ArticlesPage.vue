<template>
  <div>
    <h1>Articles</h1>
    <div class="grid">
      <router-link v-for="post in posts" :key="post.id" :to="`/post/${post.id}`" class="grid-item">
        <img :src="post.image" :alt="post.title">
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
    axios.get('http://localhost:8000/posts/')
      .then(response => {
        this.posts = response.data;

        // for debugging, returns post image url:
        this.posts.forEach(post => {
          console.log(`Post image URL: http://localhost:8000${post.image}`);
        });
        //

      })
      .catch(error => {
        if (error.response) {
          console.log('Status:', error.response.status);
          console.log('Data:', error.response.data);
        } else if (error.request) {
          console.log('Request:', error.request);
        } else {
          console.log('Error:', error.message);
        }
        console.log(error.config);
      })
  }
};
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Caveat:wght@500&family=Montserrat&family=Neucha&display=swap');



h1 {
  font-family: 'Caveat';  /* Use 'Architects Daughter' font */
  color: white;  /* Set text color to white */
  font-size: 7vw;  /* Increase size */
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5), 0 0 0.4em rgba(211, 211, 211, 0.2), 0 0 0.1em rgba(211, 211, 211, 0.2); /* Added for faux inner shadow */
  
}


body {
  background-image: url('~@/assets/leaf-background.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
}
.grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}


.grid-item {
  width: calc(100% / 3 - 10px); /* calculates the width for 3 items per row */
  margin: 5px;  /* for some space around each item */
  position: relative;
  display: flex; /* Added */
  justify-content: center; /* Added */
  align-items: center; /* Added */
  flex-direction: column; /* Added */
}


.grid-item img {
  width: 80%;
  height: 80%;            /* Set height to match width */
  display: block;
  object-fit: cover;       /* This line scales the image while maintaining the aspect ratio */
  position: relative;
  border-radius: 15px;
  box-shadow: inset 0 0 10px #000000;
}

.centered-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5), 0 0 0.4em rgba(211, 211, 211, 0.2), 0 0 0.1em rgba(211, 211, 211, 0.2); /* Added for faux inner shadow */
  font-family: 'Montserrat';
  font-size: 3.3vw;
  font-weight: bold;
  text-align: center;
}
</style>