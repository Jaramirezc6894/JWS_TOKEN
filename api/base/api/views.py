from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
				# ,com
				# ,n_user
				# ,s_id

		token = super().get_token(user)
		# token = super().get_token(com)
		# token = super().get_token(n_user)
		# token = super().get_token(s_id)

		# Agregar valores personalizados
		token['username'] = user.username
		# token['company'] = com.company
		# token['network_user'] = n_user.network_user
		# token['sessionid'] = s_id.sessionid
		# ...

		return token

class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
	routes = [
		'/api/token',
		'/api/token/refresh',
		
		]


	return Response(routes)