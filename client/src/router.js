import VueRouter from  'vue-router'
import Home from './pages/Home'
import Shelters from './pages/Shelters'
import ShelterDetails from './pages/ShelterDetails'
import Dogs from './pages/Dogs'
import DogDetails from './pages/DogDetails'

const routes = [
  {path: '/', component: Home, name: 'Home' },
  {path: '/shelters', component: Shelters, name: 'Shelters' },
  {path: '/shelters/:shelter_id', component: ShelterDetails, name: 'ShelterDetails' },
  {path: '/dogs', component: Dogs, name: 'Dogs'},
  {path: '/dogs/:dog_id', component: DogDetails, name: 'DogDetails'},
]

export default new VueRouter({ routes, mode: 'history' })
