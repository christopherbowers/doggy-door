<template>
  <h1>{{ shelterDetails.name }}</h1>
</template>

<script>

import axios from 'axios'

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
      const res = await axios.get(`http://localhost:8000/shelters/${id}`)
      this.shelterDetails = res.data
    }
  }
}

</script>
