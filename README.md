# yLIueTools

yLIueTools包含自己正在使用的一些python小工具

当前版本: 1.0.4

代码最新更新时间: 2025.09.22

github项目地址: [yLIueTools](https://github.com/yLIue/yLIueTools)

## 描述 <a id="description"></a>

每一个代码萌新都会自己尝试造轮子,这是我自己尝试写的方便自己用的小工具

可能有些功能会跟其他包冲突了,主要还是自己方便嘛

该包包含内容:

- 方便调试和筛选输出信息的Debug模块
- 方便输出带有颜色字体的Color模块

## 目录

[1.描述](#description)

[2.安装流程](#Install)

[3.Debug模块使用说明](#Debug)

[4.Color模块使用说明](#Color)

[5.Update log](#Update)

## 安装流程 <a id="Install"></a>

使用pip进行安装

```python
  pip install yliueTools
```

## Debug模块使用说明 <a id="Debug"></a>

### 注意

Debug包会调用Color包的函数，Color的**颜色显示**在**不支持ANSI转义序列**的终端会出现**乱码**的情况
你可以通过关闭颜色来让其正常显示

```python
 debug = Debug("Test", _color=False)
```

### 初步使用

1.引入该包

```python
 from MxTools import Debug
```

2.定义一个Debug对象

```python
 # debug = Debug('project_name') 
 # project_name 为项目名称 type:str
 debug = Debug('Test')
```

3.使用Debug模块打印信息

```python
 debug.log('Hello World!')
 # 输出
 # [2025-09-21 16:01:47,299] ING Test.default: Hello World!
```

### 筛选器教程

 使用log打印时有3个参数
 分别是 **_msg**(打印信息) **_name**(信息打印位置,默认为default) **_type**(类型，默认为ING)

 我们可以在定义类的时候使用 **_filterTyp** 和 **_filterName** 筛选器筛选自己想看的信息

 ```python
  debug = Debug('Test',_filterType = 'ING', _filterName = 'default')
  # 筛选出类型为ING 发出位置为 default的打印信息
 ```

### 关闭Debug输出

```python
  debug = Debug('Test', False)
```

### API

#### Debug类

```python
  Debug(_project: str, _debug: bool = True, _filterType: str = 'all', _filterName: str = 'all',_tips: bool = True, _color: bool = True)
```

- _project 项目名称,必填项
- _debug debug的开关,可以一键关闭所有输出
- _filterType 类型筛选器
- _filterName 发出位置筛选器
- _tips 提示显示的开关
- _color  可以关闭输出的字体颜色

#### .log

```python
  .log(_msg, _name: str = 'default', _type: str = 'ING')
```

- _msg 信息
- _name 信息发出位置
- _type 信息类型,已有参数会有颜色标识

##### _type已有参数

- ING 正常运行
- ERR 错误
- PRIVATE 属于Debug内部信息
- TIPS  提示信息,可以在定义类的时候使用 **_tips = False** 来关闭所有的提示信息
- GLOBAL  全局变量
- OUTPUT  接口输出

## Color模块使用说明<a id="Color"></a>

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

## Update log <a id="Update"></a>

`Ver1.0.1 2025.09.21` 第一次上传

`Ver1.0.2 2025.09.22` 修改部分编写错误 debug.rEnd修复了文件夹读取与实际不符合的bug,不要使用没提到的功能,即便它有,这极其不稳定

`Ver1.0.3 2025.09.22` 修改了自叙文件的编写错误

`Ver1.0.4 2025.09.22` 修复Debug筛选器筛选问题,加入了屏蔽提示的开关,更好的自叙文件

筛选器Bug...这个真是核心的问题,都是因为自己不够小心,Orz不好意思qaq,幸好没人用