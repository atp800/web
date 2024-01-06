@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Montserrat&display=swap');

<template>
  <div class="video-background">
    <video playsinline autoplay muted loop>
      <source src="/videos/lion_dim_blur_1.mov" type="video/mp4">
    </video>
    <div class="blurred-border"></div>
    <div class="overlay-image"></div>
    <header class="header">
      <h1>WildEye</h1>
    </header>
    <div class="content">
      <transition-group name="fade" tag="div" class="links-container">
        <router-link 
          v-for="(link, index) in links" 
          :key="link.name" 
          :to="link.to" 
          class="link"
          :style="{ 'animation-delay': `${index * 0.2}s` }"
        >
          {{ link.name }}
        </router-link>
      </transition-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',

  data() {
    return {
      links: [
        { name: 'Blog', to: '/blog' },
        { name: 'Reviews', to: '/reviews' },
        { name: 'Wildlife', to: '/wildlife' },
        { name: 'Science', to: '/science' },
        { name: 'Philosophy', to: '/philosophy' },
        { name: 'Settings', to: '/settings' },
      ],
    };
  },
};
</script>

<style scoped>
.video-background {
  position: relative;
  width: 100%;
  height: 100%;
  background: black;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-background video {
  position: absolute;
  z-index: 1;
  width: 85%; /* adjust to desired size */
  /* keep aspect ratio */
  height: auto;
  /* Center the video */
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  line-height: 1.5; /* Adjusts the space between lines of text */
}


/* .video-background::before {
  content: "";
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  background: rgba(0, 0, 0, 0.3);
  z-index: 3;
} */


/* .video-background::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: url('/public/images/border_image_blur.png');
  background-size: 90% 80%;
  background-position: center;
  background-repeat: no-repeat;
  pointer-events: none;
  z-index: 2;
} */

/* Adjust border for smaller screens */
@media (max-width: 800px) {
  .video-background::after {
    background-size: 80% 80%;
  }
}

/* .overlay-image {
  background: url('/public/images/splatter_blur_2.png') no-repeat center center; 
  background-size: cover;
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 4;
} */



/* .blurred-border {
  position: absolute;
  top: 0; right: 0; bottom: 0; left: 0;
  border-style: solid;
  border-width: 50000vw;
  border-image-source: url('/public/images/border_image.png');
  border-image-slice: 200%;
  border-image-width: 50000vw;
  border-image-outset: 0;
  border-image-repeat: stretch;
} */



.header {
  position: absolute;
  top: 1vh;
  width: 100%;
  text-align: center;
  z-index: 5;
  color: white;
  font-size: 4vw;
  font-family: 'Montserrat';
}

@media (min-width: 1200px) { 
  .header {
    font-size: 48px; /* Adjust as needed */
  }
}

.content {
  position: relative;
  z-index: 5;
  color: white;
  text-align: center;
  font-size: 3.5vw; /* Responsive font-size */
  margin-top: 2em;  /* Responsive top-margin */
  font-family: 'Montserrat';  
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

@media (min-width: 1200px) { 
  .content {
    font-size: 42px; /* Adjust as needed */
  }
}

.link {
  display: block;
  animation: fade-in 1s ease both;
  cursor: pointer;
  text-decoration: none;
  color: white;
  margin-bottom: 4vh; /* Adds space below each link */
  font-family: 'Architects Daughter';
}

@keyframes fade-in {
  0% {
    opacity: 0;
    transform: translateY(-20px); /*positive 20 looks cool too*/
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>