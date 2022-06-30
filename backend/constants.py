import os
class Constants:
    def __init__(self, isLocal=bool(os.environ["DONBURAKKO_IS_LOCAL"])):
        print(isLocal=="True")
        if isLocal=="True":
            self.prefix_source_dir = "."
            self.prefix_frontend_dir = "../frontend"
        else:
            self.prefix_source_dir = os.getcwd() + "/backend"
            self.prefix_frontend_dir = "../frontend"