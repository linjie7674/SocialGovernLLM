# 社会治理大模型
## 环境搭建
测试python版本：3.10
```bash
pip3 install -r requirements.txt
```
## 下载模型
在huggingface中下载模型vicuna-13b-v1.5和m3e-base。将vicuna-13b-v1.5模型放在./models/base-models/目录（若没有，则自行创建）中，将m3e-base放在./目录中。
## 下载知识库
使用以下命令下载知识库，并将其放入项目的根目录中。
```bash
wget https://bdbl-cm01.baidupcs.com/file/2ea559f4ejbc568f8481c92b8e7c98be\?bkt\=en-29a7ad5d1913bc6f856142332e57d9d8b5319a2a9bd65877b2015a4219d6a02733e949d4dbc4037d\&fid\=909904854-250528-1064050115500439\&time\=1696673109\&sign\=FDTAXUbGERLQlBHSKfWqiu-DCb740ccc5511e5e8fedcff06b081203-v7oxwYaKp09rTiAxDt8LuS6yS58%3D\&to\=401\&size\=28299537\&sta_dx\=28299537\&sta_cs\=1\&sta_ft\=zip\&sta_ct\=0\&sta_mt\=0\&fm2\=MH%2CBaoding%2CAnywhere%2C%2C%E6%B5%99%E6%B1%9F%2Ccmnet\&ctime\=1696672029\&mtime\=1696672029\&resv0\=-1\&resv1\=0\&resv2\=rlim\&resv3\=5\&resv4\=28299537\&vuk\=909904854\&iv\=0\&htype\=\&randtype\=\&tkbind_id\=0\&newver\=1\&newfm\=1\&secfm\=1\&flow_ver\=3\&pkey\=en-0826deb4c852dff386285183478ac1a73438996f4cd6b53646e9c5943e2d70c2e40da8c92749a209\&sl\=76480590\&expires\=8h\&rt\=sh\&r\=464013599\&vbdid\=213245502\&fin\=knowledge_base.zip\&fn\=knowledge_base.zip\&rtype\=1\&dp-logid\=8794118195036767539\&dp-callid\=0.1\&hps\=1\&tsl\=80\&csl\=80\&fsl\=-1\&csign\=lmihIepyto6fL9tYx0%2FgHMmwWLU%3D\&so\=0\&ut\=6\&uter\=4\&serv\=0\&uc\=3306545997\&ti\=068bcab50ae430c7fe89d949283b30407088159e83a1c58b\&hflag\=30\&from_type\=1\&adg\=c_efb1f7e9d00e4438de18e11a642c975e\&reqlabel\=250528_f_33b3553e711fa660f520c2802b819c00_-1_dd784c904d2d035ad8d468ce02e655b9\&fpath\=%E6%B5%99%E5%A4%A7%2F%E7%A4%BE%E4%BC%9A%E6%B2%BB%E7%90%86%E5%A4%A7%E6%A8%A1%E5%9E%8B\&by\=themis\&resvsflag\=1-0-0-1-1-1 -O knowledge_base.zip
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