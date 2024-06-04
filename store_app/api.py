from store_app.models import (
    Item,
    ImagesItem,
    Color,
    Packaging,
    Users,
    ItemPack,
    ItemPackColor,
    Order,
    OrderItem,
)
from rest_framework import viewsets, permissions
from .serializers import (
    ItemSerializer,
    ImagesItemSerializer,
    UserSerializer,
    ColorSerializer,
    PackagingSerializer,
    OrderSerializer,
    ItemPackSerializer,
    ItemPackColorSerializer,
    OrderItemSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from os import path

# Create Viewsets
# For Creating CRUD for the serializers



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemSerializer


class ImagesItemViewSet(viewsets.ModelViewSet):
    queryset = ImagesItem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ImagesItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("request",request.data)
        serializer.is_valid(raise_exception=False)
        img = request.data["img_url"]
        print(img)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        print("serializer data:",serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        super(ItemViewSet, self).retrieve(request, args, kwargs)
        # print("My Get request")
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        # print("Data:",data)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

class ItemPackViewSet(viewsets.ModelViewSet):
    queryset = ItemPack.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemPackSerializer


class ItemPackColorViewSet(viewsets.ModelViewSet):
    queryset = ItemPackColor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemPackColorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
    # Post Request
    def create(self, request, *args, **kwargs):
        super(UserViewSet, self).create(request, args, kwargs)
        print("My Post request")
        print(request.data)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)
    # Get Request
    def retrieve(self, request, *args, **kwargs):
        super(UserViewSet, self).retrieve(request, args, kwargs)
        print("My Get request")
        instance = self.get_object()
        
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)
# Update Request
    def patch(self, request, *args, **kwargs):
        super(UserViewSet, self).patch(request, args, kwargs)
        print("My Update request")
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)
# Delete Request
    def delete(self, request, *args, **kwargs):
        super(UserViewSet, self).delete(request, args, kwargs)
        print("My Delete request")
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)
    
    def get_queryset(request):

        print("GET request")
        # blov = bucket.get_blob("Butterfly Gola Gold.jpeg")
        # blov.make_public()
        # print(blov.public_url)
        queryset = super().get_queryset()
        name_query = request.query_params.get("name")
        # print(name_query)
        if name_query is not None:
            queryset = queryset.filter(name__icontains=name_query)
        return queryset




class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ColorSerializer


class PackagingViewSet(viewsets.ModelViewSet):
    queryset = Packaging.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PackagingSerializer


class OrderViewSet(viewsets.ModelViewSet):
    
    queryset= Order.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderItemSerializer


