from rest_framework import generics
from .models import Location, Department, Category, Subcategory, SKU
from .serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubcategorySerializer, SKUSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class LocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class DepartmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class SubcategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer



@api_view(['POST'])
def search_sku_by_metadata(request):
    
    """
    Search for products based on meta-data.
    Example payload:
    
    {
        "location": "Perimeter",
        "department": "Bakery",
        "category": "Bakery Bread",
        "subcategory": "Bagels"
    }
    
    """

    location = request.data.get('location',None)
    department = request.data.get('department',None)
    category = request.data.get('category',None)
    subcategory = request.data.get('subcategory',None)

    if not all([location, department, category, subcategory]):
        return Response({"error": "All fields (location, department, category, subcategory) are required."}, status=status.HTTP_400_BAD_REQUEST)

    products = SKU.objects.filter(
                location__name=location,
                department__name=department,
                category__name=category,
                subcategory__name=subcategory
    )
    serializer = SKUSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
