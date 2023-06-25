# How to use:
```
- replace the language code in download_models.py with the language code you want to use
e.g. ['eng','kor']
- run download_models.py
- perpare your dataset and modify the config file. rename it to config_ft.json
- run train.py
```
安装参考https://github.com/jaywalnut310/vits
注意MA那一步需要先
```
mkdir monotonic_align
cd monotonic_align
python setup.py build_ext --inplace
```
