import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import BlogPage from "../views/BlogPage.vue";
import PhilosophyPage from "../views/PhilosophyPage.vue";
import ReviewsPage from "../views/ReviewsPage.vue";
import SciencePage from "../views/SciencePage.vue";
import WildlifePage from "../views/WildlifePage.vue";
import UserSettingsPage from "../views/UserSettingsPage.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/blog",
    name: "BlogPage",
    component: BlogPage,
  },
  {
    path: "/philosophy",
    name: "PhilosophyPage",
    component: PhilosophyPage,
  },
  {
    path: "/reviews",
    name: "ReviewsPage",
    component: ReviewsPage,
  },
  {
    path: "/science",
    name: "SciencePage",
    component: SciencePage,
  },
  {
    path: "/wildlife",
    name: "WildlifePage",
    component: WildlifePage,
  },
  {
    path: "/user-settings",
    name: "UserSettingsPage",
    component: UserSettingsPage,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;







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

