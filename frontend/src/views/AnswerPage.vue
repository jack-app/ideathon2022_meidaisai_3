<template>
<div class="container">
    <div class="judge">
        <p v-if="$route.params.bool" class="correct">正解！</p>
        <p v-else class="wrong">不正解...</p>
    </div>
    <div class="answer">
        <p class="title">問題文</p>
        <p class="text">{{ $route.params.translated }}</p>
        <p class="title">原文</p>
        <p class="text">{{ $route.params.origin }}</p>
    </div>
    <div class="btnparent">
        <button class="nextbtn" v-on:click="QuestionPage()">次の問題へ</button>
    </div>
</div>

</template>



<style scoped>
.judge {
    text-align: center;
}

.correct {
    color: rgb(255, 0, 0);
    font-size: 40px;
}

.wrong {
    color: blue;
    font-size: 40px;
}

.answer {
    margin: 0 auto;
    width: 80%;
    background-color: #C3E6F1;
    border-radius: 25px;
    padding-bottom: 32px;
}

.title {
    padding-top: 32px;
    margin-left: 5%;
    font-weight: bold;
}

.text {
    margin: 0 auto;
    width: 90%;
}

.btnparent {
    float: right;
    padding-right: 5%;
}

.nextbtn{
   margin-top: 32px;
   text-align: center;
   width: 128px;
   background-color: rgb(83, 254, 177);
   border-color: rgb(83, 254, 177);
   border-radius: 10%;
   padding: 10px;
}

</style>

<script>
export default {
    name: 'AnswerPage',
    methods: {
    QuestionPage(){
      this.$router.push('/question')
    },
    }
}
</script>