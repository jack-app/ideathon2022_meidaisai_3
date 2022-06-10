<template>
<!-- 共通部分を書きたいときはこのapp.vueに記述 -->
  <div>
    <div class="links">
      <router-link to="/" class="eachLink">ホーム</router-link>/
      <router-link to="/explanation" class="eachLink">遊び方</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
body{
  background-color:#febab8;
}

a {
  text-decoration: none;
}

.links {
  text-align: right;
  color: white;
}

.eachLink {
  color: white;
  padding: 20px;
}


</style>

<script>

</script>
