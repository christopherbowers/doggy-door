<template>
  <div>
    <h1>{{ dogDetails.name }}</h1>
    <img :src="dogDetails.image" />
    <ul>
      <li>Age: {{ dogDetails.age }}</li>
      <li>Color: {{ dogDetails.color }}</li>
      <li>Description: {{ dogDetails.description }}</li>
      <li>Likes: {{ dogDetails.likes }}</li>
    </ul>
  </div>
</template>

<script>

import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'DogDetails',
  data: () => ({
    dogDetails: {},
    breed: {}
  }),
  mounted() {
    this.getDogDetails()
    // this.getBreed()
  },
  methods:{
    async getDogDetails() {
      const id = parseInt(this.$route.params.dog_id)
      const res = await axios.get(`${API_URL}/dogs/${id}`)
      this.dogDetails = res.data
    }
    // async getBreed() {
    //   const breed_url = this.dogDetails
    //   console.log(breed_url)
    //   const res = await axios.get(`${breed_url}`)
    //   this.breed = res.data.name
    // }
  }
}

</script>

<style scoped>
  img {
     height: 200px;
   }
</style>
