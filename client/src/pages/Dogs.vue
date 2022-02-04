<template>
  <div className='dog-page'>
  <h2>Dogs</h2>
  <div>
    <DogCard
      :key="dog.id"
      v-for="dog in dogs"
      :dog="dog"
      @click.native="selectShelter(dog.id)"
      class="card"
    />
  </div>
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
.dog-page{
  display: flex;
  text-align: center;
  margin: auto;
}


</style>
