""" Code is generated by ucloud-model, DO NOT EDIT IT. """

import typing


from ucloud.core.client import Client
from ucloud.services.ubill.schemas import apis


class UBillClient(Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        super(UBillClient, self).__init__(config, transport, middleware, logger)

    def get_balance(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """GetBalance - 获取账户余额

        **Request**


        **Response**

        - **AccountInfo** (dict) - 见 **AccountInfo** 模型定义

        **Response Model**

        **AccountInfo**
        - **Amount** (str) - 账户余额
        - **AmountAvailable** (str) - 账户可用余额
        - **AmountCredit** (str) - 信用账户余额
        - **AmountFree** (str) - 赠送账户余额
        - **AmountFreeze** (str) - 冻结账户金额


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetBalanceRequestSchema().dumps(d)

        resp = self.invoke("GetBalance", d, **kwargs)
        return apis.GetBalanceResponseSchema().loads(resp)

    def get_bill_data_file_url(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """GetBillDataFileUrl - 生成账单数据文件下载的 url

        **Request**

        - **BillType** (int) - (Required) 账单类型，传 0 时获取账单总览报表，传 1 获取账单明细报表
        - **BillingCycle** (str) - (Required) 账期(字符串格式，YYYY-MM，例如2021-08).   若BillingCycle 和 BillPeriod同时存在，BillingCycle 优先
        - **BillPeriod** (int) - 此字段不推荐使用，建议使用BillingCycle.   若BillingCycle 和 BillPeriod同时存在，BillingCycle 优先
        - **PaidType** (int) - 获取账单总览报表时，账单的支付状态，传 0 时获取待支付账单，传 1 时获取已支付账单。获取账单明细报表时该参数无效
        - **RequireVersion** (str) - 如需求其他语言版本的账单则使用此参数。默认中文。如 RequireVersion = "EN"，则提供英文版本账单。
        - **Version** (str) - 文件版本，若为"v1"表示获取带有子用户信息的账单，可以为空

        **Response**

        - **FileUrl** (str) - 交易账单数据下载URL
        - **IsValid** (str) - 生成的 URL是否有效，即有对应数据文件

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetBillDataFileUrlRequestSchema().dumps(d)

        resp = self.invoke("GetBillDataFileUrl", d, **kwargs)
        return apis.GetBillDataFileUrlResponseSchema().loads(resp)

    def list_u_bill_detail(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUBillDetail - 获取某个账期内的所有消费。

        **Request**

        - **BillingCycle** (str) - (Required) 账期，YYYY-MM，比如2021-08，只支持2018-05之后的查询
        - **ChargeType** (str) - 计费方式 (筛选项, 默认全部)
        - **Limit** (int) - 每页数量，默认值25，最大值：100。
        - **Offset** (int) - 数据偏移量 (默认0)
        - **OrderType** (str) - 订单类型 (筛选项, 默认全部)
        - **PaidState** (int) - 支付状态 (筛选项, 1:仅显示未支付订单; 2:仅显示已支付订单; 0:两者都显示)
        - **ProjectName** (str) - 项目名称 (筛选项, 默认全部)
        - **ResourceIds** (list) - 资源ID(筛选项, 默认全部)	支持多筛选，多筛选请在请求参数中添加多个字段例ResourceIds.0: uhost-bzgf1gh5，ResourceIds.1: uhost-gu1xpspa，
        - **ResourceTypes** (list) - 产品类型 (筛选项, 默认全部),支持多筛选，多筛选请在请求参数中添加多个字段例ResourceTypes.0: uhost，ResourceTypes.1: udisk，ResourceTypes.2: udb，
        - **ShowZero** (int) - 是否显示0元订单 (0 不显示, 1 显示, 默认0)
        - **UserEmail** (str) - 用户邮箱，可以根据用户邮箱来进行筛选

        **Response**

        - **Items** (list) - 见 **BillDetailItem** 模型定义
        - **TotalCount** (int) - 账单明细总长度

        **Response Model**

        **ResourceExtendInfo**
        - **KeyId** (str) - 资源标识健
        - **Value** (str) - 资源标识值


        **ItemDetail**
        - **ProductName** (str) - 产品小类名称
        - **Value** (str) - 产品小类规格


        **BillDetailItem**
        - **Admin** (int) - 是否为主账号
        - **Amount** (str) - 订单总金额
        - **AmountCoupon** (str) - 代金券抵扣
        - **AmountFree** (str) - 赠送金额抵扣
        - **AmountReal** (str) - 现金账户支付
        - **AzGroupCName** (str) - 可用区
        - **ChargeType** (str) - 计费方式
        - **CreateTime** (int) - 创建时间（时间戳）
        - **ItemDetails** (list) - 见 **ItemDetail** 模型定义
        - **OrderNo** (str) - 订单号
        - **OrderType** (str) - 订单类型
        - **ProjectName** (str) - 项目名称
        - **ResourceExtendInfo** (list) - 见 **ResourceExtendInfo** 模型定义
        - **ResourceId** (str) - 资源ID
        - **ResourceType** (str) - 产品类型
        - **ResourceTypeCode** (int) - 产品类型代码
        - **ShowHover** (int) - 订单支付状态
        - **StartTime** (int) - 开始时间（时间戳）
        - **UserDisplayName** (str) - 账户昵称
        - **UserEmail** (str) - 账户邮箱
        - **UserName** (str) - 账户名


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.ListUBillDetailRequestSchema().dumps(d)

        resp = self.invoke("ListUBillDetail", d, **kwargs)
        return apis.ListUBillDetailResponseSchema().loads(resp)

    def list_u_bill_overview(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ListUBillOverview - 账单总览。可按产品/项目/用户纬度获取某个账期内账单总览信息。

        **Request**

        - **BillingCycle** (str) - (Required) 账期，YYYY-MM格式，例如2022-02，只支持2018-05之后的查询
        - **Dimension** (str) - (Required) 账单维度, product 按产品聚合,project 按项目聚合，user 按子账号聚合
        - **HideUnpaid** (int) - 是否显示已入账账单, 1 已入账, 0 待入账 (默认0 )

        **Response**

        - **Items** (list) - 见 **BillOverviewItem** 模型定义
        - **TotalCount** (int) - 账单总览数据总数
        - **TotalPaidAmount** (str) - 已入账订单总额（已入账时显示）
        - **TotalPaidAmountReal** (str) - 现金账户扣款总额	（已入账时显示）
        - **TotalUnpaidAmount** (str) - 待入账订单总额（待入账时显示）

        **Response Model**

        **BillOverviewItem**
        - **Admin** (int) - 该账户是否为主账号，1 主账号，0 子账号（账单维度按子账号筛选时显示）
        - **Amount** (str) - 订单总金额
        - **AmountCoupon** (str) - 代金券抵扣（已入账时显示）
        - **AmountFree** (str) - 赠送金额抵扣（已入账时显示）
        - **AmountReal** (str) - 现金账户支付（已入账时显示）
        - **Dimension** (str) - 账单维度, product 按产品维度聚合,project 按项目维度聚合，user 按子账号维度聚合
        - **ProductCategory** (str) - 产品分类	（账单维度按产品筛选时显示）
        - **ProjectName** (str) - 项目名称（账单维度按项目筛选时显示）
        - **ResourceType** (str) - 产品类型	（账单维度按产品筛选时显示）
        - **ResourceTypeCode** (int) - 产品类型代码（账单维度按产品筛选时显示）
        - **UserDisplayName** (str) - 账户昵称（账单维度按子账号筛选时显示）
        - **UserEmail** (str) - 账户邮箱（账单维度按子账号筛选时显示）
        - **UserName** (str) - 账户名   （账单维度按子账号筛选时显示）


        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.ListUBillOverviewRequestSchema().dumps(d)

        resp = self.invoke("ListUBillOverview", d, **kwargs)
        return apis.ListUBillOverviewResponseSchema().loads(resp)
