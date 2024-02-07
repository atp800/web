<template>
  <div class="video-background">
    <button @click="goToHome" class="home-button">
      <!-- SVG Icon for Home button -->
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home">
        <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2h-14a2 2 0 0 1-2-2z"></path>
        <polyline points="9 22 9 12 15 12 15 22"></polyline>
      </svg>
    </button>

    <video playsinline autoplay muted loop>
      <source src="/videos/multi_animal_splatter_compressed.mov" type="video/mp4">
    </video>
    <div class="blurred-border"></div>
    <div class="overlay-image"></div>
    <header class="header">
      <h1>About Us</h1>
    </header>
    <div class="content">
      <p>We started WildEye to have an excuse to spend <br> 
        hours looking at cool animals, while helping <br>
        the environment and hopefully making enough from <br>
        the site to live on.</p>
      <p>Wildlife documentaries will always be our main focus,<br>
         but we also write articles, review eco-products <br>
         and make vlogs about out journey.</p>

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
  methods: {
    goToHome() {
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Architects+Daughter&family=Caveat:wght@500&family=Montserrat&display=swap');


.video-background {
  padding-top: 9em; 
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
  padding-top: 5em; 
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


.home-button {
  position: absolute;
  top: 40px;
  left: 40px;
  background: none;
  border: none;
  cursor: pointer;
  color: #eaeaea; /* adjust to your desired color */
  z-index: 10; /* add this line */
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



.header {
  position: absolute;
  margin-bottom: 53vw;
  width: 100%;
  text-align: center;
  z-index: 5;
  color: #eaeaea;
  font-size: clamp(1.5rem, 3vw, 100px);
  font-family: 'Architects Daughter';
}
/* 
@media (min-width: 1200px) { 
  .header {
    font-size: 48px;
  }
} */

.content {
  position: relative;
  z-index: 5;
  color: #eaeaea;
  text-align: center;
  font-size: clamp(0.2rem, 3vw, 80px); 
  margin-top: -2em; 
  min-height: 900px;
  font-family: 'Nanum Pen Script';
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

/* @media (min-width: 1200px) { 
  .content {
    font-size: 42px; 
  }
} */

.link {
  display: block;
  animation: fade-in 1s ease both;
  cursor: pointer;
  text-decoration: none;
  color: #eaeaea;
  margin-bottom: 4vw; /* Adds space below each link */
  font-family: 'Nanum Pen Script';
}

@keyframes fade-in {
  0% {
    opacity: 0;
    transform: translateY(20px); /*positive 20 looks cool too*/
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>