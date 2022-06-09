from django.http import JsonResponse

def getRoustes(request) :
	routes = [
		'/api/token',
		'/api/token/refresh',
		
		]


	return JsonResponse(routes, safe = False)