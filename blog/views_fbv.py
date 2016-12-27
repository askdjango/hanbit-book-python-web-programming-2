from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from blog.models import Post


def post_list(request):
    qs = Post.objects.all()
    paginate_by = 4
    paginator = Paginator(qs, paginate_by)

    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {
        'post_list': page_obj.object_list,
        'page_obj': page_obj,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })

