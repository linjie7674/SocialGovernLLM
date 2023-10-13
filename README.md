# 社会治理大模型
## 环境搭建
测试python版本：3.10
```bash
pip3 install -r requirements.txt
```
## 下载模型
在huggingface中下载模型vicuna-13b-v1.5和m3e-base。将vicuna-13b-v1.5模型放在./models/base-models/目录（若没有，则自行创建）中，将m3e-base放在./目录中。
## 下载知识库
使用以下链接下载知识库，并将其放入项目的根目录中。
```bash
https://pan.baidu.com/s/11a4t9iB6mXvstu3oXnpdSg?pwd=ham7
```

## 运行模型api
```bash
python3 startup.py --llm-api
```
## 运行webui
```bash
python3 startup.py --webui --is_public
```
## 更改模型路径
若模型放在其他路径下，需更改configs/model_config.py文件中对应模型的路径。
```Python3
"vicuna-13b-v1.5": {
    "local_model_path": "{root_dir}/models/base-models/vicuna-13b-v1.5",
    ...
},
```

```Python3
embedding_model_dict = {
    ...
    "m3e-base": f"{root_dir}/m3e-base",
    ...
}
```

## 使用
访问<http://127.0.0.1:8501>网址即可开始使用。
