import sys
sys.path.append("..")

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models
import environment_variables

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
    # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。密钥可前往官网控制台 https://console.tencentcloud.com/capi 进行获取
    cred = credential.Credential(environment_variables.SECRETID, environment_variables.SECRETKEY)
    # 实例化一个http选项，可选的，没有特殊需求可以跳过
    httpProfile = HttpProfile()
    httpProfile.endpoint = "cvm.tencentcloudapi.com"

    # 实例化一个client选项，可选的，没有特殊需求可以跳过
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # 实例化要请求产品的client对象,clientProfile是可选的
    client = cvm_client.CvmClient(cred, "ap-singapore", clientProfile)

    # 实例化一个请求对象,每个接口都会对应一个request对象
    req = models.DescribeInstancesRequest()
    params = {
        "InstanceIds": [
            "ins-rgferfer"
        ]
    }

    req.from_json_string(json.dumps(params))

    # 返回的resp是一个DescribeInstancesResponse的实例，与请求对象对应
    resp = client.DescribeInstances(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)