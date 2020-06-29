from django.shortcuts import render

# Create your views here.
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser,FormParser, MultiPartParser
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import UserInfo, Student, Employee
# from .serializers import EmployeeModelSerializer, EmployeeDeserializer


def user(request):
    print("请求到达")
    if request.method=="GET":
        print("GET")
        return HttpResponse("GET SUCCESS")
    elif request.method=="POST":
        print("POST")
        return HttpResponse("POST SUCCESS")
    elif request.method == "PUT":
        print("PUT 修改")
        return HttpResponse("PUT SUCCESS")
    elif request.method == "DELETE":
        print("DELETE 删除")
        return HttpResponse("DELETE SUCCESS")

@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    def get(self, request, *args, **kwargs):
        print("GET API")
        user_id = kwargs.get("pk")
        if user_id:
            # 查询单个
            user_values = UserInfo.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user_values:
                return Response({
                    "status": 200,
                    "message": "获取用户成功",
                    "results": user_values})
        else:
            user_list = UserInfo.objects.all().values("username", "password", "gender")
            if user_list:
                return Response({
                    "status": 201,
                    "message": "获取用户列表成功",
                    "results": list(user_list)
                })

        return Response({
            "status": 400,
            "message": "获取用户不存在",
        })

    def post(self, request, *args, **kwargs):
        """完成新增单个用户的操作"""
        print(request.POST)
        try:
            user_obj = UserInfo.objects.create(**request.POST.dict())
            if user_obj:
                return Response({
                    "status": 200,
                    "message": "新增用户成功",
                    "results": {"username": user_obj.username, "gender": user_obj.gender}
                })
            else:
                return Response({
                    "status": 500,
                    "message": "新增用户失败",
                })
        except:
            return Response({
                "status": 501,
                "message": "参数有误",
            })

    def put(self, request, *args, **kwargs):
        username = request.username
        password = request.password
        gender = request.gender
        user_id = kwargs.get("pk")
        user = UserInfo.objects.filter(pk=user_id).first()
        if user:
            user_obj = UserInfo.objects.create(username=username,password=password,gender=gender)
            if user_obj:
                return Response({
                    "status":200,
                    "message":"修改用户信息成功",
                    "results":{"username":user_obj.username,"password":user_obj.password,"gender":user_obj.gender}
                })
            else:
                return Response({
                    "status": 500,
                    "message": "修改用户信息失败"
                })
        else:
            return Response({
                "status":500,
                "message":"修改用户信息失败"
            })


    def delete(self, request, *args, **kwargs):
        user_id = kwargs.get("pk")
        if user_id:
            user = UserInfo.objects.filter(pk=user_id).delete()
            return Response({
                "status": 200,
                "message": "删除用户成功"
            })
        else:
            return Response({
                "status": 500,
                "message": "删除用户信息失败"
            })

class StudentView(APIView):
    # renderer_classes = [BrowsableAPIRenderer]
    parser_classes = [JSONParser]
    # parser_classes = [MultiPartParser]
    # parser_classes = [FormParser]
    def get(self, request, *args, **kwargs):
        print(request._request.GET)
        # 通过DRF 的request对象获取参数
        print(request.GET)
        # 通过quer_params来获取参数
        print(request.query_params)
        stu_id = kwargs.get("demo")
        if stu_id:
            stu_obj = UserInfo.objects.get(pk=stu_id)
            # 如果有值  代表查询成功
            if stu_obj:
                return Response({
                    "status": 200,
                    "message": "GET USER SUCCESS",
                    "results": stu_obj,
                })
            else:
                # 代表查询的用户信息不存在
                return Response({
                    "status": 403,
                    "message": "查询的用户不存在",
                })
        # id如果不存在  代表查询的是全部的用户信息
        else:
            stu_val = UserInfo.objects.all().values("username", "password", "gender")
            return Response({
                "status": 200,
                "message": "查询所有用户成功",
                "results": list(stu_val)
            })

    def post(self,request,*args,**kwargs):
        print(request.POST.dict())
        print(request._request.POST)  # Django 原生的request对象
        print(request.POST)  # DRF 封装后的request对象
        print(request.data)

        try:
            stu_obj = UserInfo.objects.create(**request.POST.dict())
            if stu_obj:
                return Response({
                    "status": 200,
                    "message": "添加学生成功",
                    "results":{
                        "username":stu_obj.username,
                        "password":stu_obj.password
                    }
                })
            else:
                return Response({
                    "status": 500,
                    "message": "添加学生失败"
                })
        except:
            return Response({
                "status": 501,
                "message": "参数有误"
            })
