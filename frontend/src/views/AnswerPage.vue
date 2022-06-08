<template>
<div class="container">
    <p v-if="$route.params.bool">正解！</p>
    <p v-else>不正解...</p>
</div>
</template>

<style scoped>
/* scopedを指定しないと他のページにもcssが適用 */
/* ここにcssを書く */

</style>

<script>
export default {
    name: 'AnswerPage'
}
</script>