<template>
  <div>
    <!-- Parallax Layer 1 (background) -->
    <div v-parallax="{ src: '/images/Background.png', speed: 0.2 }"></div>

    <!-- Navigation Menu -->
    <div id="nav-menu" style="position: absolute; top: 0; right: 0; z-index: 100;">
      <ul style="list-style-type: none; margin: 0; padding: 10px;">
        <li v-for="link in links" :key="link.name" style="display: inline; margin-right: 10px;">
          <router-link :to="link.to">{{ link.name }}</router-link>
        </li>
      </ul>
    </div>

    <!-- Content -->
    <section>
      <!-- Your content here -->
      <!-- 
        For example, add other non-parallax content or components here 
      -->
    </section>

    <!-- Parallax Layer 2 (midground) -->
    <div v-parallax="{ src: '/images/Midground.png', speed: 0.5 }"></div>

    <!-- Title Layer -->
    <div style="position: relative; z-index: 50; text-align: center; font-size: 2em; margin-top: -100px;">
      WildEye
    </div>

    <!-- Parallax Layer 3 (foreground) -->
    <div v-parallax="{ src: '/images/Foreground.png', speed: 0.8 }"></div>

    <!-- Other pages or content can follow here -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      links: [
        { name: 'Articles', to: '/articles' },
        { name: 'Documentaries', to: '/videos' },
        { name: 'About', to: '/about' },
      ],
    };
  },
};
</script>