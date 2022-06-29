import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import QuestionPage from '../views/QuestionPage.vue'
import AnswerPage from '../views/AnswerPage.vue'
import ExplanationPage from'../views/ExplanationPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/question',
    name: 'QuestionPage',
    component: QuestionPage
  },
  {
    path: '/answer',
    name: 'AnswerPage',
    component: AnswerPage
  },
  {
    path: '/explanation',
    name: 'explanation',
    component: ExplanationPage
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
