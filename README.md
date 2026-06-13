# 🌤️ 天气查询小工具

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Level](https://img.shields.io/badge/练习-初学者-blue?style=flat-square)

</div>

一个用 Python 写的实时天气查询工具，输入城市名即可查看天气，无需注册或 API Key。

## ✨ 功能

- 🌤️ 实时天气查询
- 🌡️ 温度、湿度、风速等信息
- 🔍 支持中英文城市名
- 🚀 无需 API Key

## 🚀 快速开始

### 依赖
```bash
无额外依赖（使用 wttr.in 免费 API）
```

### 运行
```bash
python weather.py
```

## 📖 使用说明

运行后输入城市名（如 `深圳` 或 `shenzhen`），回车查看天气。输入 `quit` 退出。

## 🛠️ 用到的知识点

| 知识点 | 应用 |
|--------|------|
| 网络请求 | urllib 调用天气 API |
| JSON 数据解析 | 解析返回数据 |
| 异常处理 | 处理网络错误 |
| 字符串格式化 | 美化输出 |
| 用户交互循环 | 持续查询 |

## 📷 运行效果

> 欢迎添加运行截图 Pull Request 😊

## 📝 后续可以增强

- [ ] 查询未来几天的天气预报
- [ ] 保存查询历史
- [ ] 多城市对比
- [ ] 图形界面版本

## ❓ 常见问题

暂无

## 📄 License

MIT License
