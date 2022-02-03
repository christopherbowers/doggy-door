<template>
  <div @click="selectShelter(shelterId)">
    <div class="image-wrapper">
      <img :src="shelter.image_url" :alt="shelter.name" />
    </div>
    <div class="info-wrapper flex-col">
      {{ shelter.name }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShelterCard',
  props: {
    shelter: {}
  }
}
</script>
