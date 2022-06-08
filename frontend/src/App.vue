<template>
<!-- 共通部分を書きたいときはこのapp.vueに記述 -->
  <div id="app">
    <nav>
      <!-- リンクの遷移についてはaタグにhref='/'みたいにいろんな書き方できる -->
      <router-link to="/">Home</router-link>
      <router-link to="/question">question</router-link>
      <router-link to="/answer">answer</router-link>
      <router-link to="/explanation">explanation</router-link>

    </nav>
    <!-- router-viewタグがviesファイルの各ページ要素を表示 -->
    <router-view/>
  </div>
</template>

<style>
body{
  background-color:#febab8;
}
</style>

<script>

</script>
