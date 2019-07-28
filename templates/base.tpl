<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
        <title>{% block title %}首页{% endblock %} - ThreatScan - 免费的网站在线安全检测平台-TScan</title>
        <link rel="icon" href="/static/img/favicon.ico">
        <link rel="stylesheet" href="/static/plugins/layui/css/layui.css">
        <link rel="stylesheet" href="/static/style/main.css">
        <!-- 自定义的css -->
        {% block custom_css %} {% endblock %}
    </head>
    <body>
        <!-- 导航栏 -->
        <header class="layui-header layui-bg-blue">
            <div class="header-content">
                <a class="layui-logo" href="/">
                    <img src="/static/img/logo.png" alt="ThreatScan" width="100px">
                </a>
                {% block page_guider %}{% endblock %}
            </div>
        </header>


        <!-- 内容区 -->
        <div class="layui-container">
            {% block content %} {% endblock %}
        </div>


        <!-- 底部信息 -->
        <footer class="footer">
            {% include 'footer.tpl' %}
        </footer>

        <script src="/static/js/jquery.min.js"></script>
        <script src="/static/plugins/layui/layui.js"></script>
        <script>
            layui.use(['layer', 'form', 'element'], function(){
                  const layer = layui.layer,
                        form = layui.form,
                        element = layui.element;
            {% block page_js %}

            {% endblock %}
        </script>
        <script>var _hmt = _hmt || [];(function() {var hm = document.createElement("script");hm.src = "https://hm.baidu.com/hm.js?a8569fd6981018f096d774868306a054";var s = document.getElementsByTagName("script")[0]; s.parentNode.insertBefore(hm, s);})();</script>
    </body>
</html>