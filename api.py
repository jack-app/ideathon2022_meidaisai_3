from google.cloud import translate

class API_tranlate:
    def translate_text(self,text="問題が発生しました",output_language="en-US",input_language="ja",project_id="symmetric-card-351306"):
        self.client = translate.TranslationServiceClient()
        self.location = "global"
        self.parent = f"projects/{project_id}/locations/{self.location}"
        self.response = self.client.translate_text(
            request={
                "parent": self.parent,
                "contents": [text],
                "mime_type": "text/plain",
                "source_language_code": input_language,
                "target_language_code": output_language,
            }
        )

        return self.response.translations

input_text = input()
sample = API_tranlate(input_text)
answer = sample.translate_text()
print(answer)