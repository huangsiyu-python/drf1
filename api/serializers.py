from rest_framework import serializers
from api.models import Employee, Student
from drf1 import settings

class EmployeeSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()
    salt = serializers.SerializerMethodField()
    def get_salt(self, obj):
        return "salt"
    gender = serializers.SerializerMethodField()
    def get_gender(self, obj):
        # print(obj.gender, type(obj))
        return obj.get_gender_display()
    # 自定义返回图片的全路径
    pic = serializers.SerializerMethodField()
    def get_pic(self, obj):
        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))
class EmployeeDeSerializer(serializers.Serializer):
    # 添加反序列化校验规则
    username = serializers.CharField(
        max_length=8,
        min_length=4,
        error_messages={
            "max_length": "太长了",
            "min_length": "太短了",
        }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()
    def create(self, validated_data):
        # print(validated_data)
        return Employee.objects.create(**validated_data)
class StudentSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField()
    # gender = serializers.IntegerField()
    # pic = serializers.ImageField()
    salt = serializers.SerializerMethodField()
    def get_salt(self, obj):
        return "salt"
    gender = serializers.SerializerMethodField()

    def get_gender(self, obj):
        # print(obj.gender, type(obj))
        return obj.get_gender_display()
    # 自定义返回图片的全路径
    pic = serializers.SerializerMethodField()
    def get_pic(self, obj):
        return "%s%s%s" % ("http://127.0.0.1:8000", settings.MEDIA_URL, str(obj.pic))


class StudentDeSerializer(serializers.Serializer):
    username = serializers.CharField(
        # max_length=8,
        # min_length=4,
        # error_messages={
        #     "max_length": "太长了",
        #     "min_length": "太短了",
        # }
    )
    password = serializers.CharField(required=False)
    phone = serializers.CharField()
    def create(self, validated_data):
        # print(validated_data)
        return Student.objects.create(**validated_data)