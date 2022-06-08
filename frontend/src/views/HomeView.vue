<template>
<!-- まずdivで囲う -->
<div>
<!-- ここにhtmlを書く -->
<!-- 写真はassetsフォルダに入れる -->
  <h1 class="title">ドン・ブラコッコ</h1>
  <button class="btn1" v-on:click="QuestionPage">スタート</button>
  <button class="btn2" v-on:click="ExplanationPage">
    <router-link to="/explanation"></router-link>
    遊び方
  </button>
</div>
</template>

<style scoped>
/* scopedを指定しないと他のページにもcssが適用 */
/* ここにcssを書く */

.title{
  margin: 0 39%;
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
// ここにjavascript(vue.js)を書く
export default {

  methods: {
    QuestionPage(){
      this.$router.push('/question')
    }
  }
}
</script>
