import os
class Constants:
    def __init__(self, isLocal=os.environ["DONBURAKKO_IS_LOCAL"]):
        if isLocal:
            self.prefix_source_dir = "."
            self.prefix_frontend_dir = "../frontend"
        if not(isLocal):
            self.prefix_source_dir = os.getcwd() + "/backend"
            self.prefix_frontend_dir = "../frontend"