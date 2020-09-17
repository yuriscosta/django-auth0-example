from django.conf import settings
from django.contrib.auth import logout as log_out
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View
from urllib.parse import urlencode

from .models import Post


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect('/codes')

    return render(request, 'index.html')


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = f"https://{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/v2/logout" \
                 f"?client_id={settings.SOCIAL_AUTH_AUTH0_KEY}&{return_to}"

    return HttpResponseRedirect(logout_url)


class PostListView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PostListView, self).dispatch(*args, **kwargs)

    def get(self, request):
        posts = Post.objects.all()
        context = {'posts': posts}

        return render(request, 'home.html', context)
