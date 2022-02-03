<template>
  <div @click="selectDog(dogId)">
    <div class="info-wrapper flex-col">
      {{ dog.name }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'DogCard',
  props: {
    dog: {}
  }
}
</script>
