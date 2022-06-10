<template>
<div>
  <h1 class="title">ドン・ブラコッコ</h1>
  <div class="image">
    <img src="../assets/donburako.png" />
  </div>
  <button class="btn1" v-on:click="QuestionPage()" >スタート</button>
  <button class="btn2" v-on:click="ExplanationPage()">遊び方</button>
  <!-- <select  v-model="selectedTime">
    <option>1</option>
    <option>2</option>
    <option>3</option>
  </select> -->
</div>
</template>

<style scoped>
.title{
  text-align: center;
}

.image {
  text-align: center;
}

.btn1{
  display: block;
  background-color:#FFF;
  width: 30%;
  padding: 15px 30px;
  border-radius: 15px;
  margin: 2% 35%;
}

.btn2{
  display: block;
  background-color:#FFF;
  width: 30%;
  padding: 15px 30px;
  border-radius: 15px;
  margin: 2% 35%;
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