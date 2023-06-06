import json
import os

from django.shortcuts import render

# Create your views here.
# 引入必要的模块
import requests
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from djangoGPT.settings import API_URL, ACCESS_TOKEN
import openai

@csrf_exempt  # 禁用 CSRF 防护
# ChatGPT API 反向代理地址

def home(request):
    return render(request, 'home.html')


class ChatGPT:
    def __init__(self, user):
        self.user = user
        self.messages = [{"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"}]
        self.filename="./user_messages.json"

    def ask_gpt(self):
        # q = "用python实现：提示手动输入3个不同的3位数区间，输入结束后计算这3个区间的交集，并输出结果区间"
        rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        return rsp.get("choices")[0]["message"]["content"]


    def writeTojson(self):
        try:
            # 判断文件是否存在
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    # 创建文件
                    pass
            # 读取
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                msgs = json.loads(content) if len(content) > 0 else {}
            # 追加
            msgs.update({self.user : self.messages})
            # 写入
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(msgs, f)
        except Exception as e:
            print(f"错误代码：{e}")

# def get_completion(prompt):
#     query = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=[{"role": "user", "content": prompt }]
#     )
#     response = query.get('choices')[0]['message']['content']
#     return response

def get_completion(prompt):
    query = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt }]
    )
    response = query.get('choices')[0]['message']['content']
    return response

class ChatGPT:
    def __init__(self, user):
        self.user = user
        self.messages = [{"role": "system", "content": "一个有10年Python开发经验的资深算法工程师"}]
        self.filename="./user_messages.json"

    def ask_gpt(self):
        rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        return rsp.get("choices")[0]["message"]["content"]


    def writeTojson(self):
        try:
            # 判断文件是否存在
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    # 创建文件
                    pass
            # 读取
            with open(self.filename, 'r', encoding='utf-8') as f:
                content = f.read()
                msgs = json.loads(content) if len(content) > 0 else {}
            # 追加
            msgs.update({self.user : self.messages})
            # 写入
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(msgs, f)
        except Exception as e:
            print(f"错误代码：{e}")
from djangoGPT.settings import messages
def get_completion(prompt,use):
    global messages
    if use == 'true':
        messages.append({"role": "user", "content": prompt})
        rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = rsp.get("choices")[0]["message"]["content"]
        messages.append({"role": "assistant", "content": answer})
        if len(messages) >= 10 or prompt == '1':
            messages = []
        return answer
    else:
        query = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{"role": "user", "content": prompt }]
    )
    response = query.get('choices')[0]['message']['content']
    return response


openai.api_key = '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'
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        use = request.POST.get('useContext')
        response = get_completion(message, use)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid method'})


