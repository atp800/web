<template>
  <div>
    <button @click="goToHome" class="home-button">
      <!-- SVG Icon for Home button -->
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home">
        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2h-14a2 2 0 0 1-2-2z"></path>
        <polyline points="9 22 9 12 15 12 15 22"></polyline>
      </svg>
    </button>

    <h1>Articles</h1>
    <div class="grid">
      <router-link v-for="post in posts" 
                   :key="post.post_id"
                   :to="`/post/${post.post_id}`" 
                   class="grid-item">
        <img :src="post.image" 
             :alt="post.title"
             @mouseover="hoveredPost = post.post_id" 
             @mouseleave="hoveredPost = null"
             :class="hoveredPost === post.post_id ? 'fade' : ''">
             <transition-group name="fade" tag="div">
        <div class="centered-text" v-if="hoveredPost !== post.post_id">{{ post.title }}</div>
        <div class="centered-text" :key="`description-${post.post_id}`" v-if="hoveredPost === post.post_id" :style="{'font-size': isHoveredPost(post.post_id) ? '1.7vw' : '3.2vw'}">{{ shortDescription(post.description) }}</div>
              </transition-group>
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
      hoveredPost: null,
    };
  },
  methods: {
    goToHome() {
      this.$router.push('/');
    },
    setHoveredPost(id) {
      this.hoveredPost = id;
    },
    isHoveredPost(id) {
      return this.hoveredPost === id;
    },
    shortDescription(description) {
      return description.length > 150
        ? description.substring(0, 150) + '...'
        : description;
    }
  },
  
  created() {
    axios.get('http://localhost:8000/posts/')
      .then(response => {
        this.posts = response.data;

        // for debugging, returns post id and image url:
        this.posts.forEach(post => {
          console.log(`Post ID: ${post.post_id}, Post Image URL: http://localhost:8000${post.image}`);
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

@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Caveat:wght@500&family=Montserrat&family=Nanum+Pen+Script&family=Neucha&display=swap');

.home-button {
  position: absolute;
  top: 40px;
  left: 40px;
  background: none;
  border: none;
  cursor: pointer;
  color: white; /* adjust to your desired color */
}

.home-button svg {
  width: 2rem;  /* adjust size as needed */
  height: 2rem;
  opacity: 1;    /* Set original opacity */
  transition: opacity 0.15s ease-in-out; /* Smooth transition */
}

.home-button:hover svg {
  opacity: 0.5;    /* Adjust to desired opacity during hover */
}

h1 {
  font-family: 'Architects Daughter';
  color: white;
  font-size: clamp(1.5rem, 7vw, 100px);
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
  width: 60%;
  height: 80%;            /* Set height to match width */
  display: block;
  object-fit: cover;       /* This line scales the image while maintaining the aspect ratio */
  position: relative;
  border-radius: 15px;
  box-shadow: inset 0 0 10px #000000;
  aspect-ratio: 1 / 1; /* Add aspect-ratio to maintain square aspect */
  overflow: hidden; /* Make sure the image doesn't exceed the grid item */
  opacity: 1;  /* Set the initial opacity */
  transition: opacity 0.22s ease-in-out;  /* Adjust timing as needed */
}

.grid-item img.fade {
  opacity: 0.5;
}

.centered-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5), 0 0 0.4em rgba(211, 211, 211, 0.2), 0 0 0.1em rgba(211, 211, 211, 0.2); /* Added for faux inner shadow */
  font-family: 'Nanum Pen Script';
  font-size: clamp(1vw, 3.2vw, 150px);
  font-weight: bold;
  text-align: center;
  transition: font-size 0.22s ease-in-out;
  pointer-events: none; /* Added */
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.22s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.fade-enter-to, .fade-leave-from {
  opacity: 1;
}
</style>