class student:
    def __init__(self,name,age,number,**score):
        self.name = name
        self.number = number
        self.score = score
    
student1 = student("孙家祥",24,421,语文="32",数学=89,英语=73)
print(student1.score["数学"])
for subject,scores in student1.score.items():
    print(f"{subject}成绩为：{scores}")