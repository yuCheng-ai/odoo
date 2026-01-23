{
    'name': '流云 ERP 定制模块',
    'version': '1.0',
    'category': 'Theme/Backend',
    'summary': '流云 ERP 品牌定制、样式美化与功能增强',
    'description': """
        该模块用于承载“流云 ERP”的所有自定义改动，包括：
        1. 登录页面中国风美化
        2. 后台菜单顺序优化（默认显示仪表板）
        3. 品牌标识（Logo、名称）统一
        4. 左右布局侧边栏导航
    """,
    'author': 'Super Individual',
    'depends': ['web', 'auth_signup', 'mail', 'spreadsheet_dashboard'],
    'data': [
        'views/login_templates.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'liuyun_custom/static/src/scss/sidebar.scss',
            'liuyun_custom/static/src/xml/navbar.xml',
        ],
        'web.assets_frontend': [
            'liuyun_custom/static/src/scss/login.scss',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
