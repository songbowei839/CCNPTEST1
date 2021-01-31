# 一、程序业务逻辑:  
A、从表 area_code 中拿到一些区号  
B、在表 enterprise\_enable\_info 和 number\_rule\_info 插入企业开关   
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

#  三、程序调用      
>curl -v 'http://127.0.0.1:11400/api/v1/entid/2011240005/ani/tel:010/uri/15034100163/number?pool=912&group=91'   

&emsp;&emsp;把对应的池子和组替换一下就ok了，其它都不用换，因为是按主叫选，010的区号肯定造的是有号码   

# 展望   
&emsp;&emsp;接下来需要做的就是把 main.py 和 delete_enterprise.py 需要的参数从外面传过来，而不是每次都要改 main.py 和 delete_enterprise.py ，或者加个配置文件也行啊    