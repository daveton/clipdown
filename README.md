<div align="center">
<img src="./logo/logo192.png" width="120" alt="ClipDown Logo"/>
</div>

<h1 align="center">ClipDown</h1>

<p align="center">
  <b>适用于NAS的视频下载工具</b><br>
  支持抖音 / TikTok / Bilibili 无水印下载<br>
  <a href="./docs/README.en.md">English</a>
</p>

<p align="center">
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/daveton/clipdown?style=flat-square" alt="License"/>
  </a>
</p>

---

## 功能特点

- 抖音无水印视频/图集下载
- TikTok无水印视频下载  
- Bilibili视频下载
- Web界面批量解析
- RESTful API接口
- 适合NAS本地部署

## 快速开始

### Docker部署（推荐）

```bash
# 克隆项目
git clone https://github.com/daveton/clipdown.git
cd clipdown

# 启动服务
docker-compose up -d

# 访问 http://localhost:8080
```

### 手动部署

```bash
# 安装依赖
pip install -r requirements.txt

# 启动服务
python start.py
```

## 配置说明

编辑 `config.yaml`：

```yaml
Web:
  Domain: http://your-nas-ip:8080
  Tab_Title: ClipDown
  
API:
  Host_Port: 80
```

## 重要提示

- 本项目仅供学习交流使用
- 部署后需要在浏览器中获取抖音Cookie并替换到配置文件中
- 请遵守各平台的使用条款


## 文档

- 文档导航：[`docs/README.md`](./docs/README.md)
- NAS 部署：[`docs/NAS_DEPLOY.md`](./docs/NAS_DEPLOY.md)
- English README：[`docs/README.en.md`](./docs/README.en.md)

## 技术栈

- Web界面: [PyWebIO](https://www.pyweb.io/)
- API服务: [FastAPI](https://fastapi.tiangolo.com/)
- 数据爬取: [HTTPX](https://www.python-httpx.org/)

## 开源协议

基于 [Apache-2.0](LICENSE) 协议开源

原始项目: [Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API)
