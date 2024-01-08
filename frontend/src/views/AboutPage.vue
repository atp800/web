<template>
  <div class="video-background">
    <video playsinline autoplay muted loop>
      <source src="C:/Users/apana/OneDrive/Documents/Projects/WebsiteProject/frontend/src/assets/lion_video.mp4" type="video/mp4">
    </video>
    <div class="content">
      <h1>About Us</h1>
      <transition-group name="fade" tag="div">
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
        { name: 'Home', to: '/' },
        { name: 'Articles', to: '/articles' },
        { name: 'Documentaries', to: '/videos' },
        { name: 'About', to: '/about' },
      ],
    };
  },
};
</script>

<style scoped>
.video-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: black;
}

.video-background video {
  position: absolute;
  top: 50%;
  left: 50%;
  min-width: 100%;
  min-height: 100%;
  width: auto;
  height: auto;
  z-index: 0;
  transform: translate(-50%, -50%);
}

.content {
  position: relative;
  z-index: 1;
  color: white;
  text-align: center;
  font-size: 2em;
  margin-top: 2em;
}

.link {
  animation: fade-in 1s ease both;
  cursor: pointer;
  text-decoration: none;
  color: white;
  margin-top: 1em;
}

@keyframes fade-in {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>