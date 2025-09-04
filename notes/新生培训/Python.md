# Python 开发全方位指南
## 目录
1. [Conda 全方位介绍](#conda-全方位介绍)
   - [一、什么是Conda？](#一什么是conda)
   - [二、为什么我们要用Conda？](#二为什么我们要用conda)
   - [三、如何在Linux上安装Conda？](#三如何在linux上安装conda)
   - [四、Conda的常用命令](#四conda的常用命令)
2. [Python 基础教程](#python-基础教程)
   - [一、变量与数据类型](#一变量与数据类型)
   - [二、循环与判断](#二循环与判断)
   - [三、列表、字典与元组](#三列表字典与元组)
   - [四、函数](#四函数)
   - [五、import 语句（模块导入）](#五import-语句模块导入)
   - [六、PYTHONPATH 环境变量](#六pythonpath-环境变量)
3. [Python 面向对象编程（OOP）教程](#python-面向对象编程oop教程)
   - [一、类与对象的基本概念](#一类与对象的基本概念)
   - [二、类的定义与对象的创建](#二类的定义与对象的创建)
   - [三、类的方法](#三类的方法)


## :star: Conda 全方位介绍
###  一、什么是Conda？
Conda 是一个开源的**包管理和环境管理工具**，最初是为 Python 语言开发的，但现在已支持多种编程语言（如 R、C++、Java 等）。它由 Anaconda, Inc.（前身为 Continuum Analytics）开发维护，核心功能涵盖了包的查找、安装、更新、卸载，以及独立开发环境的创建、切换和删除。

简单来说，Conda 就像一个“全能管家”：一方面，它能帮你统一管理不同开发所需的软件包，解决包之间的依赖冲突问题；另一方面，它能为每个项目创建独立的“隔离空间”（即环境），让不同项目的配置互不干扰——比如一个项目需要 Python 3.8 版本，另一个项目需要 Python 3.11 版本，通过 Conda 就能轻松实现切换，无需反复卸载安装。


### 二、为什么我们要用Conda？
在开发过程中，手动管理包和环境往往会遇到各种麻烦，而 Conda 恰好能解决这些核心痛点，具体优势如下：

#### 1. 解决“包依赖地狱”问题
很多开发工具或库（即“包”）需要依赖其他特定版本的包才能运行，手动安装时很容易出现“版本不兼容”“依赖缺失”等问题。Conda 会在安装包时**自动分析并安装其所需的依赖包**，并确保所有依赖的版本相互匹配，极大减少手动调试的时间。

#### 2. 实现环境隔离，避免项目冲突
不同项目的配置需求可能差异很大：比如 A 项目需要 TensorFlow 1.x，B 项目需要 TensorFlow 2.x；或者 C 项目需要 Python 2.7（旧项目维护），D 项目需要 Python 3.10。如果共用一个环境，这些配置会相互干扰甚至导致项目报错。  
Conda 可以为每个项目创建独立环境，每个环境的包和 Python 版本都是独立的，切换环境即可无缝切换开发配置。

### 三、如何在Linux上安装Conda？
Linux 上的 Conda 主要有两个版本：**Anaconda**（包含 Python 解释器、常用包及管理工具，体积较大）和 **Miniconda**（仅包含 Conda 核心功能和 Python 解释器，体积小，可按需安装包）。推荐优先选择 Miniconda，更轻量灵活。

以下是 Miniconda 的详细安装步骤：

#### 1. 确认Linux系统架构
首先通过终端命令确认系统是 32 位还是 64 位（目前主流为 64 位）：
```bash
uname -m
```
- 若输出 `x86_64`，则为 64 位系统；
- 若输出 `i386`/`i686`，则为 32 位系统。


#### 2. 获取Miniconda安装脚本
https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

#### 3. 运行安装脚本
进入项目目录后，通过 `bash` 命令执行安装脚本：
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

执行后会进入安装流程，按以下步骤操作：
1. **查看许可协议**：按 `Enter` 键开始查看，持续按 `Space` 键翻页，直到出现 “Do you accept the license terms? [yes|no]”；
2. **同意协议**：输入 `yes` 并按 `Enter`；
3. **选择安装路径**：默认路径为 `/home/用户名/miniconda3`，可直接按 `Enter` 确认，也可输入自定义路径（如 `/opt/miniconda3`）；
4. **是否初始化Conda**：出现 “Do you wish the installer to initialize Miniconda3 by running conda init?” 时，输入 `yes` 并按 `Enter`（初始化后可直接在终端使用 `conda` 命令）。


#### 4. 验证安装是否成功
安装完成后，关闭当前终端并重新打开（让环境变量生效），输入以下命令查看 Conda 版本：
```bash
conda --version
```
若输出类似 `conda 24.x.x` 的版本信息，则说明安装成功。


#### 5. （可选）配置国内镜像源（加速包下载）
由于 Conda 官方仓库在国外，国内下载包可能较慢，可配置国内镜像源（如清华源、中科大源）。以配置清华源为例，在终端执行以下命令：
```bash
# 添加清华源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
```


### 四、Conda的常用命令
以下是一些常用的 Conda 命令及其功能说明：

1. **查看已安装的 Conda 版本**：
    ```bash
    conda --version
    ```

2. **更新 Conda 到最新版本**：
    ```bash
    conda update conda
    ```

3. **创建新环境**：
    ```bash
    conda create --n 环境名 python=版本号
    ```
    示例：创建一个 Python 3.9 的环境：
    ```bash
    conda create --n myenv python=3.9
    ```

4. **激活环境**：
    ```bash
    conda activate 环境名
    ```

5. **退出当前环境**：
    ```bash
    conda deactivate
    ```

6. **列出所有环境**：
    ```bash
    conda env list
    ```

7. **安装包到当前环境**：
    ```bash
    conda install 包名
    ```
    示例：安装 NumPy：
    ```bash
    conda install numpy
    ```

8. **更新包到最新版本**：
    ```bash
    conda update 包名
    ```

9. **卸载包**：
    ```bash
    conda remove 包名
    ```

11. **删除环境**：
     ```bash
     conda remove --name 环境名 --all
     ```


## :tent: Python 基础教程
### 一、变量与数据类型

#### 1. 变量定义
变量是存储数据的容器，无需声明类型，直接赋值即可：
```python
name = "Alice"  # 字符串
age = 25        # 整数
height = 1.65   # 浮点数
is_student = True  # 布尔值
```

#### 2. 基本数据类型
- **整数(int)**: 没有小数部分的数字，如 `42`、`-7`
- **浮点数(float)**: 带小数的数字，如 `3.14`、`-0.5`
- **字符串(str)**: 文本数据，用单引号或双引号包裹，如 `"hello"`、`'python'`
- **布尔值(bool)**: 只有 `True`（真）和 `False`（假）两个值
- **NoneType**: 表示空值，只有 `None` 一个值
$$注释$$
```python
# 查看变量类型
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
```
### 二、列表、字典与元组
$$要讲索引逻辑$$
#### 1. 列表（List）
有序、可变的元素集合，用 `[]` 表示，
```python
# 定义列表
numbers = [1, 2, 3, 4, 5]
names = ["张三", "李四", "王五"]

# 访问元素（索引从0开始）向前从0开始，向后从-1开始
print(numbers[0])  # 1
print(names[-1])    # 王五

# 切片操作
print(numbers[1:3])  # [2, 3]（获取索引1到2的元素）
print(numbers[:3])   # [1, 2, 3]（从开头到索引2）

# 常用操作
numbers.append(6)    # 添加元素到末尾
numbers.remove(3)    # 删除指定元素
print(len(numbers))  # 获取长度
```

#### 2. 字典（Dictionary）
键值对集合，无序（Python 3.7+ 有序），用 `{}` 表示
```python
# 定义字典
person = {
    "name": "张三",
    "age": 20,
    "is_student": True
}

# 访问值
print(person["name"])  # 张三
print(person.get("age"))  # 20（更安全的访问方式）

# 修改和添加
person["age"] = 21  # 修改值
person["gender"] = "男"  # 添加新键值对

# 遍历字典
for key in person:
    print(f"{key}: {person[key]}")
```

#### 3. 元组（Tuple）
有序、不可变的元素集合，用 `()` 表示
```python
# 定义元组
point = (3, 4)
info = ("Alice", 25, "female")

# 访问元素
print(point[0])  # 3

# 元组不可修改（以下代码会报错）
# point[0] = 5

# 拆包
x, y = point
print(x, y)  # 3 4
```


### 三、循环与判断

#### 1. 条件判断（if-elif-else）
```python
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

#### 2. 循环结构
##### （1）for循环（遍历序列）
```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)

# 遍历范围
for i in range(5):  # 0-4
    print(i)

for i in range(2, 6):  # 2-5
    print(i)
```

##### （2）while循环（条件循环）
```python
count = 0
while count < 3:
    print(f"计数: {count}")
    count += 1  # 等价于 count = count + 1
```

##### （3）循环控制
- `break`: 终止循环
- `continue`: 跳过当前循环，进入下一次
- `pass`: 用来帮助实现思维

```python
for i in range(10):
    if i == 5:
        break  # 当i=5时终止循环
    print(i)
```


### 四、函数

#### 1. 函数定义与调用
用 `def` 关键字定义函数
```python
# 定义函数
def greet(name):
    """向指定名字的人打招呼"""  # 文档字符串
    return f"你好，{name}！"

# 调用函数
message = greet("张三")
print(message)  # 你好，张三！
```

#### 2. 带默认参数的函数
```python
def add(a, b=10):  # b的默认值为10
    return a + b

print(add(5))    # 15（使用默认参数b=10）
print(add(5, 3)) # 8（覆盖默认参数）
```


### 五、import 语句（模块导入）

目前python之所以常用不仅是因为其简单的语法逻辑与规则，还有是其简单成熟的包调用
在 Python 中，`import` 语句用于导入其他模块（.py 文件）中的代码，实现代码复用。模块可以是 Python 标准库、第三方库或自定义脚本。

#### 1. 基本导入方式
```python
# 导入整个模块
import math  # 导入标准数学模块
print(math.sqrt(16))  # 使用模块中的函数（模块名.函数名）

# 导入模块并指定别名
import numpy as np  # 为模块指定简短别名
print(np.array([1, 2, 3]))  # 通过别名使用模块

# 导入模块中的所有成员（不推荐，可能导致命名冲突）
from datetime import *
print(datetime.now())  # 直接使用datetime类
```

#### 2. 导入自定义模块
如果有一个自定义文件 `my_module.py`：
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"
```

可以在同一目录下的其他文件中导入：
```python
from my_module import greet
print(greet("Python"))  # 输出：Hello, Python!
```

### 六、PYTHONPATH 环境变量

`PYTHONPATH` 是 Python 解释器用于查找模块的路径列表。当使用 `import` 语句时，Python 会在这些路径中搜索对应的模块。

在linux中这就属于我们说的**环境变量**中的一种
#### 1. 查看当前 PYTHONPATH
```bash
# 在终端中使用以下命令查看当前 PYTHONPATH：
echo $PYTHONPATH
```

#### 2. 临时添加路径 

```bash
export PYTHONPATH="/home/user/my_python_scripts:$PYTHONPATH"
```

#### 3. 永久设置 PYTHONPATH（终端）
##### Linux/Mac 系统：
在 `.bashrc` 或 `.zshrc` 中添加：
``` .bashrc
export PYTHONPATH="/home/user/my_python_scripts:$PYTHONPATH"
```
生效命令：
```bash
source ~/.bashrc  # 或 source ~/.zshrc
```

#### 4. 作用
- 解决「ModuleNotFoundError」：当模块不在默认搜索路径时，通过添加路径让 Python 找到模块
- 方便管理自定义模块：将常用脚本放在固定目录并添加到 `PYTHONPATH`，可在任何地方导入使用


## :fire: Python 面向对象编程（OOP）教程
面向对象编程（Object-Oriented Programming，简称OOP）是一种编程范式，它将数据和操作数据的方法封装在一起，通过类和对象来组织代码，提高代码的复用性、可维护性和扩展性。

### 一、类与对象的基本概念

#### 1. 什么是类（Class）？
类是对现实世界中某一类事物的抽象描述，它定义了这类事物共有的**属性**（数据）和**方法**（操作）。

例如："人类"可以作为一个类，共有的属性包括姓名、年龄、性别，共有的方法包括走路、说话等。

#### 2. 什么是对象（Object）？
对象是类的具体实例，是实际存在的个体。一个类可以创建多个对象。

例如："张三"是"人类"这个类的一个对象，"李四"是另一个对象。

### 二、类的定义与对象的创建

#### 1. 定义类
使用 `class` 关键字定义类，语法如下：
```python
class 类名:
    # 类的属性和方法
    def __init__(self):
        pass
    def functions(self, a, b):
        pass

```

#### 2. 初始化方法（`__init__`）
`__init__` 方法是类的构造方法，用于初始化对象的属性，在创建对象时自动调用。
```python
class Person:
    # 初始化方法，self 表示当前对象本身
    def __init__(self, name, age):
        # 定义属性
        self.name = name  # 姓名属性
        self.age = age    # 年龄属性
    def show_age(self):
        print(self.age)
        print(self.name)

```


#### 3. 创建对象
通过 `类名(参数)` 方式创建对象（实例化）：
```python
# 创建 Person 类的对象
person1 = Person("张三", 20)
person2 = Person("李四", 25)

# 访问对象的属性
print(person1.name)  # 输出：张三
print(person2.age)   # 输出：25
person.show_age()    # 输出：25
                     #      张三
```

### 三、类的方法

方法是定义在类中的函数，用于描述对象的行为。方法的第一个参数必须是 `self`，表示当前对象。

#### 1. 实例方法
实例方法是最常用的方法类型，只能通过对象调用。
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 定义实例方法：说话
    def speak(self):
        print(f"我叫{self.name}，今年{self.age}岁")
    
    # 定义实例方法：过生日（修改年龄）
    def birthday(self):
        self.age += 1
        print(f"生日快乐！{self.name}现在{self.age}岁了")

# 使用方法
p = Person("王五", 30)
p.speak()       # 输出：我叫王五，今年30岁
p.birthday()    # 输出：生日快乐！王五现在31岁了
```

## :question: 项目练习：
**写一个储存了四则运算的函数的文件，并在另一个文件中导入使用它**