from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from duser.models import Duser
from .forms import PostForm
from .models import Post
from tag.models import Tag


def post_upload(request):
    if not request.session.get("user"):
        return redirect("/user/login")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = request.session.get("user")
            duser = Duser.objects.get(pk=user)

            post = Post()
            post.title = form.cleaned_data["title"]
            post.imagesrc = form.cleaned_data["imagesrc"]
            post.contents = form.cleaned_data["contents"]
            post.writer = duser
            post.save()

            tags = form.cleaned_data["tags"].split(",")
            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                post.tags.add(_tag)

            return redirect("/post/list/")

    else:
        form = PostForm()

    return render(request, "post_upload.html", {"form": form})


def post_list(request):
    all_posts = Post.objects.all().order_by("-registered_date")
    page = int(request.GET.get("p", 1))
    paginator = Paginator(all_posts, 4)

    posts = paginator.get_page(page)

    return render(request, "post_list.html", {"posts": posts})


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("게시글을 찾을 수 없습니다.")

    return render(request, "post_detail.html", {"post": post})
