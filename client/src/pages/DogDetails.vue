<template>
  <div>
    <h1>{{ dogDetails.name }}</h1>
    <img :src="dogDetails.image" className='dog-image'/>
    <ul>
      <li>Age: {{ dogDetails.age }}</li>
      <li>Color: {{ dogDetails.color }}</li>
      <li>Description: {{ dogDetails.description }}</li>
      <li>Likes: {{ dogDetails.likes }}</li>
    </ul>
    <button @click='deleteDog'>adopt me now!</button>
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
    },
    async deleteDog() {
      const id = parseInt(this.$route.params.dog_id)
      await axios.delete(`${API_URL}/dogs/${id}`)
      this.$router.push('/dogs')
    },
    // handleSubmit() {

    // }
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
.dog-image {
     height: 200px;
   }

li {
  list-style: none;
}
</style>
