
from customauth_app.models import CustomUser
from customauth_app.serializers import CustomUserSerliazer, CustomUserQuerySerliazer
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

# Create your views here.

# only for user registration working
class CustomUserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerliazer



# if you CRUD operation you can try this class 

# class CustomUserViewSet(viewsets.ViewSet):
#     permission_classes = [AllowAny]
#     def list(self, request):
#         try:
#             queryset = CustomUser.objects.all()
#             serializer = CustomUserQuerySerliazer(queryset, many=True)
#             response_data = {
#                 "data": serializer.data,
#                 "message": "User List Response Success",
#                 "error": False,
#                 "status": status.HTTP_200_OK

#             }
#             return Response(response_data)
#         except Exception:
#             response_data = {
#                 "message": "Error Response",
#                 "error": True,
#                 "status": status.HTTP_400_BAD_REQUEST

#             }
#             return Response(response_data)


#     def create(self, request):
#         try:
#             serializer = CustomUserSerliazer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             response_data = {
#                 "data": serializer.data,
#                 "message": "User Registration Successfully",
#                 "error": False,
#                 "status": status.HTTP_201_CREATED

#             }
#             return Response(response_data)
#         except Exception:
#             response_data = {
#                 "message": "User Registration Error",
#                 "error": True,
#                 "status": status.HTTP_400_BAD_REQUEST

#             }
#             return Response(response_data)


#     def retrieve(self, request, pk=None):
#         try:
#             user = CustomUser.objects.get(id=pk)
#             serializer = CustomUserQuerySerliazer(user)
#             response_data = {
#                 "data": serializer.data,
#                 "message": "User Retrieve Data",
#                 "error": False,
#                 "status": status.HTTP_201_CREATED

#             }
#             return Response(response_data)
#         except Exception:
#             response_data = {
#                 "message": "User Retrieve Error",
#                 "error": False,
#                 "status": status.HTTP_400_BAD_REQUEST

#             }
#             return Response(response_data)


#     def update(self, request, pk=None):
#         try:
#             queryset = CustomUser.objects.get(id=pk)
#             serializer = CustomUserSerliazer(queryset, data=request.data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             response_data = {
#                 "data": serializer.data,
#                 "message": "User Update Successfully",
#                 "error": False,
#                 "status": status.HTTP_201_CREATED
#             }
#             return Response(response_data)
#         except Exception:
#             response_data = {
#                 "message": "User Update Error",
#                 "error": True,
#                 "status": status.HTTP_400_BAD_REQUEST
#             }
#             return Response(response_data)


#     def destroy(self, request, pk=None):
#         try:
#             user = CustomUser.objects.get(id=pk)
#             user.delete()
#             response_data = {
#                 "message": "User Delete Successfully",
#                 "error": False,
#                 "status": status.HTTP_202_ACCEPTED
#             }
#             return Response(response_data)
#         except Exception:
#             response_data = {
#                 "message": "User Delete Error",
#                 "error": True,
#                 "status": status.HTTP_400_BAD_REQUEST
#             }
#             return Response(response_data)