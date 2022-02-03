import VueRouter from  'vue-router'
import Home from './pages/Home'
import Shelters from './pages/Shelters'
// import AllDogs from './pages/AllDogs'

const routes = [
  {path: '/', component: Home, name: 'Home' },
  {path: '/shelters', component: Shelters, name: 'Shelters' },
]

export default new VueRouter({ routes, mode: 'history' })
