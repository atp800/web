<template>
  <div>
    
    

     <!-- Parallax Container for Layer 1 (background) -->
    <div class="parallax-container">
      <Parallaxy :speed="20">
        <img src="/images/Background.png" alt="Background" class="parallax-image">
      </Parallaxy>
    </div>

    <!-- Parallax Container for Layer 2 (midground) -->
    <div class="parallax-container">
      <Parallaxy :speed="50">
        <img src="/images/Midground.png" alt="Midground" class="parallax-image">
      </Parallaxy>
    </div>

    <!-- Title Layer -->
    <div style="position: relative; z-index: 50; text-align: center; font-size: 10em; margin-top: 30px;">
      WildEye
    </div>

    <!-- Parallax Container for Layer 3 (background) -->
    <div class="parallax-container">
      <Parallaxy :speed="90">
        <img src="/images/Background.png" alt="Background" class="parallax-image">
      </Parallaxy>
    </div>


    <!-- Content -->
    <section>
      <!-- Your content here -->
    </section>



    <!-- Navigation Menu -->
    <div id="nav-menu" style="position: absolute; top: 0; right: 0; z-index: 100;">
      <ul style="list-style-type: none; margin: 0; padding: 10px;">
        <li v-for="link in links" :key="link.name" style="display: inline; margin-right: 10px;">
          <router-link :to="link.to">{{ link.name }}</router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import Parallaxy from '@lucien144/vue3-parallaxy';

const links = [
  { name: 'Articles', to: '/articles' },
  { name: 'Documentaries', to: '/videos' },
  { name: 'About', to: '/about' },
];
</script>

<style>
/* Wrapper for the entire parallax content */
.parallax-wrapper {
  position: relative;
  overflow: hidden;
  height: 100vh; /* Full viewport height */
}

/* Parallax containers */
.parallax-container {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  overflow: hidden;
}

.parallax-image {
  width: 100%;
  height: auto; /* Adjust this as needed to maintain aspect ratio */
  object-fit: cover;
  object-position: center;
}

/* Navigation menu styles */
#nav-menu {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 100;
}

#nav-menu ul {
  list-style-type: none;
  margin: 0;
  padding: 10px;
}

#nav-menu li {
  display: inline;
  margin-right: 10px;
}

/* Title layer styles */
.title-layer {
  position: absolute;
  z-index: 50; /* Adjust z-index as needed */
  text-align: center;
  font-size: 2em;
  width: 100%;
  top: 50%; /* Center vertically */
  left: 50%;
  transform: translate(-50%, -50%); /* Center horizontally */
}
</style>