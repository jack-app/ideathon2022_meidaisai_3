<template>
    <!-- <p v-if="$route.params.bool">正解！</p>
    <p v-else>不正解...</p> -->

<!-- まずdivで囲う -->
<div>
<!-- ここにhtmlを書く -->
<h1>こたえぺーじ</h1>
 <div>
    <button class="nextquestion">次の問題へ</button>
 </div>
 <div class="monndaikotae">
  <p>元の問題文</p>
 </div>
</div>

</template>



<style scoped>
/* scopedを指定しないと他のページにもcssが適用 */
/* ここにcssを書く */
.nextquestion{
   position: relative;
   top: 500px;
   left: 90%;
   width: 8%;
   background-color: rgb(83, 254, 177);
   border-color: rgb(83, 254, 177);
   border-radius: 10%;
   padding: 10px;
}

.monndaikotae{
   padding:25px 15px 200px;
   margin: 150px 150px 200px;
   color: rgb(115, 227, 224);
   background:rgb(115, 227, 224);
   border-radius: 25px;
}
</style>

<script>
export default {
    name: 'AnswerPage'
}
</script>