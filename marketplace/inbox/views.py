from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from item.models import Item
from .models import Inbox
from .forms import InboxMessageForm, ReplyMessageForm


@login_required
def new(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:

        return redirect('dashboard:index')

    messages = Inbox.objects.filter(item=item).filter(members__in=[request.user.id])

    if messages:
        pass # return messages

    if request.method == 'POST':
        form  = InboxMessageForm(request.POST)

        if form.is_valid():
            inbox = Inbox.objects.create(item=item)
            inbox.members.add(request.user)
            inbox.members.add(item.created_by)
            inbox.save()

            inbox_message = form.save(commit=False)
            inbox_message.inbox = inbox
            inbox_message.created_by = request.user
            inbox_message.save()

            return redirect('item:detail', pk=item_pk)

    else:
        form = InboxMessageForm()
    
    return render(request, 'inbox/new.html', {
        'form': form,
        'item_pk': item_pk
    })

@login_required
def inbox(request):
    messages = Inbox.objects.filter(members__in=[request.user.id])

    return render(request, 'inbox/index.html', {
        'messages': messages
    })

@login_required
def detail(request,pk):
    convo = Inbox.objects.filter(members__in=[request.user.id]).get(pk=pk)
    item = convo.item

    if request.method == 'POST':
        form = ReplyMessageForm(request.POST)

        if form.is_valid():
            convo_message = form.save(commit=False)
            convo_message.inbox = convo
            convo_message.created_by = request.user
            convo_message.save()

            convo.save()

            return redirect('inbox:detail', pk=pk)
    else:
        form = ReplyMessageForm()

        return render(request, 'inbox/detail.html', {
            'convo': convo,
            'form': form
        })