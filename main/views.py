from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

import os
import json

from rest_framework.parsers import JSONParser

from .grauf_module import getPath

from .models import MapImage
from .serializers import MapImageSerializer

class MapImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MapImage.objects.all()
    serializer_class = MapImageSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'head']

    # def list(self, request):
    #     map = MapImage.objects.all()
    #     serializerMap = MapImageSerializer(map, many=True)
    #     data = serializerMap.data.copy()
    #
    #     _from = request.query_params.get('from')
    #     _to = request.query_params.get('to')
    #
    #
    #     images = MapImage.objects.filter(slug=f'{_from}_{_to}')
    #     serializerImage = MapImageSerializer(images, many=True)
    #     data.update({"images": [image['image'] for image in serializerImage.data]})
    #
    #     return Response(data)

    # def get_queryset(self):
    #     _from = self.request.query_params.get('from')
    #     _to = self.request.query_params.get('to')
    #
    #     # images = MapImage.objects.filter(slug=f'{_from}_{_to}')
    #     #
    #     # print(self.request)
    #     #
    #     # for i in images:
    #     #     print(i)
    #     #
    #     # print(images)
    #     #
    #     # if images.exists():
    #     #
    #     #     return images
    #     # else:
    #
    #     maps_ = getPath(_to, _from)
    #
    #
    #     map = {}
    #
    #     map['slug'] = f'{_from}_{_to}'
    #
    #     map['ground_flour'] = maps_[0]
    #     map['first_flour'] = maps_[1]
    #     map['second_flour'] = maps_[2]
    #
    #     # user_encode_data = json.dumps(map, indent=2).encode('utf-8')    # dict to byte
    #     # stream = io.BytesIO(user_encode_data)                           # byte to stream
    #     # data = JSONParser().parse(stream)                               # json parse
    #     #
    #     # ser = MapImageSerializer(data=data)
    #     #
    #     # if ser.is_valid():
    #     #     print('ok')
    #     #     print(ser.validated_data)
    #     return JsonResponse(status=404, data={'status':'false','message': {
    #         "ground_flour": map['ground_flour'],
    #         "first_flour": map['first_flour'],
    #         "second_flour": map['second_flour'],}})

def get_image_view(request):

    # получение пораметров
    _from = request.GET.get('from', '')
    _to = request.GET.get('to', '')

    # проверка на наличие существующего маршрута
    if os.path.exists(f'media/map_output/from_{_from}_to_{_to}_ground_floor.jpg') and os.path.exists(f'media/map_output/from_{_from}_to_{_to}_first_floor.jpg') and os.path.exists(f'media/map_output/from_{_from}_to_{_to}_second_floor.jpg') and os.path.exists(f'media/map_output/from_{_from}_to_{_to}_third_floor.jpg'):
        return JsonResponse(status=200, data={'status': 'true', 'message': {
            "ground_flour": f'media/map_output/from_{_from}_to_{_to}_ground_floor.jpg',
            "first_flour": f'media/map_output/from_{_from}_to_{_to}_first_floor.jpg',
            "second_flour": f'media/map_output/from_{_from}_to_{_to}_second_floor.jpg',
            "third_flor": f'media/map_output/from_{_from}_to_{_to}_third_floor.jpg'}})

    # генерирование маршрута
    maps_ = getPath(_from, _to)
    # except:
    #     return JsonResponse(status=404, data={'status': 'false', 'message': 'путь не может быть построен'})

    map = {}

    map['slug'] = f'{_from}_{_to}'

    map['ground_floor'] = maps_[0]
    map['first_floor'] = maps_[1]
    map['second_floor'] = maps_[2]
    map['third_floor'] = maps_[3]

    return JsonResponse(status=200, data={'status': 'true', 'message': {
        "ground_floor": map['ground_floor'],
        "first_floor": map['first_floor'],
        "second_floor": map['second_floor'],
        "third_floor": map['third_floor']
    }})
