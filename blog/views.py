from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

# Create your views here.
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context={
        }
        return render(request, 'blog_list.html', context)

