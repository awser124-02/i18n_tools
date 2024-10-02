import xml.etree.ElementTree as ET
from os import path

def load_translations(language: str, file_path: str = 'i18n'):
    """load i18n translations from xml file

    ## Usage:
    ```python
    from i18n_tools.trans import load_translations
    translations = load_translations('en-US') # load translations for English

    def lang_get(key: str): # define a function to get translations
        __result__ = translations.get(key) # get translation
        if __result__ is None:
            raise TransError(f"Translation for key '{key}' not found.")
        else:
            return __result__ # output translation
       
    print(lang_get('hello')) # output 'hello'
    ```

    ## Warning:
    - The file path is relative to **the directory of this library**. Please set the file path to the location of your project.

    Args:
        language (str): language code, e.g. **en-US**, **zh-CN**
        file_path (str, optional): i18n translation file path. Defaults to 'i18n'.

    Returns:
        translations (dict): translation dictionary

    \n\n\n

    加载i18n翻译xml文件

    ## 用法:
    ```python
    from i18n_tools.trans import load_translations
    translations = load_translations('zh-CN') # 加载中文翻译

    def lang_get(key: str): # 定义获取翻译函数
        __result__ = translations.get(key) # 获取翻译
        if __result__ is None: # 若未找到翻译
            raise TransError(f"Translation for key '{key}' not found.") # 则抛出翻译错误
        else:
            return __result__ # 否则返回翻译
       
    print(lang_get('hello')) # 输出'你好'
    ```

    ## 警告:
    - 文件路径相对于**此库的目录**。请将文件路径设置为你的项目的位置。
    
    ## 参数:
        language (str): 语言代码, e.g. **en-US**, **zh-CN**
        file path (str, optional): i18n翻译文件路径。默认为'i18n'。

    ## 返回值:
        translations (dict): 翻译字典
    """
    translations = {}
    try:
        tree = ET.parse(path.join(file_path, f'{language}.xml'))
        root = tree.getroot()
        for string in root.findall('string'):
            name = string.get('name')
            value = string.text
            translations[name] = value
    except FileNotFoundError:
        raise TransError(f"Translation file for {language} not found.")
    return translations

class TransError(Exception):
    """Translation error

    Args:
        message (str): error message

    Raises:
        TransError: translation error

    \n\n\n

    翻译错误
    ## 参数:
        message (str): 错误信息

    ## 异常:
        TransError: 翻译错误
    """
    def __init__(self, message, code=None):
        super().__init__(message)

    def __str__(self):
        error_message = self.args[0]
        return "TranslationError: "+error_message
