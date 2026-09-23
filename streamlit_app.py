import streamlit as st
import pandas as pd
import numpy as np

# 1. تهيئة وإعدادات الصفحة الرئيسية
st.set_page_config(
    page_title="Enterprise Shock Simulation AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. العنوان الرئيسي والترويسة
st.title("🛡️ Enterprise Shock Simulation AI Platform")
st.caption("منصة محاكاة الصدمات الاقتصادية والمالية التفاعلية واستجابة الذكاء الاصطناعي")
st.divider()

# 3. القائمة الجانبية - معلمات التحكم بالصدمة
st.sidebar.header("⚙️ معلمات المحاكاة (Simulation Parameters)")

shock_type = st.sidebar.selectbox(
    "نوع الصدمة الاقتصادية:",
    ["ارتفاع التضخم / الفائدة", "صدمة سلاسل الإمداد", "تذبذب أسعار العملات", "انخفاض الطلب والسوق"]
)

severity = st.sidebar.slider("شدة الصدمة (%):", min_value=5, max_value=50, value=20)
duration_months = st.sidebar.slider("مدة التأثير (أشهر):", min_value=1, max_value=24, value=6)

# 4. محرك الحسابات المالية التقديرية
months = [f"شهر {i+1}" for i in range(duration_months)]
base_revenue = 1000000  # $1,000,000
impact_factor = 1 - (severity / 100)

revenue_impacted = [base_revenue * (impact_factor ** (i / duration_months)) for i in range(duration_months)]
cashflow_impacted = [r * 0.25 for r in revenue_impacted]

# 5. عرض مؤشرات الأداء الحيوية (KPIs)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="الصدمة النشطة", value=shock_type)
with col2:
    st.metric(label="الانخفاض المباشر بالإنتاج/الإيرادات", value=f"-{severity}%", delta_color="inverse")
with col3:
    st.metric(label="أفق التعافي المتوقع", value=f"{duration_months} أشهر")

st.write("")
st.subheader("📊 مسار الإيرادات والتدفق النقدي المتوقع أثناء الصدمة")

# 6. الرسم البياني التفاعلي
df_chart = pd.DataFrame({
    "الإيرادات ($)": revenue_impacted,
    "التدفق النقدي ($)": cashflow_impacted
}, index=months)

st.line_chart(df_chart)

# 7. استجابة الذكاء الاصطناعي الذاتية
st.divider()
st.subheader("🤖 خطة الاستجابة التلقائية للذكاء الاصطناعي (Autonomous Response)")

if st.button("🚀 تفعيل بروتوكول التحوط والاستجابة الذاتية"):
    st.success("تم تفعيل بروتوكول حماية السيولة وقواعد إعادة التخصيص التلقائي بنجاح!")
    st.json({
        "حالة التحوط": "نشط (100%)",
        "سياسة التوريد": "تأمين المخزون المباشر لأجل 90 يوم",
        "مستوى المخاطرة بعد التدخل": "منخفض - آمن"
    })

# 8. جدول التفاصيل المالية المباشرة
with st.expander("🔍 عرض جدول البيانات المالي المباشر"):
    st.dataframe(df_chart)

st.divider()
st.success("✅ تم تحميل المنصة بنجاح وهي جاهزة للاستخدام!")
  
