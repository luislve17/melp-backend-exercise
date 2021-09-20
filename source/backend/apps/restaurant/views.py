from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Restaurant

@api_view(['GET', 'POST', ])
def apply_restaurant(request):
    if request.method == "GET": return get_restaurant(request)
    elif request.method == "POST": return create_restaurant(request)

def get_restaurant(request):
    restaurant_id = request.query_params.get('id')

    if restaurant_id:
        try:
            obj = Restaurant.objects.get(pk=restaurant_id)
            response_obj = obj.__dict__
            del response_obj["_state"]
            response_status = status.HTTP_200_OK
        except Restaurant.DoesNotExist as e:
            response_obj = {"error": f"{str(e)}|Used parameters in request: {dict(request.query_params)}"}
            response_status = status.HTTP_404_NOT_FOUND
    else:
        response_obj = {"error": "No expected parameters in request"}
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_obj, status=response_status)

def create_restaurant(request):
    data = request.data
    expected_fields = [field.name for field in Restaurant._meta.fields]
    useful_data = {key:val for key, val in data.items() if key in expected_fields}
    print(useful_data)
    
    try:
        new_obj = Restaurant(**useful_data)
        new_obj.save()
        response_obj = new_obj.__dict__
        del response_obj["_state"]
        response_status = status.HTTP_200_OK
    except Exception as e:
        response_obj = {"error": f"{str(e)}|Used parameters in request: {dict(request.query_params)}"}
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_obj, status=response_status)
