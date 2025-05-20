from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from twitter.models import TwitterAccount
from twitter.services import publish_tweet
# Create your views here.
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!, im Dui")

def test_tweet_view(request):
    if request.method == 'GET':
        
        
        print('get mettoooood')
        pass

    if request.method == 'POST':
        message = request.POST.get('message')
        
        # Opción 1: Usar credenciales fijas (para pruebas rápidas)
        # success = publish_tweet(
        #     "TU_API_KEY",
        #     "TU_API_SECRET",
        #     "TU_ACCESS_TOKEN",
        #     "TU_ACCESS_TOKEN_SECRET",
        #     message
        # )

        # Opción 2: Usar una cuenta guardada en la base de datos (recomendado)
        account = TwitterAccount.objects.first()  # O selecciona una cuenta específica
        success = publish_tweet(
            account.api_key,
            account.api_secret,
            account.access_token,
            account.access_token_secret,
            message
        )

        if success:
            messages.success(request, "¡Tweet publicado correctamente!")
        else:
            messages.error(request, "Error al publicar el tweet. Revisa las credenciales.")
        
        return redirect('test_tweet')  # Recarga la página
    
    # Obtener cuentas disponibles (si usas el modelo)
    accounts = TwitterAccount.objects.all()
    
    return render(request, 'twitter/test_tweet.html', {
        'accounts': accounts,
    })


class Account(View):
	pass
