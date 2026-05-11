# NAS部署指南

## 通用Docker部署（适用于所有NAS）

### 1. 准备工作

确保NAS已安装:
- Docker
- Docker Compose (推荐)

### 2. 部署步骤

```bash
# 克隆项目
git clone https://github.com/daveton/clipdown.git
cd clipdown

# 创建下载目录
mkdir -p download

# 启动服务
docker-compose up -d
```

### 3. 访问服务

打开浏览器访问: `http://your-nas-ip:8080`

### 4. 配置Cookie（重要）

1. 在电脑浏览器中登录抖音网站
2. 按F12打开开发者工具
3. 找到Cookie并复制
4. 编辑 `config.yaml`，更新Cookie配置
5. 重启容器: `docker-compose restart`

## 群晖NAS部署

### 使用Container Manager

1. 打开Container Manager
2. 选择"项目" → "新建"
3. 设置项目名称: `clipdown`
4. 选择项目路径并上传docker-compose.yml
5. 点击"下一步"完成部署

### 端口设置

- 容器端口: 80
- 本地端口: 8080（可自定义）

### 卷设置

| 容器路径 | 本地路径 | 说明 |
|---------|---------|------|
| /app/config.yaml | ./config.yaml | 配置文件 |
| /app/download | ./download | 下载目录 |
| /app/logo | ./logo | Logo文件 |

## 威联通NAS部署

### 使用Container Station

1. 打开Container Station
2. 创建应用程序
3. 粘贴docker-compose.yml内容
4. 设置网络端口映射
5. 部署应用

## 常用命令

```bash
# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down

# 重启服务
docker-compose restart

# 更新镜像
docker-compose pull
docker-compose up -d
```

## 故障排查

### 端口冲突
修改 `docker-compose.yml` 中的端口映射:
```yaml
ports:
  - "8081:80"  # 改为其他端口
```

### 权限问题
确保下载目录有写入权限:
```bash
chmod 755 ./download
```

### 网络问题
如果无法访问，检查防火墙设置，确保端口已开放。
