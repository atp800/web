<template>
  <div class="homepage">
    
    <!-- Static Image Container -->
    <div class="image-container">
      <img src="/images/Homepage1.png" alt="Background" class="static-image">
    </div>

    <!-- Tagline Container 
    <div class="tagline">
      Unveiling Nature: Wildlife Documentaries, Eco-Reviews and Science for a Sustainable Life
    </div>-->
    
    <!-- Navigation Menu -->
    <div id="nav-menu">
      <ul>
        <li v-for="link in links" :key="link.name">
          <router-link :to="link.to">{{ link.name }}</router-link>
        </li>
      </ul>
    </div>

  </div>
</template>


<script setup>
const links = [
  { name: 'Articles', to: '/articles' },
  { name: 'Videos', to: '/videos' },
  { name: 'About', to: '/about' },
];
</script>


<style>
/* Styles for the homepage */
.homepage {
  position: relative;
  height: 100vh; /* Full viewport height */
  background-color: black; /* Fallback color */
  overflow: hidden;
}

/* Static Image Container Styles */
.image-container {
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.static-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
}

/* Navigation menu styles */
#nav-menu {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 100;
  font-family: "urw-form", sans-serif;
  font-weight: 700;
  font-style: normal;
}

#nav-menu ul {
  list-style-type: none;
  margin: 0;
  padding: 10px;
  /* Align menu to the right */
  text-align: right;
}

#nav-menu li {
  display: inline;
  margin-right: 20px; /* Increase spacing between links */
}

/* Make sure all links inside #nav-menu are styled */
#nav-menu a {
  color: #eaeaea; /* Sets the desired text color for the links */
  text-decoration: none; /* Removes the underline from links */
  font-size: 1.5rem; /* Increases the font size */
  font-weight: 700; /* Optional: if you want to make the text bold */
  padding: 5px 10px; /* Optional: if you want to increase the clickable area for better UX */
}


/* .tagline {
  position: absolute;
  bottom: 23.7vh;
  left: 50%;
  transform: translateX(-50%);
  color: #eaeaea; 
  font-family: "urw-form", sans-serif; 
  font-size: max(calc(1rem + 1vw), 10px);
  font-style: italic;
  text-align: center; 
  max-width: 100%; 
  z-index: 10;
  padding:0;
  margin:0;

} */
</style>