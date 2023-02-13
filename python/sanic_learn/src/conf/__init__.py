import os


def load_config():
    """
    设置系统环境变量, 进行配置文件的选择
    export MODE = PRO
    """
    mode = os.environ.get('MODE', "DEV")
    if mode == 'PRO':
        from .pro_conf import ProConfig
        return ProConfig
    elif mode == 'DEV':
        from .dev_conf import DevConfig
        return DevConfig
    else:
        from .dev_conf import DevConfig
        return DevConfig


CONFIG = load_config()
