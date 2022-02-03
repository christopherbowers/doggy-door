<template>
  <div>
    <ShelterCard
      :key="shelter.id"
      v-for="shelter in shelters"
      :shelter="shelter"
    />
  </div>
</template>

<script>
import axios from 'axios'

import ShelterCard from '../components/ShelterCard'
console.log(ShelterCard)

export default {
  name: 'Shelters',
  components: {
    ShelterCard
  },
  data: () => ({
    shelters: []
  }),
  mounted() {
    this.getShelters()
  },
  methods: {
    async getShelters() {
      const res = await axios.get(`http://localhost:8000/shelters`)
      this.shelters = res.data
    }
  }
}

</script>

<style scoped>

</style>
