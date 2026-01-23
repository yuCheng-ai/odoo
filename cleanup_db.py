# 彻底清理旧模块记录
old_module = env['ir.module.module'].search([('name', '=', 'china_login_style')])
if old_module:
    print('Found old module china_login_style, cleaning up...')
    # 强制设为未安装状态并删除
    old_module.state = 'uninstalled'
    env['ir.model.data'].search([('module', '=', 'china_login_style')]).unlink()
    old_module.unlink()
    print('Old module record removed.')

# 确保新模块处于安装队列
new_module = env['ir.module.module'].search([('name', '=', 'liuyun_custom')])
if new_module:
    print('Marking liuyun_custom for installation...')
    new_module.state = 'to install'
else:
    print('liuyun_custom not found in DB, updating module list...')
    env['ir.module.module'].update_list()
    new_module = env['ir.module.module'].search([('name', '=', 'liuyun_custom')])
    if new_module:
        new_module.state = 'to install'

env.cr.commit()
print('Database cleanup finished.')
