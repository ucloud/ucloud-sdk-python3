## 0.11.7 (2021-07-22)

ENHANCEMENTS:

- Update all APIs of `UHost` (#151)
- Update all APIs of `USMS` (#150)

## 0.11.6 (2021-07-08)

ENHANCEMENTS:

- Update all APIs of `UCDN` (#147)
- Update all APIs of `UK8S` (#145)

## 0.11.5 (2021-07-02)

ENHANCEMENTS:

- Update all APIs of `UMem` (#143)
- Update all APIs of `UCDN` (#142)

## 0.11.4 (2021-05-14)

ENHANCEMENTS:

- Update all APIs of `UAccount` (#139)
- Update all APIs of `UK8S` (#140)
- Update all APIs of `Cube` (#138)

## 0.11.3 (2021-05-08)

ENHANCEMENTS:

- Update all APIs of `UDDB` (#135)
- Update all APIs of `UDB` (#134)
- Update all APIs of `ULB` (#132)
- Update all APIs of `UMem` (#133)
- Update all APIs of `UFile` (#131)
- Update all APIs of `UBill` (#128)
- Update all APIs of `UEC` (#126)

## 0.11.2 (2021-04-30)

ENHANCEMENTS:

- Update all APIs of `UCDN` (#113)
- Update all APIs of `UBill` (#112)
- Update all APIs of `UDPN` (#112)
- Update all APIs of `UEC` (#110)
- Update all APIs of `USMS` (#109)
- Update all APIs of `VPC2.0` (#108)
- Update all APIs of `IPSecVPN` (#107)
- Update all APIs of `UNet` (#106)

## 0.11.1 (2021-04-28)

ENHANCEMENTS:

- Update all APIs of `UDDB` (#102)
- Update all APIs of `UCDN` (#103)
- Update all APIs of `UFS` (#101)
- Update all APIs of `UDisk` (#99)
- Update all APIs of `PathX` (#100)
- Update all APIs of `UHost` (#98)

## 0.11.0 (2021-04-22)

FEATURES:

- add `URocketMQ ` apis to be consistent with official document(#96 )
- add `ISMS ` apis to be consistent with official document(#95  )
- add `UGN ` apis to be consistent with official document(#94   )

ENHANCEMENTS:

- add U-Timestamp-Ms in request header for tracing the e2e latency

## 0.10.3 (2021-04-14)

## 0.10.2 (2021-03-03)

BUG FIXES:

- Fix `timeout` options for requests transport (#88)

## 0.10.1 (2021-02-07)

ENHANCEMENTS:

- Update all APIs of `VPC` (#82)
- Update all APIs of `UDisk` (#81)
- Update all APIs of `UNet` (#80)
- Update all APIs of `UHost` (#76)

BUG FIXES:

- (**BROKEN CHANGE**) Fix `DescribeRouteTable` field `SubnetCount` from `string` to `integer` (#82)
- (**BROKEN CHANGE**) Fix `CloneRouteTable` field `Region` as `Required` (#82)
- (**BROKEN CHANGE**) Fix `UHostDiskSet` field `Encrypted` from `string` to `boolean` (#76)

## 0.10.0 (2020-11-26)

FEATURES:

- Add product `UK8S`
- Add product `Cube`

## 0.9.4 (2020-09-25)

ENHANCEMENTS:

- Update all APIs of `UMem` (#195)

## 0.9.3 (2020-09-22)

BUG FIXES:

- Fix python 2 compatible helpers for nested CJK charset

## 0.9.2 (2020-07-31)

ENHANCEMENTS:

- Improve testing with `requests_mock`
- Add `InvalidResponseException` and `HTTPStatusException`
- Add `request_uuid` to response and exception logging
- Add default exception middileware
- Change documentation url
- Update all APIs of `UCloudStack`

BUG FIXES:

- Fix `pytest` version compatible

## 0.9.1 (2020-06-05)

ENHANCEMENTS:

- Add `CreateCertificate` api
- Add `DescribeCertificate` api
- Add `DeleteCertificate` api
- Add `DescribeOPLogs` api
- Update `DescribeVMInstance` api
- Update `CreateVS` api

## 0.9.0 (2020-05-21)

FEATURES:

- Add `ucloudstack` product

ENHANCEMENTS:

- Add `deprecated` decorator

## 0.8.2 (2020-03-12)

BUG FIXES:

- Fix `DescribeSubnetResource`

## 0.8.1 (2020-03-11)

ENHANCEMENTS:

- Update `DescribeSubnet` api

## 0.8.0 (2019-12-03)

FEATURES:

- Add `ufs` product (#42)

## 0.7.0 (2019-11-21)

FEATURES:

- Add ssl options of client (#37)

ENHANCEMENTS:

- Add testing report use ucloud test framework (#38)

## 0.6.2 (2019-10-25)

ENHANCEMENTS:

- Update fields of `UHost` api
- Add `DescribeIsolationGroup ` of `UHost`
- Add `DescribeUHostInstanceSnapshot` of `UHost`

BUG FIXES:

- Fix fields of `BatchDescribeNewUcdnDomain`

## 0.6.1 (2019-10-25)

BUG FIXES:

- fix `UCDN` response fields

## 0.6.0 (2019-10-23)

FEATURES:

- add `UCDN` product

ENHANCEMENTS:

- Add toolkit for auto release

