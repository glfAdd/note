# -*- coding: utf-8 -*-
import gettext
import os


class I18nBase:
    @staticmethod
    def get_i18n(*, file_name: str, languages=None) -> gettext:
        cur_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        """
        domain: 翻译文件名
        localedir
        languages: 转换语言列表(遍历, 先找到哪个用哪个)
        class_
        fallback
        codeset=None
        """
        return gettext.translation(domain=file_name, localedir=cur_dir, languages=languages).gettext


if __name__ == '__main__':
    _ = I18nBase.get_i18n(file_name='abc', languages=['zh-CN', 'en-US'])
