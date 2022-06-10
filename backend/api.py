from google.cloud import translate
import random

class API_translate:
    # クラスのインスタンスを作成
    def __init__(self, text="問題が発生しました"):
        self.text = [str(text)]
        self.project_id = "ideatranslate-352309"
        
    def many_translate(self, _from, _to):
        res = self.client.translate_text(
        request={
             "parent": self.parent,
             "contents": self.text,
             "mime_type": "text/plain",
             "source_language_code": _from,
             "target_language_code": _to,
            }
        )  #日本語を任意の言語に変換
        self.text = [res.translations[0].translated_text]


    def translate_text(self,count=0):
        self.count = 1  #何回変換したかを数えるカウンターを定義
        self.output_code = []   #変更する言語羅列のための型を定義
        self.client = translate.TranslationServiceClient()  
        self.location = "global"
        self.parent = f"projects/{self.project_id}/locations/{self.location}"
        self.path = "language_code.txt" #言語コード一覧のpathを取得
        # self.text = [text]  #翻訳のテキストを複製
        with open(self.path) as f:  #全言語コードのリスト化
            self.code = f.read()
            self.code = self.code.split("\n")
        while (self.count <= count):    #変換する言語コードをランダムに回数分取得
            self.output_code.append(random.choice(self.code))
            self.count += 1
        self.output_code.append("finish")
        print(self.output_code)
        _from = "ja"
        for index, language_code in enumerate(self.output_code): #グーグル翻訳APIをたたく
            if language_code=="finish":
                self.many_translate(_from, "ja")
                break
            # 同じ言語同士の翻訳はできないエラー対策
            if _from==language_code:
                print(f"{index}: {_from} to {language_code}は実行されません")
                continue
            print(f"{index}: {_from} to {language_code}")
            self.many_translate(_from, language_code)
            _from = language_code

        return self.text
    
    
if __name__=="__main__":
    with open("./source.txt", "r", encoding="utf-8") as f:
        text = f.read()
        print(API_translate(text).translate_text(count=20))