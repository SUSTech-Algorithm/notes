# Robocon 新生培训 - Ubuntu & IDE 使用指南

## 📋 培训大纲 (约1小时)

| 时间段 | 内容 | 时长 |
|--------|------|------|
| 0-15分钟 | Ubuntu 22.04/24.04 基础介绍 | 15分钟 |
| 15-35分钟 | Ubuntu 系统操作与开发环境配置 | 20分钟 |
| 35-50分钟 | IDE 介绍与配置 (VSCode, Cursor, Claude Code) | 15分钟 |
| 50-60分钟 | 实践操作与答疑 | 10分钟 |

---

## 🐧 Ubuntu 22.04/24.04 基础介绍


### 5. 常用快捷键
- `Ctrl + Alt + T`: 打开终端
- `Ctrl + C`: 中断当前命令
- `Ctrl + D`: 退出终端
- `Tab`: 自动补全
- `Ctrl + L`: 清屏


### 什么是 Ubuntu？
- **Ubuntu** 是基于 Debian 的 Linux 发行版
- 开源、免费、安全稳定
- 广泛应用于服务器、桌面和嵌入式开发
- 适合机器人开发和学习

### Ubuntu 22.04 LTS vs 24.04 LTS
| 特性 | Ubuntu 22.04 LTS | Ubuntu 24.04 LTS |
|------|------------------|------------------|
| 发布时间 | 2022年4月 | 2024年4月 |
| 支持周期 | 5年 (至2027年) | 5年 (至2029年) |
| 内核版本 | 5.15 | 6.8 |
| 推荐用途 | 稳定开发环境 | 最新特性体验 |

### 系统要求
- **CPU**: 2 GHz 双核处理器
- **内存**: 4 GB RAM (推荐 8 GB)
- **存储**: 25 GB 可用空间
- **显卡**: 支持 1024×768 分辨率

---

## 🛠️ Ubuntu 系统操作与开发环境配置

### 2. APT 包管理器详解

#### 什么是 APT？
- **APT** (Advanced Package Tool) 是 Ubuntu 的包管理系统
- 负责软件包的安装、更新、卸载和依赖管理
- 从软件源 (repository) 下载和安装软件

#### 基础 APT 命令
```bash
# 更新软件包列表 (从软件源获取最新信息)
sudo apt update

# 升级已安装的软件包
sudo apt upgrade

# 安装软件包
sudo apt install package_name


# 卸载软件包 (保留配置文件)
sudo apt remove package_name

# 完全卸载软件包 (包括配置文件)
sudo apt purge package_name

# 清理不需要的包
sudo apt autoremove   ## 慎用！！慎用！！
```

#### 软件源配置

##### 什么是软件源？
软件源是存储软件包的服务器，Ubuntu 默认使用官方源，但有时需要更换为国内镜像源以提高下载速度。

##### 查看当前软件源
```bash
# 查看软件源配置文件
cat /etc/apt/sources.list
```

##### 更换为国内镜像源 (推荐)

```bash
# 备份原始配置
sudo cp /etc/apt/sources.list /etc/apt/sources.list.backup

# 编辑软件源配置
sudo nano /etc/apt/sources.list
```

##### 常用国内镜像源

**清华大学镜像源 (推荐)**
```bash
# 替换 /etc/apt/sources.list 内容
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
```

**阿里云镜像源**
```bash
deb https://mirrors.aliyun.com/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.aliyun.com/ubuntu/ jammy-security main restricted universe multiverse
```

**中科大镜像源**
```bash
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
deb https://mirrors.ustc.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
```

##### 更换镜像源后的操作
```bash
# 更新软件包列表
sudo apt update

# 升级系统
sudo apt upgrade
```

### 4. Shell 配置文件 (.bashrc 和 .zshrc)

#### 什么是 Shell 配置文件？
**Shell 配置文件是每次打开终端时自动执行的脚本，用于：**
- 设置环境变量
- 定义别名 (alias)
- 配置命令提示符
- 加载自定义函数

#### .bashrc (Bash Shell 配置)
```bash
# 查看当前 .bashrc 文件
cat ~/.bashrc

# 编辑 .bashrc 文件
nano ~/.bashrc
# 或使用其他编辑器
code ~/.bashrc  # VSCode
```

### 1. 基础终端操作

```bash
# 查看当前目录
pwd

# 列出文件和目录
ls 
ls -a

# 切换目录
cd /path/to/directory
cd ~  # 回到用户主目录
cd .. # 回到上级目录

# 创建目录
mkdir project_name

# 创建文件
touch filename.txt

# 复制文件
cp source.txt destination.txt

# 移动/重命名文件
mv old_name.txt new_name.txt

# 删除文件
rm filename.txt
rm -rf directory_name  # 删除目录及其内容
```

---

## 💻 IDE 介绍与配置
### 什么是 IDE？

**IDE**（集成开发环境，Integrated Development Environment）是一种为程序员提供综合开发工具的软件应用。它通常集成了代码编辑器、编译器/解释器、调试器和图形化界面，帮助开发者更高效地编写、调试和管理代码。

主要功能包括：
- 代码高亮和自动补全
- 语法检查和错误提示
- 一键编译/运行
- 调试工具（断点、单步执行等）
- 项目和文件管理
- 插件扩展支持

常见的 IDE 有 Visual Studio Code（简称VSCode）、PyCharm、CLion、Eclipse、Cursor、Claude code 等。对于初学者，推荐使用 `VSCode`，界面友好、插件丰富，适合多种编程语言和开发场景。


### 1. Visual Studio Code (VSCode)
#### VSCode 简介

Visual Studio Code（简称 VSCode）是由微软开发的一款免费、开源、跨平台的轻量级代码编辑器。它支持 Windows、macOS 和 Linux 系统，拥有丰富的插件生态，适用于多种编程语言（如 C/C++、Python、JavaScript、ROS 等）。VSCode 提供了强大的代码补全、调试、Git 集成、远程开发等功能，界面简洁，易于上手，非常适合初学者和专业开发者使用。

主要特点：
- 跨平台：支持主流操作系统
- 插件丰富：可通过扩展市场安装各种开发工具
- 代码高亮与智能补全
- 内置终端和调试工具
- 良好的 Git 集成
- 支持远程开发（如 Remote-SSH）

#### 安装 VSCode
```bash

# 下载 .deb 包安装
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
sudo apt update
sudo apt install code
```

#### 推荐扩展
- **C/C++**: Microsoft C/C++ 扩展包
- **Python**: Python 扩展包
- **GitLens**: Git 增强工具
- **Remote - SSH**: 远程开发
- **ROS**: ROS 开发支持
- **Chinese (Simplified)**: 中文语言包

## 📚 学习资源

### 官方文档
- [Ubuntu 官方文档](https://ubuntu.com/tutorials)
- [VSCode 官方文档](https://code.visualstudio.com/docs)

### 推荐教程
- [Linux 命令行基础](https://www.learnenough.com/command-line-tutorial)


---

## ❓ 常见问题解答

### Q: Ubuntu 和 Windows 有什么区别？
A: Ubuntu 是 Linux 系统，开源免费，命令行强大，适合开发；Windows 是商业系统，图形界面友好，软件生态丰富。

### Q: 如何选择 Ubuntu 版本？
A: 推荐使用 LTS 版本（长期支持），22.04 更稳定，24.04 有最新特性。

### Q: VSCode 和 Cursor 哪个更好？
A: VSCode 功能全面，插件丰富；Cursor 集成 AI 助手，适合快速开发。建议都尝试。

### Q: 如何解决权限问题？
A: 使用 `sudo` 命令获取管理员权限，但要注意安全性。

### Q: .bashrc 和 .zshrc 有什么区别？
A: .bashrc 是 Bash shell 的配置文件，.zshrc 是 Zsh shell 的配置文件。Zsh 功能更强大，支持更好的自动补全和主题。

### Q: 如何让配置文件修改立即生效？
A: 使用 `source ~/.bashrc` 或 `source ~/.zshrc` 命令重新加载配置文件。

### Q: 软件下载速度很慢怎么办？
A: 更换为国内镜像源，推荐使用清华大学镜像源，可以显著提高下载速度。

### Q: 如何选择合适的镜像源？
A: 选择距离你最近的镜像源，国内推荐清华、阿里云或中科大镜像源。

### Q: 添加软件源后出现错误怎么办？
A: 检查软件源地址是否正确，确保网络连接正常，必要时恢复备份的配置文件。

---

## 🎯 培训总结

通过本次培训，你应该掌握：
- ✅ Ubuntu 基础操作和命令
- ✅ 开发环境配置
- ✅ IDE 选择和配置
- ✅ 项目创建和管理

### 下一步学习建议
1. 深入学习 Linux 命令行
3. 学习 C++/Python 编程
5. 实践项目开发

---

*最后更新: 2024年*
*培训时长: 约1小时*
*适合人群: Robocon 新生*
