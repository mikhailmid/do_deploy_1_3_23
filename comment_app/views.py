from django.shortcuts import render
from .models import Comment
from .forms import CommentForm


# Create your views here.
def main_view(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentForm()
    context = {'comments': Comment.objects.all(), 'form': form}
    return render(request, 'comment_app/index.html', context=context)
