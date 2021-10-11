from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serielizar import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#  Using the REST FRAMEWORK Generic Class VIEWS  **************************************

class MyGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

#  Using teh REST FRAMEWORK  CLASS BASED VIEWS  **************************************

class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serielizers = ArticleSerializer(articles, many=True)

        return Response(serielizers.data)

    def post(self, request):
        serielizer = ArticleSerializer(data=request.data)

        if serielizer.is_valid():
            serielizer.save()
            return Response(serielizer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serielizer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):
    def getObject(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.getObject(id)
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data)

    def put(self, request, id):
        article = self.getObject(id)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.getObject(id)
        article.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


#  Using teh REST FRAMEWORK  FUNCTION BASED VIEWS  **************************************

# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serielizers = ArticleSerializer(articles, many=True)

#         return Response(serielizers.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data)

#         if serielizer.is_valid():
#             serielizer.save()
#             return Response(serielizer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serielizer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'DELETE', 'PUT'])
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         article_serializer = ArticleSerializer(article)
#         return Response(article_serializer.data)
#     elif request.method == 'PUT':
#         serializer = ArticleSerializer(article, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#  Using ONLY DJANGO   **************************************

# @csrf_exempt
# def article_list(request):

#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serielizers = ArticleSerializer(articles, many=True)

#         return JsonResponse(serielizers.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serielizer = ArticleSerializer(data=data)

#         if serielizer.is_valid():
#             serielizer.save()
#             return JsonResponse(serielizer.data, status=201)
#         else:
#             return JsonResponse(serielizer.errors, status=400)

# @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         article_serializer = ArticleSerializer(article)
#         return JsonResponse(article_serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article, data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)