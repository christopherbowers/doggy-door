import VueRouter from  'vue-router'
import Home from './pages/Home'
import Shelters from './pages/Shelters'
import ShelterDetails from './pages/ShelterDetails'
import Dogs from './pages/Dogs'

const routes = [
  {path: '/', component: Home, name: 'Home' },
  {path: '/shelters', component: Shelters, name: 'Shelters' },
  {path: '/shelters/:shelter_id', component: ShelterDetails, name: 'ShelterDetails' },
  {path: '/dogs', component: Dogs, name: 'Dogs'}
]

export default new VueRouter({ routes, mode: 'history' })
