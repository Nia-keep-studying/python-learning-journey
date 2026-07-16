from pathlib import Path
import json

class StudyMemorize:
    def __init__(self):
        self.location = Path(__file__).parent/"studied_list.json"

    def write_in(self):
        date = input("今天的日期是: ")
        subject = input("你学的是什么学科: ")
        detail = input("今天学了什么: ")
        feedback = input("有什么收获: ")
        study_dict = {"date":date,"subject":subject,"detail":detail,"feedback":feedback}
        records = self.load_records()
        records.append(study_dict)
        self.location.write_text(json.dumps(records,ensure_ascii=False),encoding="utf-8")

    def read_record(self):
            records = self.load_records()
            if records:
                for record in records:
                    for key,value in record.items():
                        print(f"{key} - {value} ")
                    print("\n")

    def search_record(self):
        active = False
        records = self.load_records()
        if records:
            search_date = input("想查找哪天的学习记录: ")
            for record in records:
                if record["date"] == search_date:
                    active = True
                    for key,value in record.items():
                        print(f"{key} - {value}")
                    break
            if active != True:
                print(f"没有找到{search_date}日期的记录")

    def load_records(self):
        if self.location.exists():
            records = json.loads(self.location.read_text(encoding="utf-8"))
        else:
            print("还没有学习记录")
            records = []
        return records
    
    def run(self):
        while True:
            print("\n请选择操作:")
            print("1.增加学习记录")
            print("2.读取学习记录")
            print("3.查询学习记录")
            print("4.退出")

            option = input("\n请选择操作: ")
            if option == "1":
                self.write_in()
            elif option == "2":
                self.read_record()
            elif option == "3":
                self.search_record()
            elif option == "4":
                print("正在退出程序")
                break
            else:
                print("输入无效")
                continue