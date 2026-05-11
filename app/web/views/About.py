from pywebio.output import popup, put_markdown, put_html, put_text, put_link, put_image
from app.web.views.ViewsUtils import ViewsUtils

t = ViewsUtils().t


# 关于弹窗/About pop-up
def about_pop_window():
    with popup(t('更多信息', 'More Information')):
        put_html('<h3>⭐{}</h3>'.format(t('项目信息', 'Project Info')))
        put_markdown('[ClipDown](https://github.com/daveton/clipdown) - 视频下载工具')
        put_html('<hr>')
        put_html('<h3>🎯{}</h3>'.format(t('反馈', 'Feedback')))
        put_markdown('{}：[GitHub Issues](https://github.com/daveton/clipdown/issues)'.format(
            t('Bug反馈', 'Bug Feedback')))
        put_html('<hr>')
