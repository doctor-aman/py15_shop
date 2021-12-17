from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (RegisterSerializer, ActivationSerializer, LoginSerializer, ChangePasswordSerializer,
                          ForgotPasswordSerializer, ForgotPasswordCompleteSerializer)


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.create()
            message = f'Вы успешно зарегистрированы. ' \
                      f'Вам отправлено письмо с активацией'
            return Response(message, status=201)


class ActivationView(APIView):
    def post(self, request):
        data = request.data
        serializer = ActivationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Ваш аккаунт успешно активирован')


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer



class LogoutView(APIView):
    permission_classes = [IsAuthenticated] # проверка на наличие права
    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно разлогинились')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        serializer = ChangePasswordSerializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Пароль успешно обновлен')


class ForgotPasswordView(APIView):
    def post(self,request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return  Response('Вам отправлено письмо для восстановления пароля')

class ForgotPasswordComlete(APIView):
    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_pass()
        return Response('Пароль успешно обновлен')

# MVC (Model-View-Controller)
# Model - связь с БД (models.py)
# View - представление данных (serializer.py)
# Controller - обработчик запросов (views.py)

# API (application Programming Intrface) - интерфейс для пвзаимодейтсвия программ

# RESTful API- API отвечающий стилю REST
# REST  это архитектурныё стиль, набор правил для построения приложения
# Имеет следующие правила:

# 1. Модель клиент-сервер

# 2.отсутствие состояние клиента(на сервере не хранится данные о том , залогинен пользователь или нет)

# 3.Кэширование- временное хранение данных

# 4.Единообразие интерфейса- единый подход ко всем ресурсам



# GET api/v1/product - список
# POST api/v1/product - создание