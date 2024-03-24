class TransForm:
    def __init__(self,target:str) -> None:
        self.target = target
    def trnasformer(self):
        return self.target.upper()
    

tem = TransForm("hello i am very happy")

print(tem.trnasformer())
