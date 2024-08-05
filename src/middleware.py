from src.models import User
from src.serializers import FullUserSerializer
from django.core.exceptions import PermissionDenied
from django.conf import settings

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        relative_url = request.path
        
        print(relative_url)

        
        if '/media/image/' not in relative_url and relative_url not in settings.IGNORE_URLS:
        
            auth_header = request.headers.get('Authorization')
            
            user = User.objects.filter(session=auth_header).first()
        
            if not user:
                raise PermissionDenied
            
            user_serializer = FullUserSerializer(user)
            
            request.session["user"] = user_serializer.data

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware