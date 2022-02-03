<template>
  <div>
  <h2>Shelters</h2>
  <section>
    <ShelterCard
      :key="shelter.id"
      v-for="shelter in shelters"
      :shelter="shelter"
      @click.native="selectShelter(shelter.id)"
    />
  </section>
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
    },
    selectShelter(shelterId) {
      this.$router.push(`shelters/${shelterId}`)
    }
  }
}

</script>

<style scoped>

</style>
