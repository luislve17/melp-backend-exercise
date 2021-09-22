from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Restaurant

@api_view(['GET'])
def get_stats(request):
    # latitude=x
    # longitude=y
    # radius=z
    # Get all locations distance from (x,y)
    # Check wich ones D is less than R
    # Return
    return Response({"msg":"test"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def apply_restaurant(request):
    if request.method == "GET": return get_restaurant(request)
    elif request.method == "POST": return create_restaurant(request)
    elif request.method == "PATCH": return update_restaurant(request)
    elif request.method == "DELETE": return delete_restaurant(request)

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

def update_restaurant(request):
    if request.data.get("id"):
        data = request.data
        expected_fields = [field.name for field in Restaurant._meta.fields]
        useful_data = {key:val for key, val in data.items() if key in expected_fields}
        body_data = useful_data.copy()
        del body_data["id"]

        obj_id = useful_data["id"]
        obj = Restaurant.objects.get(pk=obj_id)
        obj.__dict__.update(body_data)
        
        if obj is None:
            response_obj = {"error": f"Item with id:{obj_id} not found for update|Used parameters in request: {useful_data}"}
            response_status = status.HTTP_400_BAD_REQUEST
        else:
            response_obj = obj.__dict__
            del response_obj["_state"]
            response_status = status.HTTP_200_OK
    else:
        response_obj = {"error": "Missing data in body: 'id'"}
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_obj, status=response_status)

    
def delete_restaurant(request):
    obj_id = request.data.get("id")
    if obj_id:
        try:
            obj = Restaurant.objects.get(pk=obj_id)
            obj.delete()
            response_obj = {"msg": f"Item was deleted (id:{obj_id})"}
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_obj = {"error": f"{str(e)}|Used parameters in request: {dict(request.data)}"}
            response_status = status.HTTP_400_BAD_REQUEST
    else:
        response_obj = {"error": "Missing data in body: 'id'"}
        response_status = status.HTTP_400_BAD_REQUEST

    return Response(response_obj, status=response_status)