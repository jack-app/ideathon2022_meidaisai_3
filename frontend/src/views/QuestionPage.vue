<template>
<div class="container">
    <div class="question">
        <p>問題</p>
        <p>{{ sampleData.source }}</p>
    </div>
    <div id="choises">
        <!-- AnswerPageに真偽値を渡す。正解の選択肢ならtrue -->
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: true }}"
        >{{ sampleData.choices.correct }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false }}"
        >{{ sampleData.choices.wrong[0] }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false }}"
        >{{ sampleData.choices.wrong[1] }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false }}"
        >{{ sampleData.choices.wrong[2] }}
        </router-link>
    </div>
</div>
</template>

<style scoped>
/* scopedを指定しないと他のページにもcssが適用 */
/* ここにcssを書く */

</style>

<script>
export default {
    data() {
        return {
            sampleData: {
                source: "昔々あるところに………",
                choices: {
                    correct: "桃太郎",
                    wrong: ["一寸法師", "三年寝太郎", "カチカチ山"]
                },
                finish: 10001
            }
        }
    },
    mounted() {
        let target = document.getElementById('choises');
        // choisesの子要素をシャッフルする
        for(let i =target.children.length; i >= 0; i--){
            target.appendChild(target.children[Math.random()*i|0]);
        }
    }
}
</script>