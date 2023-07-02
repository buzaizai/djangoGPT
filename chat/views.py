import json
import os

from django.shortcuts import render

# Create your views here.
# 引入必要的模块
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import openai

@csrf_exempt  # 禁用 CSRF 防护

def home(request):
    return render(request, 'home.html')

import requests
from bs4 import BeautifulSoup

# 用于访问搜索引擎的函数
def search_engine(query):
    # 将查询字符串编码成 URL
    url = "https://www.google.com/search?q={}".format(requests.utils.quote(query))
    # 向搜索引擎发出 GET 请求
    response = requests.get(url)
    # 从响应中提取 HTML 页面内容
    html_content = response.text
    # 使用 BeautifulSoup 解析 HTML 页面
    soup = BeautifulSoup(html_content, 'html.parser')
    # 找到页面中的所有搜索结果
    search_results = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")
    # 返回前五个搜索结果文本
    results_text = [result.get_text() for result in search_results[:5]]
    return results_text

from djangoGPT.settings import messages
def get_completion(prompt,use,internet):
    global messages
    prompt = '问题：' + prompt + '\n'
    if internet == 'true':
        search_results = search_engine(prompt)
        prompt += "\n请从下面这些在google上检索到的结果中筛选出正确答案，结果只输出把全部的结果总结后的内容\n"
        for i, result in enumerate(search_results):
            prompt += f"\n{result}"
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


openai.api_key = 'YOUR_API_KEY'
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        use = request.POST.get('useContext')
        internet = request.POST.get('internet')
        response = get_completion(message, use,internet=internet)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid method'})


