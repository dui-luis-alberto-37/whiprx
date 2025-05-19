from wagtail import hooks
from django.http import JsonResponse
from django.urls import path
from django.shortcuts import render, redirect
from .models import TwitterAccount
from .services import publish_tweet

@hooks.register('register_admin_urls')
def register_publish_url():
    return [
        path('publish-tweet/', publish_tweet_view, name='publish_tweet'),
    ]

def publish_tweet_view(request):
    if request.method == 'POST':
        account_id = request.POST.get('account')
        message = request.POST.get('message')
        account = TwitterAccount.objects.get(id=account_id)
        success = publish_tweet(
            account.api_key,
            account.api_secret,
            account.access_token,
            account.access_token_secret,
            message
        )
        return JsonResponse({'success': success})
    accounts = TwitterAccount.objects.all()
    return render(request, 'twitter_publisher/publish.html', {'accounts': accounts})

@hooks.register('register_admin_menu_item')
def register_publish_menu_item():
    return {
        'name': 'Publicar en Twitter',
        'url': '/admin/publish-tweet/',
        'icon_name': 'megaphone',
    }
