# 一、程序业务逻辑:  
A、从表 area_code 中拿到一些区号  
B、在表 enterprise\_enable\_info 和 number\_rule\_info  
C、在表 number_pool 中插入一条数据，相当于建一个池子  
D、在表 number_group 中插入一条数据，相当于新建一个组  
E、拿到新建的的池编号a和组编号b  
F、在表 pool\_group\_relation 中插入池子a 和 组b之间的绑定关系  
G、在表 dialout\_number\_info 中插入数据以新建号码，并在表 group\_number_relation   中插入数据，以新建号码和组之间的绑定关系  
H、在 isp 表中插入数据，以对号码的频次并发，进行控制  

|功能|指导思想|使用|编译环境
|-|-|-|-
|针对一个所配置的 enterprise\_id ，生成一个可用的号码池和号码组，策略是，非溢出，主叫区域外显|把号码平均分到 isp 、 area_code 和 是否全国上面|支持，企业不存在的情况，如果企业存在，可能会有问题|python 3.7 

# 二、程序使用

|para|enterprise\_id|start\_num|number\_count|isp\_identity|isp\_count|areaCode_count|
|-|-|-|-|-|-|-
||企业id|第一个号码|号码的数量|isp的组成部分|isp 的数量|区号的数量
