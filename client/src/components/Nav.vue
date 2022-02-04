<template>
  <nav>
    <router-link to="/">Home </router-link>
    <router-link to="/shelters"> Shelters </router-link>
    <router-link to="/dogs"> All Dogs </router-link>
    <router-link to="/newdog"> Add Dog </router-link>
  </nav>
</template>

<script>


export default {
  name: 'Nav'
}

</script>

<style scoped>
a {
  text-decoration: none;
  color: rgb(98, 78, 184);
  font-size: 25px;
}

a:hover {
  color: rgb(255, 255, 255);
}

nav {
  display:flex;
  justify-content: space-between;
}

</style>
