from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ArrayDiagonale
from .serializers import ArrayDiagonaleSerializers
import matrixalg
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
import numbers

# Create your views here.
class ArrayDiagonaleView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='size', 
                description='Size of matrix', 
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                required=True
            ),
        ],
        request=None,
        responses={
            200: OpenApiResponse(
                response=ArrayDiagonaleSerializers,
                description='Succesfully retrieved'
            )
        },
        description='Returns matrix and its diagonal',
        methods=['GET']
    )


    def get(self, request):
        size = request.GET.get('size')
        if size.isdigit() == False:
            return Response('Size must be integer', status=400)
        a = matrixalg.main(size)
        result = ArrayDiagonale(a['массив'], a['диагональ'])

        serializer_for_request = ArrayDiagonaleSerializers(instance=result)

        return Response(serializer_for_request.data)