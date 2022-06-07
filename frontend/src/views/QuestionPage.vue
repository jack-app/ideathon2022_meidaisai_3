<template>
<!-- まずdivで囲う -->
<div class="question">
 <!-- ここにhtmlを書く -->
  <p></p>

 <div>
   <button class="answera">A</button>
 </div>

 <div>
     <button class="answerb">B</button>
 </div>

 <div>
     <button class="answerc">C</button>
 </div>

 <div>
     <button class="answerd">D</button>
 </div>
</div>



</template>

<style scoped>
/* scopedを指定しないと他のページにもcssが適用 */
/* ここにcssを書く */
.question{
    padding:20px 15px 200px;
    margin: 20px 150px 200px;
    color: rgb(88, 231, 176);
    background:rgb(88, 231, 176);
    border-radius: 25px
}

.answera{
    position: absolute;
    top: 350px;
    width: 150px;
    padding:20px 270px 40px;
    margin: 20px 0% 100px;
    color: rgb(92, 254, 165);
    background: rgb(92, 254, 165);
    border-radius: 15px
    

}

.answerb{
    position: absolute;
    top: 350px;
    width: 150px;
    padding:20px 270px 40px;
    margin: 20px 41% 100px;
    color: rgb(92, 254, 165);
    background: rgb(92, 254, 165);
    border-radius: 15px;
}

.answerc{
    position: absolute;
    top: 500px;
    width: 150px;
    padding:20px 270px 40px;
    margin: 20px 0% 100px;
    color: rgb(92, 254, 165);
    background: rgb(92, 254, 165);
    border-radius: 15px
}

.answerd{
    position: absolute;
    top: 500px;
    width: 150px;
    padding:20px 270px 40px;
    margin: 20px 41% 100px;
    color: rgb(92, 254, 165);
    background: rgb(92, 254, 165);
    border-radius: 15px
}
</style>

<script>
// ここにjavascript(vue.js)を書く

</script>