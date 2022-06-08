<template>
    <!-- <div class="question">
        <p>問題</p>
        <p>{{ sampleData.source }}</p>
    </div>
    <div id="choises"> -->
        <!-- AnswerPageに真偽値を渡す。正解の選択肢ならtrue -->
        <!-- <router-link
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
        </router-link> -->
    <!-- </div> -->
<!-- まずdivで囲う -->
<div class="question">
 <!-- ここにhtmlを書く -->
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