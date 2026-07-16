import ollama

print("正在加载模型，请稍候...")

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {"role": "user", "content": "用一句话解释什么是AI Agent"}
    ]
)

print("模型回复如下：")
print(response["message"]["content"])
