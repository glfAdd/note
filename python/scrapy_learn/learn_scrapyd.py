"""
�������:
    scrapy: һ�������ܣ�����Դ���һ��scrapy��Ŀ
    scrapyd: �൱��һ��������ܹ���scrapy��Ŀ����Զ�̲��𣬵���ʹ�õ�. ����һ��cs��client-server������
    scrapydwe: scrapyd�Ŀ��ӽ���


scrapyd ����ʱ��ȡ scrapy.cfg �ļ�������
scrapydweb ������ scrapyd
"""

""" ============================  ��װ 
pip install scrapyd
"""

""" ============================ ���� 
scrapyd
service scrapyd {start|stop|status}
"""

""" ============================ ���� 
���ȡscrapy ��Ŀ scrapy.cfg �ļ�������
[deploy]                            # target ����
url = http://localhost:6800/        # scraypd ��������ַ
project = mySpider                  # ������


����Զ�̷���������
vim /usr/local/python3/lib/python3.6/site-packages/scrapyd/default_scrapyd.conf
��
bind_address = 127.0.0.1
��Ϊ
bind_address = 0.0.0.0
"""
