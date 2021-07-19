
from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from .models import board
from django.http import HttpResponse , HttpResponseNotAllowed
from .forms import sendCommentForm 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def Board(request):
    Comment = board.objects.order_by('-created_at')
    return render(request , 'comment/commentsboard.html' , {
                    'comment':Comment
    })
@login_required( redirect_field_name =None, login_url='/')
def Comment(request):
    if request.method == 'POST':
        form = sendCommentForm(request.POST)

        if form.is_valid():
            board.objects.create(
                comment = form.cleaned_data['comment'],
                username = request.user.username
            )
            return redirect('comment:comment')

    else:
        form = sendCommentForm()
        

    return render(request, 'comment/comment.html', {"form":form})

