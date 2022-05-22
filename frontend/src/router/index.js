import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import QuestionPage from '../views/QuestionPage.vue'
import AnswerPage from '../views/AnswerPage.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/question',
    name: 'question',
    component: QuestionPage
  },
  {
    path: '/answer',
    name: 'answer',
    component: AnswerPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
