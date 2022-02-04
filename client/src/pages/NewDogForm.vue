<template>
  <div class="form-container">
     <form @submit.prevent="handleSubmit">
     <select @change="switchSelect($event)">
       <option :key="shelter.id" v-for="shelter in shelters" :value="shelter.id">
         {{ shelter.name }}
       </option>
     </select>
      <input
        @input="handleChange"
        placeholder="name"
        :value="name"
        name="name"
        type="text"
      />
      <input
        @input="handleChange"
        placeholder="Age"
        :value="age"
        name="age"
        type="number"
      />
      <select @change="switchSelect($event)">
        <option :key="breed.id" v-for="breed in breeds" :value="breed.id">
          {{ breed.name }}
        </option>
      </select>
      <input
        @input="handleChange"
        placeholder="Color"
        :value="color"
        name="color"
        type="text"
      />
      <input
        @input="handleChange"
        placeholder="description"
        :value="description"
        name="description"
        type="text"
      />
      <input
        @input="handleChange"
        placeholder="likes"
        :value="likes"
        name="likes"
        type="text"
      />
      <input
        @input="handleChange"
        placeholder="image"
        :value="image"
        name="image"
        type="text"
      />
      <button>Add</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = process.env.VUE_APP_API_URL

export default {
  name: 'NewDogForm',
  data: () => ({
    breeds: [],
    shelters: [],
    name: '',
    age: null,
    color: '',
    breed: null,
    description: '',
    likes: '',
    image: '',
    shelter: null
  }),
  mounted() {
    this.getBreeds(),
    this.getShelters()
  },
  methods: {
    async getBreeds() {
      const res = await axios.get(`${API_URL}/breeds`)
      this.breeds = res.data
    },
    async getShelters() {
      const res = await axios.get(`${API_URL}/shelters`)
      this.shelters = res.data
    },
    handleChange(e) {
      this[e.target.name] = e.target.value
      this[e.target.age] = e.target.value
      this[e.target.color] = e.target.value
      this[e.target.description] = e.target.value
      this[e.target.likes] = e.target.value
      this[e.target.image] = e.target.value
    },
    switchSelect(event) {
      this.breed = event.target.value,
      this.shelter = event.target.value
    },
    async handleSubmit() {
      axios.post(`${API_URL}/dogs/`, {
        name: this.name,
        age: this.age,
        color: this.color,
        breed_id: this.breed,
        description: this.description,
        likes: this.likes,
        image: this.image,
        shelter_id: this.shelter,
        adopted: false
      })
      this.$router.push('/dogs')
    },
  }
}
</script>
