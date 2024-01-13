import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import ArticlesPage from "../views/ArticlesPage.vue";
import PhilosophyPage from "../views/VideosPage.vue";
import ReviewsPage from "../views/AboutPage.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/articles",
    name: "ArticlesPage",
    component: ArticlesPage,
  },
  {
    path: "/videos",
    name: "VideosPage",
    component: PhilosophyPage,
  },
  {
    path: "/about",
    name: "AboutPage",
    component: ReviewsPage,
  },
  {
    path: '/articles/:slug', // use slug instead of id
    name: 'PostPage',
    component: () => import('@/views/PostPage.vue')
  },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;


  // {
  //   path: "/science",
  //   name: "SciencePage",
  //   component: SciencePage,
  // },
  // {
  //   path: "/wildlife",
  //   name: "WildlifePage",
  //   component: WildlifePage,
  // },
  // {
  //   path: "/user-settings",
  //   name: "UserSettingsPage",
  //   component: UserSettingsPage,
  // }




// const routes = [
//   {
//     path: '/',
//     name: 'home',
//     component: HomeView
//   },
//   {
//     path: '/about',
//     name: 'about',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
//   }
// ]

