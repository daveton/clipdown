# PyWebIO组件/PyWebIO components
import os

import yaml
from pywebio import session, config as pywebio_config
from pywebio.input import *
from pywebio.output import *

from app.web.views.Document import api_document_pop_window
from app.web.views.ParseVideo import parse_video
# PyWebIO的各个视图/Views of PyWebIO
from app.web.views.ViewsUtils import ViewsUtils

# 读取上级再上级目录的配置文件
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as file:
    _config = yaml.safe_load(file)

# 现代深色主题CSS / Modern dark theme CSS
DARK_THEME_CSS = """
<style>
/* 基础重置 / Base reset */
* { margin: 0; padding: 0; box-sizing: border-box; }

/* 深色主题变量 / Dark theme variables */
:root {
    --bg-primary: #070b14;
    --bg-secondary: #0f172a;
    --bg-card: rgba(15, 23, 42, 0.72);
    --border-color: rgba(148, 163, 184, 0.24);
    --text-primary: #e2e8f0;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --accent: #38bdf8;
    --accent-text: #082f49;
}

/* 全局背景 / Global background */
body {
    background: radial-gradient(circle at top, #111827 0%, var(--bg-primary) 45%) !important;
    color: var(--text-primary) !important;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
}

#pywebio-scope-top {
    background-color: var(--bg-primary) !important;
}

/* 头部样式 / Header styles */
.header {
    border: 1px solid var(--border-color);
    border-radius: 18px;
    padding: 0 24px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 900px;
    margin: 20px auto 0;
    background: rgba(15, 23, 42, 0.55);
    backdrop-filter: blur(8px);
}

.header-left {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-container {
    width: 40px;
    height: 40px;
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid var(--border-color);
    background: rgba(255, 255, 255, 0.05);
}

.logo-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.brand-text h1 {
    font-size: 20px;
    font-weight: 600;
    letter-spacing: -0.025em;
    color: var(--text-primary);
    margin: 0;
}

.brand-text p {
    font-size: 12px;
    color: var(--text-muted);
    margin: 0;
}

.header-nav {
    display: flex;
    align-items: center;
    gap: 24px;
}

.header-nav a {
    font-size: 14px;
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.2s;
}

.header-nav a:hover {
    color: var(--text-primary);
}

/* 主内容区 / Main content */
.main-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 56px 24px 80px;
}

.hero-section {
    text-align: center;
    margin-bottom: 48px;
}

.hero-title {
    font-size: 48px;
    font-weight: 700;
    letter-spacing: -0.025em;
    line-height: 1.1;
    color: var(--text-primary);
    margin-bottom: 16px;
}

.hero-title .muted {
    display: block;
    color: var(--text-muted);
    margin-top: 8px;
}

.hero-desc {
    font-size: 16px;
    color: var(--text-secondary);
    max-width: 500px;
    margin: 24px auto 0;
    line-height: 1.6;
}

/* 输入卡片 / Input card */
.input-card {
    border-radius: 24px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    padding: 20px;
    box-shadow: 0 18px 40px -18px rgba(56, 189, 248, 0.55);
}

/* 自定义textarea样式 / Custom textarea */
.custom-textarea {
    width: 100% !important;
    height: 160px !important;
    background: transparent !important;
    border: none !important;
    resize: none !important;
    outline: none !important;
    color: var(--text-primary) !important;
    font-size: 15px !important;
    line-height: 1.5 !important;
    padding: 0 !important;
}

.custom-textarea::placeholder {
    color: #52525b !important;
}

/* 按钮组 / Button group */
.button-group {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 16px;
}

.btn-primary {
    flex: 1;
    height: 48px;
    border-radius: 16px;
    background: var(--accent) !important;
    color: var(--accent-text) !important;
    border: none !important;
    font-weight: 500;
    font-size: 15px;
    cursor: pointer;
    transition: opacity 0.2s;
}

.btn-primary:hover {
    opacity: 0.9;
}

.btn-secondary {
    padding: 0 20px;
    height: 48px;
    border-radius: 16px;
    background: transparent !important;
    color: var(--text-secondary) !important;
    border: 1px solid var(--border-color) !important;
    font-size: 15px;
    cursor: pointer;
    transition: background 0.2s;
}

.btn-secondary:hover {
    background: rgba(255, 255, 255, 0.05) !important;
}

/* API预览卡片 / API preview card */
.api-card {
    margin-top: 40px;
    border-radius: 24px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    overflow: hidden;
}

.api-header {
    padding: 16px 20px;
    border-bottom: 1px solid var(--border-color);
    font-size: 14px;
    color: var(--text-muted);
}

.api-code {
    padding: 20px;
    font-family: 'SF Mono', Monaco, monospace;
    font-size: 14px;
    color: var(--text-secondary);
    line-height: 1.8;
    white-space: pre-wrap;
    overflow-x: auto;
}

/* 页脚 / Footer */
.footer {
    border-top: 1px solid var(--border-color);
    padding: 24px;
    text-align: center;
    font-size: 14px;
    color: var(--text-muted);
}

/* 隐藏PyWebIO默认元素 / Hide PyWebIO default elements */
footer { display: none !important; }

/* 结果区域样式 / Result area styles */
#pywebio-scope-result {
    margin-top: 40px;
}

/* 表格样式覆盖 / Table style overrides */
.table {
    background: var(--bg-card) !important;
    border-radius: 16px !important;
    border: 1px solid var(--border-color) !important;
    overflow: hidden;
}

.table th {
    background: rgba(255, 255, 255, 0.03) !important;
    color: var(--text-secondary) !important;
    border-bottom: 1px solid var(--border-color) !important;
}

.table td {
    color: var(--text-primary) !important;
    border-bottom: 1px solid var(--border-color) !important;
}

/* 提示框样式 / Alert styles */
.alert-success {
    background: rgba(34, 197, 94, 0.1) !important;
    border: 1px solid rgba(34, 197, 94, 0.2) !important;
    color: #22c55e !important;
    border-radius: 12px !important;
}

.alert-warning {
    background: rgba(234, 179, 8, 0.1) !important;
    border: 1px solid rgba(234, 179, 8, 0.2) !important;
    color: #eab308 !important;
    border-radius: 12px !important;
}

.alert-error {
    background: rgba(239, 68, 68, 0.1) !important;
    border: 1px solid rgba(239, 68, 68, 0.2) !important;
    color: #ef4444 !important;
    border-radius: 12px !important;
}

.alert-info {
    background: rgba(59, 130, 246, 0.1) !important;
    border: 1px solid rgba(59, 130, 246, 0.2) !important;
    color: #3b82f6 !important;
    border-radius: 12px !important;
}

/* 链接样式 / Link styles */
a {
    color: #3b82f6 !important;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* 代码块样式 / Code block styles */
pre {
    background: var(--bg-secondary) !important;
    border-radius: 12px !important;
    border: 1px solid var(--border-color) !important;
    color: var(--text-secondary) !important;
}

/* 响应式 / Responsive */
@media (max-width: 768px) {
    .header-nav { display: none; }
    .hero-title { font-size: 36px; }
    .main-container { padding: 40px 16px; }
}
</style>
"""

pywebio_config(theme='dark',
               title=_config['Web']['Tab_Title'],
               description=_config['Web']['Description'])


class MainView:
    BRAND_NAME = "ClipDown"
    BRAND_SUBTITLE = "Video Download API"

    def __init__(self):
        self.utils = ViewsUtils()

    def _inject_head(self, favicon_url: str):
        """Inject global styles and head metadata."""
        session.run_js(f"""
            $('head').append(`{DARK_THEME_CSS}`);
            $('head').append('<link rel="icon" type="image/png" href="{favicon_url}">');
            $('head').append('<meta name="referrer" content="no-referrer">');
        """)

    def _render_header(self, favicon_url: str):
        header_html = f"""
        <div class="header">
            <div class="header-left">
                <div class="logo-container">
                    <img src="{favicon_url}" alt="{self.BRAND_NAME}">
                </div>
                <div class="brand-text">
                    <h1>{self.BRAND_NAME}</h1>
                    <p>{self.BRAND_SUBTITLE}</p>
                </div>
            </div>
            <nav class="header-nav">
                <a href="#" onclick="pywebio.session.run_js('show_api_doc()')">API</a>
                <a href="https://github.com/daveton/clipdown" target="_blank">GitHub</a>
            </nav>
        </div>
        """
        put_html(header_html)

    def _render_footer(self):
        footer_html = """
        <div class="footer">
            © 2026 ClipDown
        </div>
        """
        put_html(footer_html)

    # 主界面/Main view
    def main_view(self):
        with use_scope('main'):
            favicon_url = _config['Web']['Favicon']

            # 注入CSS和meta标签 / Inject CSS and meta tags
            self._inject_head(favicon_url)

            # 头部 / Header
            self._render_header(favicon_url)

            # 主内容区 / Main content
            put_html('<div class="main-container">')

            # Hero区域 / Hero section
            hero_title = self.utils.t("下载视频", "Download Videos")
            hero_subtitle = self.utils.t("无水印提取", "Without Watermarks")
            hero_desc = self.utils.t("快速解析抖音、TikTok 和 Bilibili 视频", "Fast parsing for TikTok, Douyin and Bilibili")

            hero_html = f"""
            <div class="hero-section">
                <h2 class="hero-title">
                    {hero_title}
                    <span class="muted">{hero_subtitle}</span>
                </h2>
                <p class="hero-desc">{hero_desc}</p>
            </div>
            """
            put_html(hero_html)

            # 输入卡片 / Input card
            put_html('<div class="input-card">')
            parse_video()
            put_html('</div>')

            # API预览卡片 / API preview card
            api_title = self.utils.t("API 示例", "API Example")
            api_preview_html = f"""
            <div class="api-card">
                <div class="api-header">POST /api/hybrid/video_data</div>
                <div class="api-code">curl -X POST https://api.clipdown.com/api/hybrid/video_data \\
  -H "Content-Type: application/json" \\
  -d '{{"url": "https://v.douyin.com/xxxxx", "minimal": true}}'</div>
            </div>
            """
            put_html(api_preview_html)

            put_html('</div>')  # 关闭main-container

            # 页脚 / Footer
            self._render_footer()
