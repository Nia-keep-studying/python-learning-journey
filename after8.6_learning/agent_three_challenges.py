import ollama

# ============================================================
# 挑战 A：多轮对话 —— 让模型记住你刚才说过的话
# ============================================================
# 秘诀：把所有对话历史都存在 messages 列表里，每次都全发过去
print("=" * 50)
print("挑战 A：多轮对话")
print("=" * 50)

# 准备一个空的历史记录列表
history = [
    {"role": "user", "content": "我叫小明"}
]

# 第一轮：告诉它名字
r1 = ollama.chat(model="qwen2.5:3b", messages=history)
# 把模型回复也加进历史
history.append({"role": "assistant", "content": r1["message"]["content"]})

# 第二轮：再问它我叫什么 —— 它必须从历史里找答案
history.append({"role": "user", "content": "我叫什么？"})
r2 = ollama.chat(model="qwen2.5:3b", messages=history)

print(f"我问：「我叫什么？」\n模型答：{r2['message']['content']}\n")

# ============================================================
# 挑战 B：换角色 —— 用 system 提示词让模型变一个人
# ============================================================
print("=" * 50)
print("挑战 B：换角色 —— 鲁迅语气")
print("=" * 50)

r3 = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {"role": "system", "content": "你是鲁迅，用鲁迅的文风回答。语气要像《狂人日记》那样。"},
        {"role": "user", "content": "AI这个东西你怎么看？"}
    ]
)

print(f"鲁迅说：{r3['message']['content']}\n")

# ============================================================
# 挑战 C：批量提问 —— 用循环一次问三个问题
# ============================================================
print("=" * 50)
print("挑战 C：批量提问")
print("=" * 50)

questions = [
    "什么是AI Agent？",
    "Python适合做什么？",
    "学编程最难的是什么？"
]

for i, q in enumerate(questions, 1):
    r = ollama.chat(
        model="qwen2.5:3b",
        messages=[{"role": "user", "content": q}]
    )
    print(f"[问题{i}] {q}")
    print(f"[回答{i}] {r['message']['content']}\n")
