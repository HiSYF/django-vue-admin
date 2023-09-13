from django.shortcuts import render

# Create your views here.
from lkapp.models import LkappModel
from lkapp.serializers import LkappModelSerializer, LkappModelCreateUpdateSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class LkappDemoModelViewSet(CustomModelViewSet):
    """
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = LkappModel.objects.all()
    serializer_class = LkappModelSerializer
    create_serializer_class = LkappModelCreateUpdateSerializer
    update_serializer_class = LkappModelCreateUpdateSerializer
    filter_fields = ['lk_name', 'server_web_port']
    search_fields = ['lk_name']