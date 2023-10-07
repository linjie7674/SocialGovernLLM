# 运行方式：
# 1. 安装必要的包：pip install streamlit-option-menu streamlit-chatbox>=1.1.6
# 2. 运行本机fastchat服务：python server\llm_api.py 或者 运行对应的sh文件
# 3. 运行API服务器：python server/api.py。如果使用api = ApiRequest(no_remote_api=True)，该步可以跳过。
# 4. 运行WEB UI：streamlit run webui.py --server.port 7860

import streamlit as st
from webui_pages.utils import *
from streamlit_option_menu import option_menu
from webui_pages import *
import os
from configs import VERSION
from server.utils import api_address


api = ApiRequest(base_url=api_address())

if __name__ == "__main__":
    st.set_page_config(
        "社会治理大模型",
        os.path.join("img", "icon.png"),
        initial_sidebar_state="expanded",
        menu_items={
            # 'Get Help': 'https://github.com/chatchat-space/Langchain-Chatchat',
            # 'Report a bug': "https://github.com/chatchat-space/Langchain-Chatchat/issues",
            'About': f"""欢迎使用 社会治理大模型 {VERSION}！"""
        }
    )

    if not chat_box.chat_inited:
        st.toast(
            f"欢迎使用`社会治理大模型` ! \n\n"
            f"您可以开始提问了。"
        )

    pages = {
        "对话": {
            "icon": "chat",
            "func": dialogue_public_page,
        },
        # "知识库管理": {
        #     "icon": "hdd-stack",
        #     "func": knowledge_base_page,
        # },
    }

    with st.sidebar:
        st.image(
            os.path.join(
                "img",
                "logo.png"
            ),
            use_column_width=True
        )
        st.caption(
            f"""<p align="right">当前版本：{VERSION}</p>""",
            unsafe_allow_html=True,
        )
        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        default_index = 0
        selected_page = option_menu(
            "",
            options=options,
            icons=icons,
            # menu_icon="chat-quote",
            default_index=default_index,
        )

    if selected_page in pages:
        pages[selected_page]["func"](api)
