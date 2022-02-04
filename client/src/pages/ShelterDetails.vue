<template>
  <h1>{{ shelterDetails.name }}</h1>
</template>

<script>

import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'ShelterDetails',
  data: () => ({
    shelterDetails: {}
  }),
  mounted() {
    this.getShelterDetails()
  },
  methods:{
    async getShelterDetails() {
      const id = parseInt(this.$route.params.shelter_id)
      const res = await axios.get(`${API_URL}/shelters/${id}`)
      this.shelterDetails = res.data
    }
  }
}

</script>
