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
      const res = await axios.get(`http://localhost:8000/dogs`)
      this.dogs = res.data
    }
  }

}

</script>
