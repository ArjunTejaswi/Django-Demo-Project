from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class MyView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("got hit!!")

class TodoList(APIView):
    def get(self, request):
        (TodoSerializer(request.headers))
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({'statusCode':200 ,'success': True, 'data': serializer.data})

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            todo = self.get_object(pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        except:
            return Response("something went wrong")
        
    def post(self, request, pk, **kwargs):
        try:
            print("1", kwargs)
            partial = kwargs.pop('partial', True)
            print("2", partial)
            instance = self.get_object(pk)
            print("3", instance)
            serializer = TodoSerializer(instance, data=request.data, partial=partial)
            if serializer.is_valid():
                name = serializer.validated_data.get('name')
                print("4", name)
                if name:
                    instance.name = name
                    instance.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("something went wrong")

    def put(self, request, pk):
        try:
            print("i am here")
            todo = self.get_object(pk)
            print("aa", todo)
            serializer = TodoSerializer(todo, data=request.data)
            print("pp", serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response("something went wrong")


    def delete(self, request, pk):
        print("delete", pk)
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# view for registering users
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)