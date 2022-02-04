<template>
  <div id="app">
    <Nav />
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>


<script>
import Nav from './components/Nav'

export default {
  name: 'App',
  components: {
    Nav
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.card {
  cursor: pointer;
}

.card:hover {
  color: #385c80;
}

body{
  display: flex;
  justify-content: center;
  background-image: linear-gradient(to top, #ffffff, #fbfdff, #f2fcff, #e7fcff, #ddfcff, #d5fbff, #ccf9fe, #c3f8fe, #baf4fe, #b2f0fe, #aaebfe, #a3e7ff);
}

</style>
