<template>
<!-- まずdivで囲う -->
<div>
<!-- ここにhtmlを書く -->
<!-- 写真はassetsフォルダに入れる -->
  <img alt="Vue logo" src="../assets/logo.png">
  <h1>{{ piyopiyo }}</h1>
</div>
</template>

<style scoped>
/* scopedを指定しないと他のページにもcssが適用 */
/* ここにcssを書く */
</style>

<script>
// ここにjavascript(vue.js)を書く
export default {
  data(){
    return{
      hogehoge:[],
      hugahuga:[],
      piyopiyo:'aaaaaaaaa'
    }
  }
}
</script>
