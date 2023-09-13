from lkapp.models import LkappModel
from dvadmin.utils.serializers import CustomModelSerializer


class LkappModelSerializer(CustomModelSerializer):
    """
    序列化器
    """

    class Meta:
        model = LkappModel
        fields = "__all__"


class LkappModelCreateUpdateSerializer(CustomModelSerializer):
    """
    创建/更新时的列化器
    """

    class Meta:
        model = LkappModel
        fields = '__all__'