from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer

User = get_user_model()  # Points to CustomUser


# APIView for retrieving, updating, and deleting user details (no generics)
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users

    def get(self, request, *args, **kwargs):
        """ Retrieve user details """
        try:
            user = User.objects.get(id=kwargs['pk'])
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        """ Update user details """
        try:
            user = User.objects.get(id=kwargs['pk'])
            if request.user != user:
                return Response({'error': 'You are not authorized to update this user.'},
                                status=status.HTTP_403_FORBIDDEN)

            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        """ Delete a user """
        try:
            user = User.objects.get(id=kwargs['pk'])
            if request.user != user:
                return Response({'error': 'You are not authorized to delete this user.'},
                                status=status.HTTP_403_FORBIDDEN)

            user.delete()
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class ManageFriendView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """ Add a friend by ID (authenticated users only) """
        friend_id = request.data.get('friend_id')

        try:
            friend = User.objects.get(id=friend_id)
            if friend == request.user:
                return Response({'error': 'You cannot add yourself as a friend'}, status=status.HTTP_400_BAD_REQUEST)

            request.user.friends.add(friend)
            return Response({'message': 'Friend added successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Friend not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        """ Remove a friend by ID (authenticated users only) """
        friend_id = request.data.get('friend_id')

        try:
            friend = User.objects.get(id=friend_id)
            if friend not in request.user.friends.all():
                return Response({'error': 'User is not your friend'}, status=status.HTTP_400_BAD_REQUEST)

            request.user.friends.remove(friend)
            return Response({'message': 'Friend removed successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Friend not found'}, status=status.HTTP_404_NOT_FOUND)

class UserListView(APIView):
    permission_classes = [AllowAny]  # [IsAdmin]

    def get(self, request, *args, **kwargs):
        """ Retrieve all registered users """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)