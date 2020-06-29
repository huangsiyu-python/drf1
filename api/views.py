from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Employee, Student
from .serializers import EmployeeSerializer, EmployeeDeSerializer, StudentSerializer, StudentDeSerializer


class EmployeeAPIView(APIView):

    def get(self, request, *args, **kwargs):

        user_id = kwargs.get("pk")

        if user_id:
            emp_obj = Employee.objects.get(pk=user_id)
            emp_ser = EmployeeSerializer(emp_obj)
            data = emp_ser.data

            return Response({
                "status": 200,
                "msg": "查询单个员工成功",
                "results": data,
            })
        else:
            emp_list = Employee.objects.all()
            emp_list_ser = EmployeeSerializer(emp_list, many=True).data

            return Response({
                "status": 200,
                "msg": "查询所有员工成功",
                "results": emp_list_ser,
            })

    def post(self, request, *args, **kwargs):
        user_data = request.data
        if not isinstance(user_data, dict) or user_data == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })
        serializer = EmployeeDeSerializer(data=user_data)
        # print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            emp_obj = serializer.save()
            return Response({
                "status": 201,
                "msg": "用户创建成功",
                "results": EmployeeSerializer(emp_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                "results": serializer.errors
            })
class StudentAPIView(APIView):
    def get(self, request, *args, **kwargs):

        user_id = kwargs.get("pk")

        if user_id:
            stu_obj = Student.objects.get(pk=user_id)
            stu_ser = StudentSerializer(stu_obj)
            data = stu_ser.data

            return Response({
                "status": 200,
                "msg": "查询单个员工成功",
                "results": data,
            })
        else:
            stu_list = Student.objects.all()
            stu_list_ser = StudentSerializer(stu_list, many=True).data

            return Response({
                "status": 200,
                "msg": "查询所有员工成功",
                "results": stu_list_ser,
            })

    def post(self, request, *args, **kwargs):
        user_data = request.data
        print(user_data)
        if not isinstance(user_data, dict) or user_data == {}:
            return Response({
                "status": 501,
                "msg": "数据有误",
            })
        serializer = StudentDeSerializer(data=user_data)
        # print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            stu_obj = serializer.save()
            return Response({
                "status": 201,
                "msg": "用户创建成功",
                "results": StudentSerializer(stu_obj).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                "results": serializer.errors
            })