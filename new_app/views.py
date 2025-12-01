from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import SaluProduct
from .serializers import SaluProductSerializer


# POST - Add product
@api_view(['POST'])
def add_salu_product(request):
    serializer = SaluProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Salu product added successfully",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET - Search
@api_view(['GET'])
def search_salu_products(request):
    query = request.GET.get('query', '')
    products = SaluProduct.objects.filter(name__icontains=query)
    serializer = SaluProductSerializer(products, many=True)
    return Response(serializer.data)


