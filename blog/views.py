from django.shortcuts import render
from rest_framework import status, viewsets, serializers, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer,TitleSerializer

class ListBlog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    def get_queryset(self):
        queryset = Blog.objects.all()
        return queryset

class OnlyBlog(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    def get(self,request,pk):
        try:
            try:
               blog = Blog.objects.get(title=pk)
            except:
                error = "there is not an id"
                return Response(error,status=status.HTTP_404_NOT_FOUND) 
            res = {
                'id':blog.id,
                'created_at':blog.created_at,
                'updated_at':blog.updated_at,
                'title':blog.title,
                'contents':blog.contents
            }
            return Response(res)
        except:
            return Response("i don't know server error",status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class ListTitle(generics.ListCreateAPIView):
#     queryset = Blog.objects.filter('title')
#     print("--------------")
#     print(queryset)
#     print("--------------")
#     serializer_class = TitleSerializer
#     def get_queryset(self):
#         queryset = Blog.objects.all()
#         print("+++++++++++++")
#         print(queryset)
#         print("+++++++++++++")
#         return queryset
# #初期ページでこっち
class ListTitle(APIView):
    def get(self,request):
        blog = Blog.objects.order_by('-created_at')
        res = [
            {'id':b.id,'updated_at':b.updated_at,'title':b.title}
        
        for b in blog
        ]
        return Response(res)

class ListTest(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        queryset = Blog.objects.all()
        page = self.request.query_params.get('page',None)
        return queryset