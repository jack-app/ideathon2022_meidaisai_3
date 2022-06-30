<template>
<div>
  <h1 class="title">ドン・ブラコッコ</h1>
  <div class="image">
    <img src="../assets/donburako.png" />
  </div>
  <button class="btn" v-on:click="QuestionPage()" >スタート</button>
  <button class="btn" v-on:click="ExplanationPage()">遊び方</button>
  <select  v-model="selectedTime">
    <option>1</option>
    <option>2</option>
    <option>3</option>
    <option>4</option>
    <option>5</option>
    <option>6</option>
    <option>7</option>
    <option>8</option>
    <option>9</option>
  </select>
  <router-link
    :to="{name: 'QuestionPage', params: {count: selectedTime}}"
  >スタート
  </router-link>
</div>
</template>

<style scoped>
.title{
  text-align: center;
}

.image {
  text-align: center;
}

.btn {
  display: block;
  background-color:#FFF;
  width: 30%;
  padding: 15px 3px;
  border-radius: 15px;
  margin: 0 auto;
  margin-top: 24px;
}

</style>

<script>
import axios from 'axios';

export default {
  data(){
    return {
      selectedTime: "1"
    }
  },
  methods: {
    QuestionPage(){
      this.$router.push('/question')
    },
    ExplanationPage(){
      this.$router.push('/explanation')
    },
    postTimes: function(){
      axios
        .put('https://still-stream-18883.herokuapp.com/' + this.selectedTime)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => console.log(error))
    }
  }
}
</script>