from pathlib import Path
import json


location = Path(__file__).parent/"studied_list.json"

def write_in():
    date = input("今天的日期是: ")
    subject = input("你学的是什么学科: ")
    detail = input("今天学了什么: ")
    feedback = input("有什么收获: ")
    study_dict = {"date":date,"subject":subject,"detail":detail,"feedback":feedback}
    records = load_records()
    records.append(study_dict)
    location.write_text(json.dumps(records,ensure_ascii=False),encoding="utf-8")

def read_record():
        records = load_records()
        if records:
            for record in records:
                for key,value in record.items():
                    print(f"{key} - {value} ")
                print("\n")
        else:
            print("还没有学习记录")

def search_record():
    active = False
    records = load_records()
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
    else:
        print("没有找到记录文件")

def load_records():
    if location.exists():
        records = json.loads(location.read_text(encoding="utf-8"))
    else:
        records = []
    return records

def clean_json():
    records = load_records()
    if records:
        records = []
        location.write_text(json.dumps(records,ensure_ascii=False),encoding="utf-8")
        print("已清空全部记录")
    else:
        print("没有记录，无需清空")

def delete_items():
    records = load_records()
    if records:
        date = input("请输入要删除哪天的记录： ")
        for record in records[:]:
            if record["date"] == date:
                records.remove(record)
                location.write_text(json.dumps(records,ensure_ascii=False),encoding="utf-8")
                print(f"已删除 {date} 的学习记录")
    else:
        print("记录为空")

def run():
    while True:
        print("\n请选择操作:")
        print("1.增加学习记录")
        print("2.读取学习记录")
        print("3.查询学习记录")
        print("4.清空学习记录")
        print("5.删除学习记录")
        print("6.退出")

        option = input("\n请选择操作: ")
        if option == "1":
            write_in()
        elif option == "2":
            read_record()
        elif option == "3":
            search_record()
        elif option == "4":
            clean_json()
        elif option == "5":
            delete_items() 
        elif option == "6":
            print("正在退出")
            break
        else:
            print("输入无效")
            continue

