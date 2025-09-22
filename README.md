# yLIueTools

yLIueTools包含自己正在使用的一些python小工具

当前版本: 1.0.3

代码最新更新时间: 2025.09.22

若自叙文件文件出现错误,可以去github看看是否更正,pypi只会随代码更新

[yLIueTools](https://github.com/yLIue/yLIueTools)

## 描述 <a id="description"></a>

每一个代码萌新都会自己尝试造轮子,这是我自己尝试写的方便自己用的小工具

可能有些功能会跟其他包冲突了,主要还是自己方便嘛

该包包含内容:

- 方便调试和筛选输出信息的Debug模块
- 方便输出带有颜色字体的Color模块

## 目录

[1.描述](#description)

[2.Debug模块使用说明](#Debug)

[3.Color模块使用说明](#Color)

[4.Update log](#Update)

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

### 过滤器教程

 使用log打印时有3个参数
 分别是 **_msg**(打印信息) **_name**(信息打印位置,默认为default) **_type**(类型，默认为ING)

 我们可以在定义类的时候使用 **_filterTyp** 和 **_filterName** 过滤器筛选自己想看的信息

 ```python
 debug = Debug('Test',_filterType = 'ING', _filterName = 'default')
 # 筛选出类型为ING 发出位置为 default的打印消息
 ```

### 关闭Debug输出

  ```python
 debug = Debug('Test', False)
 ```

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