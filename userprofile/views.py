from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.exceptions import AuthenticationFailed
from .models import Profile
from .serializers import ProfileSerializer
import jwt

class ProfileView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_user_from_token(self, request):
        print('Cookies',request.COOKIES)
        token = request.COOKIES.get("jwt")
        print('token',token)
        if not token:
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated")
        return payload["id"]

    def get(self, request):
        try:
            user_id = self.get_user_from_token(request)
            print('user id in get token',user_id)
            profile = Profile.objects.get(user_id=user_id)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        user_id = self.get_user_from_token(request)
        profile = Profile.objects.get(user_id=user_id)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user_id = self.get_user_from_token(request)
        profile = Profile.objects.get(user_id=user_id)
        profile.delete()
        return Response({"message": "Profile deleted"}, status=status.HTTP_204_NO_CONTENT)
