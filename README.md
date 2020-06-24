|para|enterprise\_id|start\_num|number\_count|isp\_identity|isp\_count|areaCode_count|
|-|-|-|-|-|-|-
||企业id|第一个号码|号码的数量|isp的组成部分|isp 的数量|区号的数量


|功能|指导思想|使用|编译环境
|-|-|-|-
|针对一个所配置的 enterprise\_id ，生成一个可用的号码池和号码组，策略是，非溢出，主叫区域外显|把号码平均分到 isp 、 area_code 和 是否全国上面|支持，企业不存在的情况，如果企业存在，可能会有问题|python 3.7 
