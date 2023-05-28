import json

# 读取源文件中的内容
with open("prompts-zh.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 遍历所有内容，转换格式
new_data = []
for content in data:
    new_content = {
        "cmd": content["act"].replace(" ", ""),
        "act": content["act"],
        "prompt": content["prompt"],
        "tags": ["chatgpt-prompts"],
        "enable": True
    }
    new_data.append(new_content)

# 将转换后的内容保存到新文件中
with open("prompts-zh(带cmd).json", "w", encoding="utf-8") as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)
