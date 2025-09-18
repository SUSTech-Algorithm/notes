
# Robocon 新生 ROS 2 入门培训大纲

-----

### :smile: 第一部分：准备工作 —— 安装 ROS 2 (15 分钟)*

欢迎来到 Robocon！为了让你的机器人“活”起来，我们首先要为它的大脑安装一个框架——ROS 2。

ROS 2 的安装过程对新手可能有些挑战，但别担心，我们有专门的国内镜像源，可以让你一键搞定！

#### 1\. 使用“鱼香ROS”国内镜像

“鱼香ROS”是国内一个非常好用的 ROS 社区，他们提供了一键安装脚本，可以自动帮你配置好 ROS 2 的环境。

**请在你的 Ubuntu 终端中，依次执行以下命令：**

1.  下载并运行安装脚本：
    ```bash
    wget http://fishros.com/install -O fishros && bash fishros
    ```
2.  按照提示操作：
      * 在终端中输入数字 **2**，选择 **“一键安装 ROS2 操作系统”**。
      * 根据你的 Ubuntu 版本，选择对应的 ROS 2 版本。**如果你使用的是 Ubuntu 22.04，请选择 Humble 版本。** **如果是Ubuntu 24.04，请选择jazzy**
      * 脚本会自动帮你完成所有安装和配置，耐心等待即可。

#### 2\. 验证安装

安装完成后，打开一个新的终端，输入以下命令：

```bash
ros2
```

如果终端显示 ROS 2 的使用说明，而不是报错信息，就说明你已经成功安装啦！

-----

### :question: 第二部分：什么是 ROS 2？ (10 分钟)
**Ros2 是款功能强大的机器人框架，用来实现机器人多模块之间的交互与通信**

  * **核心比喻**：把 ROS 2 想象成一个专为机器人设计的 **“城市”**。
      * **你的代码**：城市里的各种“建筑”，比如“避障大楼”、“抓取工厂”等。这些在ros2中就叫**节点**
      * **ROS 2**：管理这个城市的“城市管理者”，它提供道路、电力、通信网络等基础设施，让所有建筑互相沟通，协调，从而高效的实现各种工作。

它能让你专注于盖自己的“建筑”（写代码），而不用去担心修路、拉电线这些复杂的基础工作。

有些熟悉python的同学可能会问，python本身不是可以实现包的调用吗，这不是也是一种类似的通信吗，那为什么还要使用ros2。
**实际上ros2不仅可是实现一台电脑内的通信他还可以实现电脑之间的通信，因为实际的机器人上中可能有多个开发板，或者树梅派这种小型运算单元，ros2可以实现这些模块之间的通信**
**不仅如此他还可是实现不同计算机语言之间的程序通信与兼容，用C/C++的导航避障功能可以，和用python写的视觉定位互相通信**

-----

### :tent: 第三部分：城市里的核心构件 (20 分钟)

这一部分是课程的重点，尽量用最生动的语言解释 ROS 2 的基本组成部分。**我们这次讲解也是带大家入门，详细系统的学习还是得要大家看文档学习或者看网上的视频**

  * **节点 (Node)**：

      * **比喻**：城市里的每个独立的\*\*“小公司”\*\*。
      * **解释**：每个节点都是一个独立的、可执行的程序，比如一个处理摄像头画面的程序，或者一个控制马达运动的程序。每个节点只做一件事，但可以和其他节点协作。

  * **话题 (Topic) & 消息 (Message)**：

      * **比喻**：城市里的\*\*“广播电台”**和**“广播内容”\*\*。
      * **解释**：话题是数据流动的\*\*“频道”**。一个节点可以**发布\*\*（publish）数据到某个话题，另一个节点可以**订阅**（subscribe）这个话题来接收数据。

![ros2 topic and node](../../resources/ROS2/Nodes-TopicandService.gif)

  * #**服务** (Service)：

      * **比喻**：城市里的\*\*“问答服务台”\*\*。
      * **解释**：服务用于处理一次性的**请求-响应**（Request-Response）模式。客户端向服务端发送请求，服务端处理完后返回结果。

![service](../../resources/ROS2/Service-MultipleServiceClient.gif)

**Services are another method of communication for nodes in the ROS graph. Services are based on a call-and-response model versus the publisher-subscriber model of topics. While topics allow nodes to subscribe to data streams and get continual updates, services only provide data when they are specifically called by a client.** 

  * #****动作** (Action)：

      * **比喻**：城市里的\*\*“快递服务”\*\*。
      * **解释**：动作用于处理需要长时间执行的任务，并且可以提供**实时反馈**和**中途取消**。包括`goal`，`feedback`，`result`是一种闭环控制
---官方文档
![action](../../resources/ROS2/Action-SingleActionClient.gif)

-----

### :laughing: 第四部分：动手实践：创建与运行 ROS 2 包 (10 分钟)

理论讲了这么多，现在我们来亲手创建一个 ROS 2 的项目！

#### 1\. 创建你的工作区 (Workspace)

工作区是所有 ROS 2 项目的“大本营”。首先，创建一个文件夹来存放你的所有项目包。

```bash
mkdir -p ~/robocon_ws/src
cd ~/robocon_ws
```

#### 2\. 创建一个python包

现在，我们来创建一个最简单的 Python 包。
tips：ros2 是可以创建cpp/c的包的，但这里我只演示
```bash
cd src
ros2 pkg create --build-type ament_python my_first_package
```

  * **`my_first_package`**：这是你包的名字。
  * **`--build-type ament_python`**：告诉系统这是一个 Python 包。
  * **`--node-name my_first_node`**：自动帮你创建一个名为 `my_first_node.py` 的节点名。

然后咱们简单写两个节点，一个用来发送字符串消息“hello_world”,到topic“string”，一个用来订阅topic接收消息
`publisher`
```
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyFirstPublisher(Node):
    def __init__(self):
        # 初始化节点
        super().__init__('my_first_publisher')
        self.get_logger().info('MyFirstPublisher node has been initialized')
        # 创建发布者，发布消息到my_first_topic主题
        self.publisher = self.create_publisher(String, 'my_first_topic', 10)
        # 创建定时器，每0.2秒发布一次消息
        self.timer = self.create_timer(0.2, self.publish_message)


    def publish_message(self):
        # 创建消息
        message = String()
        message.data = 'Hello_World!'
        # 发布消息
        self.publisher.publish(message)

def main(args=None):
    rclpy.init(args=args)
    my_first_publisher = MyFirstPublisher()
    rclpy.spin(my_first_publisher)
    my_first_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
**tips： 消息类型**
每种消息都有其专属的消息格式，发送消息相当于是填表格
``` terminal
ros2 interface show geometry_msgs/msg/PoseStamped
```
``` ternnal
# A Pose with reference coordinate frame and timestamp

std_msgs/Header header
        builtin_interfaces/Time stamp
                int32 sec
                uint32 nanosec
        string frame_id
Pose pose
        Point position
                float64 x
                float64 y
                float64 z
        Quaternion orientation
                float64 x 0
                float64 y 0
                float64 z 0
                float64 w 1
```

`subscriber`
```
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MyFirstSubscriber(Node):
    def __init__(self):
        super().__init__('my_first_subscriber')
        self.get_logger().info('MyFirstSubscriber node has been initialized')
        self.subscriber = self.create_subscription(String, 'my_first_topic', self.message_callback, 10)

    def message_callback(self, msg):
        self.get_logger().info('Received message: %s' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    my_first_subscriber = MyFirstSubscriber()
    rclpy.spin(my_first_subscriber)
    my_first_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

`package.xml` 菜单，列出所有需要的依赖

```
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">

  <name>my_first_package</name>
  <version>0.0.0</version>
  <description>TODO: Package description</description>
  <maintainer email="fjienan@example.com">jienan</maintainer>
  <license>TODO: License declaration</license>

  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
  <test_depend>ament_pep257</test_depend>
  <test_depend>python3-pytest</test_depend>

  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
```

`setup.py`
```
from setuptools import find_packages, setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jienan',
    maintainer_email='fjienan@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          #定义节点对应文件 
            'my_first_publisher = my_first_package.publisher:main',
            'my_first_subscriber = my_first_package.subscriber:main',
        ],
    },
)
```
---



#### 4\. 运行你的包

回到工作区根目录，然后编译并运行你的包。

```bash
# 编译你的包，告诉系统你新创建了一个项目
colcon build
source install/setup.bash

# 在新终端中，运行你的节点
ros2 run my_first_package my_first_node
```
$$之后演示一下Posestamp消息的发送效果以及rqt结构$$

恭喜！你已经成功创建并运行了你的第一个 ROS 2 节点！

-----

### :blush: 第五部分：ROS 2 的“瑞士军刀”：rqt 工具 (5 分钟)

  * **rqt 比喻**：把 `rqt` 想象成一个功能强大的\*\*“机器人仪表盘”\*\*。它包含了各种插件，可以让你直观地观察和调试 ROS 2 系统。
      * **`rqt_graph`**：
          * **比喻**：城市的\*\*“交通地图”\*\*。
          * **解释**：它能以图形化的方式展示所有正在运行的节点，以及它们之间通过话题（`Topic`）连接的路径。
      * **`rqt_topic`**：
          * **比喻**：**“电台监听器”**。
          * **解释**：它可以让你实时地看到任何一个话题上正在传输的数据内容，让你能直观地检查数据是否正确。

-----

### :anger: 练习
**写两个节点，一个节点往一个topic /num 中发送一个确定的整数5，另一个节点订阅这个topic并计算这个整数的立方跟，然后将最终结果以log的形式显示在终端中（或者发送到另一个topic /result 中 然后用 topic echo 显示一下）**
**做完一切，你可以用rqt查看一下，看看有没有什么新的收获**
### 总结与展望 (5 分钟)

  * **回顾**：再次强调核心概念：`Node`（小公司），`Topic`（广播电台），`Service`（服务台），`Action`（快递）。
  * **鼓励**：ROS 2 乍一看很复杂，但一旦掌握了这些基础概念，你会发现它是一个非常强大的工具。
  * **行动**：鼓励大家多动手尝试，从简单的例子开始，逐步熟悉 ROS 2 的开发流程。

希望这份大纲能帮助你顺利完成培训！如果你对其中的某个环节需要更详细的讲解，请随时告诉我。


其他参考资料：
**官方教学文档** https://docs.ros.org/en/humble/index.html