from store_app.models import (
    Item,
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
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import pathlib
from os import path

# Create Viewsets
# For Creating CRUD for the serializers



# Fetch the service account key JSON file contents
# cred = credentials.Certificate(path.join(pathlib.Path().resolve(),'store_app','config','serviceAccountKey.json'))

# # Initialize the app with a service account, granting admin privileges
# app = firebase_admin.initialize_app(cred, {
#     'storageBucket': 'thread-butterfly.appspot.com'
# })

# bucket = storage.bucket()



class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ItemSerializer

    def retrieve(self, request, *args, **kwargs):
        super(ItemViewSet, self).retrieve(request, args, kwargs)
        print("My Get request")
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        print("Data:",data)
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


def call_my_function():
    print("Here")
    pass

class PostViewSet(viewsets.ModelViewSet):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  serializer_class = ItemSerializer
  queryset = Item.objects.all() 
  
  def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #call your function Eg.
        call_my_function()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)