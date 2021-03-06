""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.usms.schemas import apis


class USMSClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(USMSClient, self).__init__(config, transport, middleware, logger)

    def create_usms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUSMSSignature - 调用接口CreateUSMSSignature申请短信签名

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **CertificateType** (int) - (Required) 签名的资质证明文件类型，需与签名类型保持一致，说明如下：0-三证合一/企业营业执照/组织机构代码证书/社会信用代码证书；1-应用商店后台开发者管理截图；2-备案服务商的备案成功截图(含域名，网站名称，备案号)；3-公众号或小程序的管理界面截图；4-商标注册证书；5-组织机构代码证书、社会信用代码证书；
        - **Description** (str) - (Required) 短信签名申请原因
        - **File** (str) - (Required) 短信签名的资质证明文件，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB
        - **SigContent** (str) - (Required) 短信签名名称；长度为2-12个字符, 可包含中文、数字和符号；无需填写【】或[]，系统会自动添加
        - **SigPurpose** (int) - (Required) 签名用途，0-自用，1-他用；
        - **SigType** (int) - (Required) 签名类型，说明如下：0-公司或企业的全称或简称；1-App应用的全称或简称；2-工信部备案网站的全称或简称；3-公众号或小程序的全称或简称；4-商标名的全称或简称；5-政府/机关事业单位/其他单位的全称或简称；
        - **ProxyFile** (str) - 短信签名授权委托文件，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB；当您是代理并使用第三方的签名时（也即SigPurpose为1-他用），该项为必填项；

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空
        - **SigContent** (str) - 短信签名名称
        - **SigId** (str) - 短信签名ID（短信签名申请时的工单ID）

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.CreateUSMSSignatureRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUSMSSignature", d, **kwargs)
        return apis.CreateUSMSSignatureResponseSchema().loads(resp)

    def create_usms_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """CreateUSMSTemplate - 调用接口CreateUSMSTemplate申请短信模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Purpose** (int) - (Required) 短信模板用途类型：1-验证码类短信模板；2-系统通知类短信模板；3-会员推广类短信模板；
        - **Template** (str) - (Required) 短信模板内容，说明如下：字数不超过500，每个中文、符号、英文、数组等都计为一个字；模板中的变量填写格式：{N}，其中N为大于1的整数，有多个参数时，建议N从1开始顺次，例如：{1}、{2}等；短信模板禁止仅包括变量的情况；
        - **TemplateName** (str) - (Required) 短信模板名称，不超过32个字符，每个中文、符号、英文、数字等都计为1个字。
        - **Remark** (str) - 短信模板申请原因说明，字数不超过128，每个中文、符号、英文、数字等都计为1个字。
        - **UnsubscribeInfo** (str) - 当Purpose为3时，也即会员推广类短信模板，该项必填。枚举值：TD退订、回T退订、回N退订、回TD退订、退订回T、退订回D、退订回TD、退订回复T、退订回复D、退订回复N、退订回复TD、拒收回T
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空
        - **TemplateId** (str) - 短信模板ID（短信模板申请时的工单ID）

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.CreateUSMSTemplateRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateUSMSTemplate", d, **kwargs)
        return apis.CreateUSMSTemplateResponseSchema().loads(resp)

    def delete_usms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUSMSSignature - 调用接口DeleteUSMSSignature删除短信签名

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **SigIds** (list) - (Required) 签名ID（也即短信签名申请时的工单ID），支持以数组的方式，举例，以SigIds.0、SigIds.1...SigIds.N方式传入

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.DeleteUSMSSignatureRequestSchema().dumps(d)

        resp = self.invoke("DeleteUSMSSignature", d, **kwargs)
        return apis.DeleteUSMSSignatureResponseSchema().loads(resp)

    def delete_usms_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """DeleteUSMSTemplate - 调用接口DeleteUSMSTemplate删除短信模板

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **TemplateIds** (list) - (Required) 模板ID（也即短信模板申请时的工单ID），支持以数组的方式，举例，以TemplateIds.0、TemplateIds.1...TemplateIds.N方式传入
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DeleteUSMSTemplateRequestSchema().dumps(d)

        resp = self.invoke("DeleteUSMSTemplate", d, **kwargs)
        return apis.DeleteUSMSTemplateResponseSchema().loads(resp)

    def get_usms_send_receipt(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetUSMSSendReceipt - 获取短信发送回执信息。下游服务提供商回执信息返回会有一定延时，建议发送完短信以后，5-10分钟后再调用该接口拉取回执信息。若超过12小时未返回，则请联系技术支持确认原因

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **SessionNoSet** (list) - (Required) 发送短信时返回的SessionNo集合，SessionNoSet.0,SessionNoSet.1....格式
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Data** (list) - 见 **ReceiptPerSession** 模型定义
        - **Message** (str) - 错误描述

        **Response Model**

        **ReceiptPerPhone**

        - **CostCount** (int) - 消耗短信条数
        - **Phone** (str) - 手机号码
        - **ReceiptDesc** (str) - 回执结果描述
        - **ReceiptResult** (str) - 回执结果
        - **ReceiptTime** (int) - 回执返回时间

        **ReceiptPerSession**

        - **ReceiptSet** (list) - 见 **ReceiptPerPhone** 模型定义
        - **SessionNo** (str) - 发送短信时返回的SessionNo

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUSMSSendReceiptRequestSchema().dumps(d)

        resp = self.invoke("GetUSMSSendReceipt", d, **kwargs)
        return apis.GetUSMSSendReceiptResponseSchema().loads(resp)

    def query_usms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """QueryUSMSSignature - 调用接口QueryUSMSSignature查询短信签名申请状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **SigContent** (str) - 签名内容；签名ID和签名至少需填写1项；
        - **SigId** (str) - 已申请的短信签名ID（短信签名申请时的工单ID）；签名ID和签名至少需填写1项；

        **Response**

        - **Data** (dict) - 见 **OutSignature** 模型定义
        - **Message** (str) - 发生错误时，表示具体错误描述

        **Response Model**

        **OutSignature**

        - **ErrDesc** (str) - 签名审核失败原因
        - **SigContent** (str) - 签名内容
        - **SigId** (str) - 签名ID
        - **Status** (int) - 签名状态。0-待审核 1-审核中 2-审核通过 3-审核未通过 4-被禁用

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.QueryUSMSSignatureRequestSchema().dumps(d)

        resp = self.invoke("QueryUSMSSignature", d, **kwargs)
        return apis.QueryUSMSSignatureResponseSchema().loads(resp)

    def query_usms_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """QueryUSMSTemplate - 调用接口QueryUSMSTemplate查询短信模板申请状态

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **TemplateId** (str) - (Required) 模板ID

        **Response**

        - **Data** (dict) - 见 **OutTemplate** 模型定义
        - **Message** (str) - 当RetCode不为0时，Message中显示具体错误描述

        **Response Model**

        **OutTemplate**

        - **CreateTime** (int) - 创建时间
        - **ErrDesc** (str) - 审核失败原因
        - **Purpose** (int) - 模板类型，选项：1-验证码类 2-通知类 3-会员推广类
        - **Remark** (str) - 模板说明
        - **Status** (int) - 短信模板状态；状态说明：0-待审核，1-审核中，2-审核通过，3-审核未通过，4-被禁用
        - **Template** (str) - 短信模板内容
        - **TemplateId** (str) - 短信模板ID
        - **TemplateName** (str) - 短信模板名称
        - **UnsubscribeInfo** (str) - 退订信息；一般填写方式“回T退订”，当purpose为3（也即会员推广类）时，为必填项

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.QueryUSMSTemplateRequestSchema().dumps(d)

        resp = self.invoke("QueryUSMSTemplate", d, **kwargs)
        return apis.QueryUSMSTemplateResponseSchema().loads(resp)

    def send_usms_message(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """SendUSMSMessage - 发送短信息。短信字数超过70个后，按照每66个进行切割(因为要加上1/3), 2/3)等字样，占用4个字长)。短信最大长度不能超过600个字。每个汉字、数字、字母、字符都按一个字计

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **PhoneNumbers** (list) - (Required) 电话号码数组，电话号码格式为(60)1xxxxxxxx，()中为国际长途区号(如中国为86或0086，两种格式都支持)，后面为电话号码.若不传入国际区号，如1851623xxxx，则默认为国内手机号
        - **TemplateId** (str) - (Required) 模板ID。若指定的模板ID审核未通过(status不等于2)则不允许发送
        - **TemplateParams** (list) - (Required) 模板参数数组，以TempalteParams.0，TempalteParams.1.。。格式。若模板ID指定的模板无可变参数，则不传入该参数。模板参数个数与模板不匹配，则不允许发送
        - **SigContent** (str) - 使用的签名，如果不输入则使用默认签名，若没有申请默认签名不允许发送；若输入的签名没有申请，则无法发送
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Action** (str) - 操作名称
        - **Message** (str) - 发生错误时表示错误描述
        - **RetCode** (int) - 返回码
        - **SessionNo** (str) - 本次提交发送的短信的唯一ID，可根据该值查询本次发送的短信列表

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.SendUSMSMessageRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("SendUSMSMessage", d, **kwargs)
        return apis.SendUSMSMessageResponseSchema().loads(resp)

    def update_usms_signature(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateUSMSSignature - 调用接口UpdateUSMSSignature修改未通过审核的短信签名，并重新提交审核

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **File** (str) - (Required) 短信签名的资质证明文件，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB
        - **SigContent** (str) - (Required) 新的短信签名名称；长度为2-12个字符, 可包含中文、数字和符号；无需填写【】或[]，系统会自动添加
        - **SigId** (str) - (Required) 签名ID（也即短信签名申请时的工单ID），支持以数组的方式，举例，以SigIds.0、SigIds.1...SigIds.N方式传入
        - **SigPurpose** (int) - (Required) 签名用途，0-自用，1-他用；
        - **SigType** (int) - (Required) 签名类型，说明如下：0-公司或企业的全称或简称；1-App应用的全称或简称；2-工信部备案网站的全称或简称；3-公众号或小程序的全称或简称；4-商标名的全称或简称；5-政府/机关事业单位/其他单位的全称或简称；
        - **CertificateType** (int) - 签名的资质证明文件类型，需与签名类型保持一致，说明如下：0-三证合一/企业营业执照/组织机构代码证书/社会信用代码证书；1-应用商店后台开发者管理截图；2-备案服务商的备案成功截图(含域名，网站名称，备案号)；3-公众号或小程序的管理界面截图；4-商标注册证书；5-组织机构代码证书、社会信用代码证书；
        - **ProxyFile** (str) - 短信签名授权委托文件，需先进行base64编码格式转换，此处填写转换后的字符串。文件大小不超过4 MB；当您是代理并使用第三方的签名时（也即SigPurpose为1-他用），该项为必填项；

        **Response**

        - **Message** (str) - 返回状态码描述，如果操作成功，默认返回为空

        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.UpdateUSMSSignatureRequestSchema().dumps(d)

        resp = self.invoke("UpdateUSMSSignature", d, **kwargs)
        return apis.UpdateUSMSSignatureResponseSchema().loads(resp)

    def update_usms_template(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """UpdateUSMSTemplate - 调用接口UpdateUSMSTemplate修改未通过审核的短信模板，并重新提交审核

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_
        - **Template** (str) - (Required) 新的模板内容。模板名称和模板内容必须提供一个，否则会报错。小于等于600个字
        - **TemplateId** (str) - (Required) 短信模板ID
        - **Remark** (str) - 短信模板申请原因说明，字数不超过128，每个中文、符号、英文、数字等都计为1个字。
        - **TemplateName** (str) - 新的模板名称。小于等于32个字，每个中文、英文、数组、符合都计为一个字
        - **UnsubscribeInfo** (str) - 当Purpose为3时，也即会员推广类短信模板，该项必填。枚举值：TD退订、回T退订、回N退订、回TD退订、退订回T、退订回D、退订回TD、退订回复T、退订回复D、退订回复N、退订回复TD、拒收回T
        - **Zone** (str) - 可用区。参见  `可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_

        **Response**

        - **Message** (str) - 发生错误时表示错误描述

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.UpdateUSMSTemplateRequestSchema().dumps(d)

        resp = self.invoke("UpdateUSMSTemplate", d, **kwargs)
        return apis.UpdateUSMSTemplateResponseSchema().loads(resp)
