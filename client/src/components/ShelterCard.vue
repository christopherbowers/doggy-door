<template>
  <div @click="selectShelter(shelterId)">
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
