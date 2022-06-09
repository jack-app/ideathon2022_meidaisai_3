<template>
<div class="container">
    <div class="question">
        <p>問題</p>
        <p>{{ sampleData.source }}</p>
    </div>
    <div id="choices" class="choices"> -->
        <!-- AnswerPageに真偽値を渡す。正解の選択肢ならtrue -->
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: true }}" class="choice"
        >{{ sampleData.choices.correct }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false }}" class="choice"
        >{{ sampleData.choices.wrong[0] }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false }}" class="choice"
        >{{ sampleData.choices.wrong[1] }}
        </router-link>
        <router-link
            :to="{ name: 'AnswerPage', params:{ bool: false }}" class="choice"
        >{{ sampleData.choices.wrong[2] }}
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
    // DOM生成前に実行
    mounted() {
        axios
            .get('') // ここに使用するjsonを指定
            .then((response) => (this.sample = response.data)) // 取り込むデータの名前を記述
            .catch((error) => console.log(error));

        let target = document.getElementById('choices');
        // choicesの子要素をシャッフルする
        for(let i =target.children.length; i >= 0; i--){
            target.appendChild(target.children[Math.random()*i|0]);
        }
    }
}
</script>