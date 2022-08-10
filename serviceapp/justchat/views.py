# import json
#
# from django.shortcuts import render
# from django.utils.safestring import mark_safe
# import json
#
# # Create your views here.
#
# def chat(request):
#     return render(request, 'justchat/chat.html')
#
# def chatPage(request, room_name):
#     return render(request, 'justchat/room.html', {'room_name_json':mark_safe(json.dumps(room_name))})