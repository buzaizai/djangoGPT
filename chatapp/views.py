from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat(request):
    if request.method == 'POST':
        userMessage = request.POST.get('message')
        headers = {
            'Authorization': 'Bearer ' + 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJ3dWppYWt1bjEwQG91dGxvb2suY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXIteFNBbE9xcVpvbVA4VHhJYVVYNE0yRkltIn0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDAyYjUxMWEwYzI1MDkzN2U0ZTVkN2YiLCJhdWQiOlsiaHR0cHM6Ly9hcGkub3BlbmFpLmNvbS92MSIsImh0dHBzOi8vb3BlbmFpLm9wZW5haS5hdXRoMGFwcC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjg1NzcwOTcyLCJleHAiOjE2ODY5ODA1NzIsImF6cCI6IlRkSkljYmUxNldvVEh0Tjk1bnl5d2g1RTR5T282SXRHIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCBtb2RlbC5yZWFkIG1vZGVsLnJlcXVlc3Qgb3JnYW5pemF0aW9uLnJlYWQgb3JnYW5pemF0aW9uLndyaXRlIn0.umCafYjO0pDgFtp4BKI25pIsnnbqShcbtUW2vOnNaX95F03u8DLxsE9DN4d5eMIoB9MO8F5NkgMa4jA_TFa2hmHYitTc_W4xxk1CMYAb8kji4acuFDiybSYT0zfq3buAaGkN0BxZjUSo749yDZYqT8VL80jvtJUgVYBBB3AAeM-pEgz6RSmefEdrUW-v2WEybQgDzpBeveK8KmT4WA9oX_uGkgqG1TC02y-0N0ihL-x4hTI360PXnYqRI6fR66cfRvbJazVNa60LmXY8eGATtRZ37ig9_PeCCaghnmgB6hQ0MBG96hdqDG-77B9v5l6W3LF810R_vEIAZFVt1kgsqg'}  # 将 your_access_token 替换为你的 ChatGPTUnofficialProxyAPI 的 access token
        data = {
            'model': 'text-davinci-002',
            'prompt': userMessage,
            'temperature': 0.5,
            'max_tokens': 50
        }
        response = requests.post('https://ai.fakeopen.com/api/conversation', headers=headers, json=data)
        responseData = response.json()

        return JsonResponse(responseData, safe=False)
    else:
        return render(request, 'chat.html')
