<template>
<div class="container">
    <div class="question">
        <p>問題</p>
        <p>{{ sample.translated }}</p>
    </div>
    <div id="choices" class="choices"> -->
        <!-- AnswerPageに真偽値を渡す。正解の選択肢ならtrue -->
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: true, origin: sample.source, translated: sample.translated }}" class="choice"
        >{{ sample.choices.correct }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false, origin: sample.source, translated: sample.translated }}" class="choice"
        >{{ sample.choices.wrong[0] }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false, origin: sample.source, translated: sample.translated }}" class="choice"
        >{{ sample.choices.wrong[1] }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false, origin: sample.source, translated: sample.translated }}" class="choice"
        >{{ sample.choices.wrong[2] }}
        </router-link>
    </div>
</div>

</template>

<style scoped>
/* .question {
    padding:20px 15px 200px;
    margin: 20px 150px 200px;
    color: rgb(88, 231, 176);
    background:rgb(88, 231, 176);
    border-radius: 25px
} */

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
import axios from 'axios';

export default {
    data() {
        return {
            sample: null
        }
    },
    // DOM生成前に実行
    mounted() {
        axios
            .get('https://still-stream-18883.herokuapp.com/') // ここに使用するjsonを指定
            .then((response) => (this.sample = response.data)) // 取り込むデータの名前を記述
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