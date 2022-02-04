<template>
<div>
  <h1>Doggy Door.</h1>
<carousel-3d>
  <slide v-for='dog in dogs' :key="dog.id" :index="dog.id">
   <DogCard :dog='dog'/>
  </slide>
</carousel-3d>
</div>
</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'
import DogCard from '../components/DogCard.vue'
import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'Home',
  components: {
    Carousel3d,
    Slide,
    DogCard
  },
  data: () => ({
    dogs: []
  }),
  mounted() {
    this.getDogs()
  },
  methods: {
    async getDogs() {
      const res = await axios.get(`${API_URL}/dogs`)
      this.dogs = res.data
    },
    selectShelter(dogId) {
      this.$router.push(`dogs/${dogId}`)
    }
  }
}

</script>
