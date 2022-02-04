<template>
<div>
  <h1>Doggy Door</h1>
<carousel-3d>
  <slide v-for='dog in dogs' :key="dog.id" :index="dog.id" :style='{color: myColor}'>
  <router-link :key='dog.id' to='/dogs'><img :src='dog.image' /></router-link>
  </slide>
</carousel-3d>

<h1>Welcome to Doggy Door.</h1>
<h3> Open a doggy door into their furever home </h3>
</div>


</template>

<script>
import { Carousel3d, Slide } from 'vue-carousel-3d'
import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'Home',
  components: {
    Carousel3d,
    Slide
  },
  data: () => ({
    dogs: [],
    myColor: 'white'
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

<style scoped>
slide{
  background-color:azure;
}
</style>