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
    height: 300px;
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
    justify-content: space-around;
    margin-top: 64px;
}

.choice {
    width: 20%;
    background-color: rgb(92, 254, 165);
    text-align: center;
    height: 48px;
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
    data() {
        return {
            sample: null,
            query: 100000000000000
        }
    },
    // DOM生成前に実行
    mounted() {
        axios
            .get('https://obscure-temple-92668.herokuapp.com/api?b='+ this.query +'&count=2') // ここに使用するjsonを指定
            .then((response) => (this.sample = response.data)) // 取り込むデータの名前を記述
            .catch((error) => console.log(error));
        // this.query = this.query + this.sample.finish
    },
    // データの変更後に呼び出す
    updated() {
        let target = document.getElementById('choices');
        // choicesの子要素をシャッフルする
        for(let i =target.children.length; i >= 0; i--){
            target.appendChild(target.children[Math.random()*i|0]);
        }
        this.query = this.query + this.sample.finish
    }
}
</script>