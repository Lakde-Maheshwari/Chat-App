from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import ChatGroup

# Create your views here.
@login_required
def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name='Public Chat') 
    messages = chat_group.chat_messages.all().order_by('created')[:30] 

    return render(request, 'chat.html',
    {
        'chat_messages' : messages,
        'chat_group' : chat_group,
    })

def home_view(request):
    return render(request, 'blank.html')