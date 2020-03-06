SECRET_KEY = '123!@#$()<><>'
template_folder = 'static'
JOBS = [
    {
        # 任务id
        'id': 'hci_main_status_update',
        # 任务执行程序
        'func': 'timing_task.main_hci:main_hci_status_update',
        # 执行程序参数
        'args': None,
        # 任务执行类型，定时器
        'trigger': 'interval',
        # 任务执行时间，单位秒
        'seconds': 10,
    }
]
