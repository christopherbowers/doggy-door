<template>
  <div>
  <h2>Shelters</h2>
  <div class="card">
    <ShelterCard
      :key="shelter.id"
      v-for="shelter in shelters"
      :shelter="shelter"
      @click.native="selectShelter(shelter.id)"
      class
    />
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import ShelterCard from '../components/ShelterCard'

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
