<template>
  <div>
  <h1>Dogs</h1>
  <DogCard
    :key="dog.id"
    v-for="dog in dogs"
    :dog="dog"
    @click.native="selectDog(dagId.id)"
  />
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL
import DogCard from '../components/DogCard'

export default {
  name: 'Dogs',
  components: {
    DogCard
  },
  data: () => ({
    dogs: []
  }),
  mounted() {
    this.getAllDogs()
  },
  methods: {
    async getAllDogs() {
      const res = await axios.get(`${API_URL}/dogs`)
      this.dogs = res.data
    }
  }

}

</script>
