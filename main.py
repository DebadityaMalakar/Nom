#Uselsess Programming Language
RUN=True
class userArray():
    def __init__(self):
        self.userArray = [96]*16
        self.pos=0
    def getCurrentInfo(self):
        return self.pos,self.userArray[self.pos],chr(self.userArray[self.pos])
    def nextPos(self):
        if (self.pos +1 >= len(self.userArray)):
            self.pos = 0
            return EnvironmentError("Overflow")
        else:
            self.pos = self.pos + 1
    def previousPos(self):
        if(self.pos -1 <= 0):
            self.pos=0
            return EnvironmentError("Underflow")
        else:
            self.pos = self.pos -1
    def incrementValue(self):
        if(self.userArray[self.pos] +1>256):
            self.userArray[self.pos] = 0
        else:
            self.userArray[self.pos] = self.userArray[self.pos] +1 
    def decrementValue(self):
        if(self.userArray[self.pos]-1<0):
            self.userArray[self.pos] = 0
        else:
            self.userArray = self.userArray[self.pos] -1
    def returnValue(self):
        x=""
        for i in self.userArray:
            x += chr(i)
        return x


programExposeArray = userArray()
while RUN:
    print("((nom))")
    cmnd=input()
    for i in cmnd.split():
        if i=="exit":
            RUN=False
            break
        if i=="nom":
            programExposeArray.incrementValue()
        if i=="chop":
            programExposeArray.decrementValue()
        if i=="uwu":
            programExposeArray.nextPos()
        if i=="sai":
            programExposeArray.previousPos()
        if i=="info":
            print(programExposeArray.getCurrentInfo())
        if i=="return":
            print(programExposeArray.returnValue())