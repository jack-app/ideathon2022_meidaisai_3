import json
import random


class Question:
    def __init__(self, binary_str, path):
        self.binary_str = "0b" + binary_str if not("0b" in binary_str) else binary_str
        self._source_path = path
        
        _q_id_list = self.question_id_list()
        
        self.question, self.id, self.wrongs = self.random_q_choice(_q_id_list)
        
        self.binary_str = self.update_binary()
        
        
    def question_id_list(self):
        """
        問題を解いたかどうかの２進数を入力して，まだ解いていない問題番号のリストを返す
        
        Args:
            binary str : 問題を解いたかどうかの２進数
            
        Returns:
            list[int] : まだ解いていない問題番号のリスト
        """
        
        _binary = int(self.binary_str, 0)
        res = []
        for i in range(len(self.binary_str) - 2): # -2はプレフィックス（0b)の分
            # and演算をして，一の位の数を取り出す．
            if(not(_binary & 0b1)):
                res.append(i)
            # >> は右シフト演算子．
            # 数字を指定した桁だけ右にずらして，最下位より先に押し出されたビットは消える
            _binary = _binary >> 1
        return res



    def random_q_choice(self, q_list):
        """
        問題idのリストから問題をランダムに選んで返す
        
        Args:
            q_list list[int]: 問題のid
        
        Returns:
            問題の辞書，問題のid, 間違いのタイトルズ
            
        """
        if q_list == []:
            return None
        
        def load_question(id: int, wrong_ids: list):
            with open(self._source_path, "r",encoding="utf-8") as f:
                question_json = json.loads(f.read())
            q = question_json[id]
            wrongs = [question_json[_]["title"] for _ in wrong_ids]
            return q, wrongs
        
        id = random.choice(q_list)
        wrong_ids = []
        for i in q_list:
            if i != id:
                wrong_ids.append(i)
        q, wrongs = load_question(id, wrong_ids)
        return q, id, wrongs


    def update_binary(self):
        """
        ２進数を更新する関数
        
        Args:
            binary_str  str: 元の２進数
            id          int: 使ったid
        
        Returns:
            新しい２進数の文字列
        """
        length = len(self.binary_str) - 2
        binary = int(self.binary_str, 0)
        _id_bin = 1 << self.id
        res = binary | _id_bin
        return bin(res).replace("0b", "").zfill(length)