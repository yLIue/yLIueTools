# yLIueTools

yLIueTools包含自己正在使用的一些python小工具

当前版本: 1.0.5

代码最新更新时间: 2025.10.23

github项目地址: [yLIueTools](https://github.com/yLIue/yLIueTools)

## 描述

每一个代码萌新都会自己尝试造轮子,这是我自己尝试写的方便自己用的小工具

可能有些功能会跟其他包冲突了,主要还是自己方便嘛

该包包含内容:

- 方便调试和筛选输出信息的Debug模块
- 方便输出带有颜色字体的Color模块

## 目录

[1.描述](#描述)

[2.安装流程](#安装流程)

[3.Debug模块使用说明](#Debug模块使用说明)

[4.DebugAPI](#DebugAPI)

[5.Color模块使用说明](#Color模块使用说明)

[6.UpdateLog](#UpdateLog)

## 安装流程

使用pip进行安装

```python
pip install yliuetools
```

## Debug模块使用说明

### 注意

Debug包会调用Color包的函数，Color的**颜色显示**在**不支持ANSI转义序列**的终端会出现**乱码**的情况
你可以通过关闭颜色来让其正常显示

```python
debug = Debug("Test")
debug.logSet(_color=False)
```

### 初步使用

1. 引入该包

```python
from MxTools import Debug
```

2.定义一个Debug对象

```python
debug = Debug('Test')
# debug = Debug('project_name') 
# project_name 为项目的名称 type:str
```

3.使用Debug模块输出信息

```python
debug.log('Hello World!')
# 输出
# [2025-09-21 16:01:47,299] ING Test.default: Hello World!
```

4.关闭Debug输出

```python
debug = Debug('Test', False)
```

## DebugAPI

### .log

```python
.log(_msg, _func, _type)
```

使用log输出时有3个**str**参数,分别是:

- **_msg**(输出信息) 
- **_func**(当前函数名,默认为default.开启自动填充后默认为当前函数名)
- **_type**(信息类型,默认为ING)

#### 存在type的类型

| typeName | 说明                |
| -------- | ------------------- |
| ING      | 标记为运行信息      |
| ERR      | 标记为错误信息      |
| PRIVATE  | 标记为Debug内部信息 |
| TIPS     | 标记为输出信息      |
| GLOBAL   | 标记为全局信息      |
| OUTPUT   | 标记为输出信息      |

### .logSet

```python
.logset(_tips, _color, _fillFunc, _time)
```

logSet共有4个**bool**参数,分别是

- **_tips**(提示输出开关,默认为开启)
- **_color**(颜色显示开关,默认为开启)
- **_fillFunc**(默认填充函数名开关,默认为关闭)
  - 默认填充数量多了可能会对性能产生影响
- **_time**(时间显示开关,默认开启)

### .logSetReset

重置输出设置

### .filter

```python
.filter(_func, _type)
```

filter共有2个**str**参数,分别是

- **_func**(筛选函数名)
- **_type**(筛选类型)

当参数为**all**时表示筛选全部输出

### .filterReset

重置筛选器

## Color模块使用说明

### 注意

Color包的**颜色显示**在**不支持ANSI转义序列**的终端会出现**乱码**的情况

### 初步使用

 1.引入该包

 ```python
 from MxTools import Color
 ```

 2.输出紫色字体

 ```python
  print(Color.purple('Hello World!'))
 ```

### ColorAPI

- purple 紫色
- grey 灰色
- green 绿色
- red 红色
- blue 蓝色
- yellow 黄色
- cyan 青色

## UpdateLog

`Ver1.0.1 2025.09.21` 第一次上传

`Ver1.0.2 2025.09.22` 修改了部分项目说明的编写错误 debug.rEnd修复了文件夹读取与实际不符合的bug,不要使用没提到的功能,即便它有,这极其不稳定

`Ver1.0.3 2025.09.22` 修改了部分项目说明的编写错误

`Ver1.0.4 2025.09.22` 修复Debug筛选器筛选问题,加入了屏蔽提示的开关,更好的项目说明

筛选器Bug...这个真是核心的问题,都是因为自己不够小心,Orz不好意思qaq,幸好没人用

`ver1.0.5 2025.10.23` 修复一些小bug

1. 将颜色设置中Debug类移至logSet

2. 增加logSet,并在内增加了1.提示输出开关2.颜色显示开关3.默认填充函数名开关4.时间显示开关

3. 将筛选器单独分离了出来,增加filter方法

4. 增加了logSet和filter的重置方法

5. 修改了项目说明的一些问题