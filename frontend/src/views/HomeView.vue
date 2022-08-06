<template>
<div>
  <h1 class="title">ドン・ブラコッコ</h1>
  <div class="image">
    <img src="../assets/donburako.png" />
  </div>
  <div class="selection">
    <p>翻訳回数</p>
    <select  v-model="selectedTime">
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
    </select>
  </div>
  <button class="btn" v-on:click="QuestionPage()" >スタート</button>
  <button class="btn" v-on:click="ExplanationPage()">遊び方</button>
</div>
</template>

<style scoped>
.title{
  text-align: center;
}

.image {
  text-align: center;
}

.selection {
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
export default {
  data(){
    return {
      selectedTime: ""
    }
  },
  mounted() {
    // ローカルストレージから前回の選択回数を引き継ぐ
    // todo:homeに行ったらローカルストレージを削除
    this.selectedTime = localStorage.getItem('translationTime')
  },
  updated() {
    // selectboxの更新が起こったらローカルに保存
    localStorage.setItem('translationTime', this.selectedTime)
  },
  methods: {
    QuestionPage(){
      this.$router.push('/question')
    },
    ExplanationPage(){
      this.$router.push('/explanation')
    },
  }
}
</script>