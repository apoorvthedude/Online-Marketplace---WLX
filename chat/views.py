from django.shortcuts import render,get_object_or_404,redirect

from .forms import *
from item.models import *
from .models import *

# Create your views here.
def new_chat(request,item_pk):
    item = get_object_or_404(Item,pk=item_pk)

    if item.created_by == request.user:
        return redirect('dashboard:dashboard')
    
    conversations  = Chat.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            chat = Chat.objects.create(item=item)
            chat.members.add(request.user)
            chat.members.add(item.created_by)
            chat.save()

            conversation_message = form.save(commit=False)
            conversation_message.chat = chat
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail',pk=item_pk)
    
    else:
        form = ConversationMessageForm()

    return redirect(request,'chat/new.html',{
        'form':form,
    })