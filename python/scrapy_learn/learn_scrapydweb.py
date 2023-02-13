""" ============================ ��װ
pip install scrapydweb


�ο�
https://zhuanlan.zhihu.com/p/99449687
"""

""" ============================ ����
��������scrapydweb���״��������ڵ�ǰĿ¼�����������ļ� scrapydweb_settings_v8.py

����
scrapydweb

web ҳ��
http://localhost:5000/
"""

""" ============================ scrapydweb_settings_v8.py 
1. web ��¼��֤
�ر�
ENABLE_AUTH = False

����
ENABLE_AUTH = True
USERNAME = 'username'
PASSWORD = 'password'


2. �˿�
SCRAPYDWEB_PORT = 5000


3. ָ�� Scrapy ��Ŀ����Ŀ¼
ScrapydWeb ���Զ��г���·���µ�������Ŀ��Ĭ��ѡ�����±༭����Ŀ��ѡ����Ŀ�󼴿��Զ�����Ͳ���ָ����Ŀ.
ScrapydWeb �ڱ��ص�ʱ���������. 
��� ScrapydWeb ������Զ�̷������ϣ�����ͨ����ǰ���������ϴ������ egg �ļ���Ҳ���Խ�������Ŀ�ļ�����ӵ� zip/tar/tar.gz ѹ���ļ���ֱ���ϴ����ɣ������ֶ����Ϊ egg �ļ�
SCRAPY_PROJECTS_DIR = '/home/xieyabin/myprojects/'


4. ��־
# ��־�ļ�����ĵ�ַ��������־����
LOCAL_SCRAPYD_LOGS_DIR = '/Users/glfadd/Desktop'
# ������־
ENABLE_LOGPARSER = True


ENABLE_MONITOR = True





6.�ʼ����ã�ͨ����ѯ�ӽ����ں�̨��ʱģ����� Stats ҳ�棬ScrapydWeb ���������ض�������ʱ�����趨�Զ�ֹͣ�������񲢷���֪ͨ�ʼ����ʼ����İ�����ǰ���������ͳ����Ϣ��
1.��������ʺţ�
    SMTP_SERVER = 'smtp.qq.com'
    SMTP_PORT = 465
    SMTP_OVER_SSL = True
    SMTP_CONNECTION_TIMEOUT = 10

    EMAIL_USERNAME = ''  # defaults to FROM_ADDR
    EMAIL_PASSWORD = 'password'
    FROM_ADDR = 'username@qq.com'
    TO_ADDRS = [FROM_ADDR]
2.�����ʼ�����ʱ��ͻ���������������ʾ������ÿ��1Сʱ��ĳһ�������ʱ�����ҵ�ǰʱ���ǹ����յ�9�㣬12���17�㣬ScrapydWeb ���ᷢ��֪ͨ�ʼ���
    EMAIL_WORKING_DAYS = [1, 2, 3, 4, 5]
    EMAIL_WORKING_HOURS = [9, 12, 17]
    ON_JOB_RUNNING_INTERVAL = 3600
    ON_JOB_FINISHED = True
3.���˻�����������ScrapydWeb ���ṩ�˶��ִ��������ڴ���ͬ���͵� log������ 'CRITICAL', 'ERROR', 'WARNING', 'REDIRECT', 'RETRY' �� 'IGNORE'�ȡ�
    LOG_CRITICAL_THRESHOLD = 3
    LOG_CRITICAL_TRIGGER_STOP = True
    LOG_CRITICAL_TRIGGER_FORCESTOP = False
    # ...
    LOG_IGNORE_TRIGGER_FORCESTOP = False
����ʾ����������־�г���3�������ϵ� critical ����� log ʱ��ScrapydWeb ���Զ�ֹͣ��ǰ���������ǰʱ�����ʼ�����ʱ���ڣ���ͬʱ����֪ͨ�ʼ���
"""

""" ============================ logparser 
��־
��ʾ����:
'pip install logparser' on host '127.0.0.1:6800' and run command 'logparser' to show crawled_pages and scraped_items.

��װ
pip install logparser

����
vim /Users/glfadd/.pyenv/versions/3.6.6/envs/p366/lib/python3.6/site-packages/logparser/settings.py
�޸�
SCRAPYD_LOGS_DIR = '/Users/glfadd/Desktop'
SCRAPYD_SERVER = '127.0.0.1:6800'


webҳ��
http://127.0.0.1:6800/logs/stats.json



"""

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """

""" ============================ qwewqe """
