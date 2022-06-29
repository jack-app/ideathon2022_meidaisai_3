<template>
<div class="container">
    <div class="question">
        <p class="title">問題</p>
        <p class="text">{{ sample.translated }}</p>
    </div>
    <div id="choices" class="choices">
        <!-- AnswerPageに真偽値を渡す。正解の選択肢ならtrue -->
        <div class="choice">
            <router-link
                :to="{ name: 'AnswerPage', params:{ bool: true, origin: sample.source, translated: sample.translated }}" class="choiceName"
            >{{ sample.choices.correct }}
            </router-link>
        </div>
        <div class="choice">
            <router-link
                :to="{ name: 'AnswerPage', params:{ bool: false, origin: sample.source, translated: sample.translated }}" class="choiceName"
            >{{ sample.choices.wrong[0] }}
            </router-link>
        </div>
        <div class="choice">
            <router-link
                :to="{ name: 'AnswerPage', params:{ bool: false, origin: sample.source, translated: sample.translated }}" class="choiceName"
            >{{ sample.choices.wrong[1] }}
            </router-link>
        </div>
        <div class="choice">
            <router-link
                :to="{ name: 'AnswerPage', params:{ bool: false, origin: sample.source, translated: sample.translated }}" class="choiceName"
            >{{ sample.choices.wrong[2] }}
            </router-link>
        </div>
    </div>
</div>

</template>

<style scoped>
.question {
    width: 80%;
    background-color: #C3E6F1;
    border-radius: 25px;
    margin: 0 auto;
    margin-top: 64px;
    margin-bottom: 96px;
    padding-bottom: 16px;
}

.title {
    padding-top: 30px;
    margin-left: 30px;
    font-weight: bold;
}

.text {
    margin-left: 20px;
    margin-right: 20px;
}

.choices {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin-top: 32px;
}

.choice {
    width: 40%;
    background-color: rgb(92, 254, 165);
    text-align: center;
    margin-bottom: 24px;
    line-height: 48px;
    border-radius: 16px;
}

.choiceName {
    color: black;
    display: block;
}
</style>

<script>
import axios from 'axios';

export default {
    name: 'QuestionPage',
    data() {
        return {
            sample: {
                source: "",
                translated: "",
                choices: {
                    correct: "",
                    wrong: ""
                },
                finish: "000000000000000"
            },
        }
    },
    // DOM生成前に実行
    mounted() {
        let selectedTime = this.$route.params.count
        axios
            .get('https://donburakko.herokuapp.com/api?b=' + this.sample.finish + '&count=' + selectedTime)
            .then((response) => {
                (this.sample = response.data),
                console.log(this.sample.finish),
                console.log(selectedTime)
            }) // 取り込むデータの名前を記述
            .catch((error) => console.log(error));
    },
    // データの変更後に呼び出す
    updated() {
        let target = document.getElementById('choices');
        // choicesの子要素をシャッフルする
        for(let i =target.children.length; i >= 0; i--){
            target.appendChild(target.children[Math.random()*i|0]);
        }
    }
}
</script>