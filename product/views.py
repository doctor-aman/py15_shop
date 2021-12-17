from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from product.filters import ProductFilter
from product.models import Product, Category, Comment
from product.permissions import IsAdmin, IsAuthor
from product.serializers import ProductSerializer, ProductsListSerializer, CategorySerializer, CommentSerializer


# # 1 Variant
# @api_view(['GET'])
# def products_list(request):
#     products = Product.objects.all()  # select * from products;
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)
#
#
# # 2 Variant
# class ProductsListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()  # select * from products;
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


# 3 Variant
# CRUD (Create(создание), Retrive (Чтение), Update(изменение), Delete(удаление))

# class ProductsListView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductsListSerializer
#
#
# class ProductDetailView(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CreateProductView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class UpdateProductView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class DeleteAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# 4 Variant
# class ProductListCreateView(ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# 5 Variant

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]  # проверка на права пользователя
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]  # добавляем фильтрацию
    filterset_class = ProductFilter
    search_fields = ['name']  # поиск по имени
    ordering_fields = ['name', 'price']

    # api/v1/products/id/comments/
    @action(['GET'], detail=True)
    def comments(self, request, pk):
        product = self.get_object()
        comments = product.comments.all()  # queryset сделали
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    # def get_permissions(self):
    #     if self.action == 'comment':
    #         return []
    #     return [IsAdmin]

    # # api/v1/1/comment
    # @action(['POST'], detail = True)
    # def comment(self, request, pk):
    #     product = self.get_object()
    #     data = {'product': product.id}
    #     data.update(request.data)
    #     serializer = CommentSerializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response('Комментарий успешно добавлен', status=201)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


# class CreateCommentView(CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class UpdateCommentView(UpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthor]

# class DeletedCommentView(DestroyAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthor | IsAdmin]


class CommentViewSet(GenericViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return [IsAuthor()]

# TODO: пройтись по всем запросам
# TODO: комментарии к продуктам
# TODO: Заказы
# TODO: Тесты
# TODO: GIT
# TODO: Документация
