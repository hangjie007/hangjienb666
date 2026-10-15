# shopping_agent.py
import streamlit as st
from PIL import Image

# ========== 1. 初始化页面 ==========
st.set_page_config(page_title="粤港澳跨境消费智能导购Agent", page_icon="🛒")
st.title("🛒 跨境消费多模态智能导购Agent")
st.subheader("面向粤港澳赴澳购物用户AI助手")
st.divider()

# ========== 2. 知识库（珠澳通关规则 + 商品库，你可以继续扩充） ==========
custom_knowledge = {
    "通关限额": "内地居民从澳门携带物品入境内地，免税额5000元人民币；烟酒等有单独限额，化妆品单次携带不可大量囤积。",
    "美妆": "澳门美妆门店价格普遍比内地低，留意保质期；液体化妆品随身携带有容量限制。",
    "零食": "肉干、新鲜水果禁止带入内地；密封包装饼干巧克力一般可正常携带。"
}

# 模拟Agent工具函数
def commodity_recognition(image):
    """多模态商品识别函数，这里模拟结果，后续接入LLaVA"""
    return "识别商品：面膜（美妆类）"

def price_compare(good_name):
    """模拟比价"""
    return f"{good_name}：澳门线下门店 180 MOP，内地电商参考价 165 CNY"

def sentiment_analysis(good_name):
    """评论情感分析，模拟输出"""
    return "用户评价总结：保湿效果好；负面反馈集中在面膜香味偏浓，敏感肌谨慎使用。"

def query_policy(category):
    """查询通关政策"""
    if category in custom_knowledge:
        return custom_knowledge[category]
    else:
        return "暂无该品类通关资料，请确认商品类别。"

# ========== 3. 网页交互区 ==========
# 文字提问
user_text = st.text_input("💬 文字提问：你可以询问商品价格、通关规则、商品评价", placeholder="例如：面膜可以带多少回珠海？")

# 图片上传
upload_img = st.file_uploader("📷 上传商品图片识别", type=["jpg", "png", "jpeg"])
img_result = ""
if upload_img is not None:
    image = Image.open(upload_img)
    st.image(image, width=300)
    img_result = commodity_recognition(image)
    st.success(img_result)

st.divider()
# ==========4. Agent 推理输出 ==========
if st.button("🚀 开始查询，Agent分析"):
    st.subheader("智能导购Agent输出结果")
    # 如果上传图片，先使用图片识别结果
    if img_result:
        goods_name = img_result.split("：")[-1]
        st.write(price_compare(goods_name))
        st.write(sentiment_analysis(goods_name))
        st.write("📜通关政策：" + query_policy(goods_name))
    elif user_text:
        st.write(f"收到你的问题：{user_text}")
        # 这里后续接入大模型，实现自然语言理解、工具调用
        st.info("【待接入大模型】Agent将自动判断需要调用比价/评论/通关知识库工具")
    else:
        st.warning("请输入文字提问，或者上传商品图片！")

st.markdown("---")
st.caption("项目：跨境消费多模态智能导购Agent｜全国人工智能应用创新大赛 消费赛道")