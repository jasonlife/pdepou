# -*- coding: UTF-8 -*-

from __future__ import absolute_import, unicode_literals

from braces.views import AjaxResponseMixin

from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, View

from pdepou.contact.models import Contact
from pdepou.core.utils import send_email

from .models import Comment, Post


class PostListView(ListView):
    """
    Class Based View that returns the published post list
    """
    model = Post
    queryset = Post.objects.published()
    context_object_name = 'posts'
    template_name = 'blog/base_blog.html'


class PostView(AjaxResponseMixin, View):
    """
    Post Class Based View
    """

    def get_ajax(self, request, *args, **kwargs):
        """
        HTTP GET request that returns the post template
        """
        post = get_object_or_404(Post, pk=request.GET.get('post_id'))
        return render(request, 'blog/modals/_{}.html'.format(post.slug),
                      dictionary={'post': post})

    def post_ajax(self, request, *args, **kwargs):
        """
        HTTP POST request that saves a post comment
        """
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        contact = Contact.check_contact(name=name, email=email)
        comment = Comment.objects.create(text=text, post=post, contact=contact)
        send_email(contact, 'Comentario de {0} en el post {1}'
                   .format(name, post.name))
        return render(request, 'blog/partials/comment.html',
                      dictionary={'comment': comment})
