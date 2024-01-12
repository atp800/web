<template>
  <div class="video-background">
    <video playsinline autoplay muted loop>
      <source src="/videos/multi_animal_splatter.mov" type="video/mp4">
    </video>
    <div class="blurred-border"></div>
    <div class="overlay-image"></div>
    <header class="header">
      <h1>About Us</h1>
    </header>
    <div class="content">
      <br><br><br><br>
      <p>We started WildEye to have an excuse to spend <br> 
        hours looking at cool animals, while helping <br>
        the environment and hopeullfy making enough from <br>
        the site to live on.</p>
      <p>Wildlife documentaries will always be our main focus,<br>
         but we also write articles, review eco-products <br>
         and make vlogs about out journey.</p>

         <br>
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
  name: 'AboutPage',

  data() {
    return {
      links: [
        { name: '<- Home   ', to: '/' },
        // { name: 'Posts and Reviews', to: '/articles' },
        // { name: 'Documentaries and Vlogs', to: '/videos' },
      ],
    };
  },
};
</script>

<style scoped>
/* @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Montserrat&display=swap'); */
@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Caveat:wght@500&family=Montserrat&display=swap');


.video-background {
  position: relative;
  width: 100%;
  height: 100%;
  /* background: black; */
  overflow: hidden;
  display: flex;
  flex-direction: column;
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




.header {
  position: absolute;
  margin-bottom: 50vw;
  width: 100%;
  text-align: center;
  z-index: 5;
  color: white;
  font-size: clamp(1.5rem, 4vw, 100px);
  font-family: 'Architects Daughter';
}

@media (min-width: 1200px) { 
  .header {
    font-size: 48px;
  }
}

.content {
  position: relative;
  z-index: 5;
  color: white;
  text-align: center;
  font-size: clamp(1.5rem, 5.5vw, 80px); 
  margin-top: 2em;  /* Responsive top-margin */
  min-height: 900px;
  font-family: 'Nanum Pen Script';
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
  margin-bottom: 4vw; /* Adds space below each link */
  font-family: 'Nanum Pen Script';
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