<div align="center">
<img src="./logo/logo192.png" width="120" alt="ClipDown Logo"/>
</div>

<h1 align="center">ClipDown</h1>

<p align="center">
  <b>Video Download Tool for NAS</b><br>
  Support Douyin / TikTok / Bilibili watermark-free download
</p>

<p align="center">
  <a href="./LICENSE">
    <img src="https://img.shields.io/github/license/daveton/clipdown?style=flat-square" alt="License"/>
  </a>
</p>

---

## Features

- Douyin watermark-free video/images download
- TikTok watermark-free video download
- Bilibili video download
- Web UI batch parsing
- RESTful API endpoints
- Designed for NAS local deployment

## Quick Start

### Docker Deployment (Recommended)

```bash
# Clone repository
git clone https://github.com/daveton/clipdown.git
cd clipdown

# Start service
docker-compose up -d

# Access http://localhost:8080
```

### Manual Deployment

```bash
# Install dependencies
pip install -r requirements.txt

# Start service
python start.py
```

## Configuration

Edit `config.yaml`:

```yaml
Web:
  Domain: http://your-nas-ip:8080
  Tab_Title: ClipDown
  
API:
  Host_Port: 80
```

## Important Notes

- This project is for educational purposes only
- After deployment, you need to obtain Douyin cookies from browser and update the config file
- Please comply with the terms of service of each platform

## Tech Stack

- Web UI: [PyWebIO](https://www.pyweb.io/)
- API Service: [FastAPI](https://fastapi.tiangolo.com/)
- Data Crawling: [HTTPX](https://www.python-httpx.org/)

## License

Open source under [Apache-2.0](LICENSE)

Original project: [Douyin_TikTok_Download_API](https://github.com/Evil0ctal/Douyin_TikTok_Download_API)
