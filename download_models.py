'''
Author: zhangzheyu zheyuzhang527@gmail.com
Date: 2023-05-24 14:35:38
LastEditors: zhangzheyu zheyuzhang527@gmail.com
LastEditTime: 2023-06-12 14:31:04
FilePath: /mms/download_models.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE

'''
import os
# lang_list=['tha','pol','kor','deu','ind','spa','vie','por','fra']

lang_list=['eng']
for lang in lang_list:
    if os.path.isdir(f"models/{lang}"):
        continue
    if not os.path.exists(f"{lang}.tar.gz"):
        # cmd=f"wget https://dl.fbaipublicfiles.com/mms/tts/{lang}.tar.gz"
        cmd=f"wget https://dl.fbaipublicfiles.com/mms/tts/full_model/{lang}.tar.gz"
        os.system(cmd)
    cmd=f"tar -xvf {lang}.tar.gz -C models"
    os.system(cmd)