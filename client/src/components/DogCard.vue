<template>
  <div className='dog-card'>
    
    <div class="card-container">
    <img :src="dog.image"/>
    
    <h3>{{ dog.name }}</h3>
    <p>age: {{dog.age}} years old</p>
    <div className='bottom-bar'>
    <h5>{{dog.name}} likes {{dog.likes}}!</h5>
    <h5>{{dog.name}}'s message for you: {{dog.description}}</h5>
    <button @click="selectDog(dogId)">adopt me!</button>
    </div>
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

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@300&display=swap');
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Helvetica;
    text-align: center;
    
}
.dog-card {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    width: 100vw;
    text-align: center;
}
.card-container {
    margin-top: 25%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 5px solid white;
    border-radius: 25px;
    width: 455px;
    height: 590px;
    background-image: linear-gradient(to top, #ffffff, #fefeff, #fcfcfe, #fbfbfe, #f9fafe, #f8f9fd, #f6f9fd, #f5f8fc, #f4f7fb, #f3f6fb, #f1f6fa, #f0f5f9);
}

.bottom-bar {
    display: flex;
    flex-direction: column;
    border: 2px solid white;
    width: 290px;
    height: 5%;
    background-image: linear-gradient(to bottom, #f7daea, #d37fc4, #c386d3, #af8edf, #9896e8, #84a3f2, #6eaef8, #5ab9fa, #53cbfc, #60dcfb, #79ebf7, #98f9f3);
}

img {
    width: 66%;
    border: 5px solid paleturquoise;
    border-radius: 50%;
    background-color: white;
    margin-top: 10px;
}


hr {
    height:100%;
    width: 0;
    border: 1px solid white;
    position: relative;
    top: -8px;
}


.none {
    color:white;
}

</style>