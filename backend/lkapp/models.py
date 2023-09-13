from django.db import models
from dvadmin.utils.models import CoreModel
from uuid import uuid4

# Create your models here.
class LkappModel(CoreModel):
    server_web_port = models.IntegerField(verbose_name="web端口")
    server_ssh_port = models.IntegerField(verbose_name="ssh端口")
    lk_name = models.CharField(max_length=255, verbose_name="粮库名称")
    city = models.CharField(max_length=255, verbose_name="城市")
    lmt_username = models.CharField(max_length=255, verbose_name="流媒体账号")
    lmt_password = models.CharField(max_length=255, verbose_name="流媒体密码")
    serve_username = models.CharField(max_length=255, verbose_name="服务器账号")
    server_password = models.CharField(max_length=255, verbose_name="服务器密码")
    server_keygen = models.CharField(max_length=255, verbose_name="服务器公钥")
    server_ip = models.CharField(max_length=255, verbose_name="服务器ip")


    class Meta:
        db_table = "lk_serve_basis"
        verbose_name = '粮库服务器基础信息'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
        # fields = ['server_web_port', 'server_ssh_port', 'lk_name', 'city', 'lmt_username',
        #           'lmt_password', 'serve_username', 'server_password', 'server_keygen', 'server_ip']