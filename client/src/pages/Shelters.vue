<template>
  <div>
  <h2>Shelters</h2>
  <div>
    <ShelterCard
      :key="shelter.id"
      v-for="shelter in shelters"
      :shelter="shelter"
      @click.native="selectShelter(shelter.id)"
      class="card"
    />
  </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL
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
      const res = await axios.get(`${API_URL}/shelters`)
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
