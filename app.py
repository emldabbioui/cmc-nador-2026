import streamlit as st
import pandas as pd
import os

# 1. إعدادات المنصة العامة
st.set_page_config(page_title="منصة التسيير والتحليل السيكولوجي البيداغوجي", page_icon="🧠", layout="wide")

# 2. إدارة قاعدة البيانات
DATA_FILE = "cmc_diagnostique_2026.csv"
if not os.path.exists(DATA_FILE):
    df_empty = pd.DataFrame(columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])
    df_empty.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')

page = st.sidebar.radio("قائمة التحكم والتنقل:", ["📝 فضاء المتدرب (التقويم التشخيصي)", "🔐 لوحة تحكم الأستاذ (الاستراتيجيات النفسية)"])

# ==========================================
# 📝 الجزء الأول: فضاء المتدرب والتحليل الفردي المعمق
# ==========================================
if page == "📝 فضاء المتدرب (التقويم التشخيصي)":
    st.title("📊 مدينة المهن والكفاءات بالناظور - التقويم التشخيصي السيكولوجي")
    st.subheader("قطاع التسيير والتجارة | شعبة الهندسة المالية والمحاسبة")
    
    with st.form("diagnostique_form"):
        nom = st.text_input("الاسم الكامل (Nom et Prénom):")
        niveau = st.selectbox("المستوى الدراسي الحالي:", ["السنة الأولى - جذع مشترك", "السنة الثانية - تخصص الهندسة المالية والمحاسبة", "السنة الثالثة - تخصص الهندسة المالية والمحاسبة"])
        groupe = st.text_input("الفوج / القسم (Groupe):")
        st.divider()
        
        q1 = st.slider("1. أشعر بالنشاط والحيوية وسط النقاشات الجماعية المفتوحة.", 1, 5, 3)
        q2 = st.slider("2. أفضّل معالجة التمارين بمفردي في أجواء هادئة.", 1, 5, 3)
        q3 = st.slider("3. يسعدني جداً توجيه زملائي وتبسيط المفاهيم الصعبة لهم.", 1, 5, 3)
        q4 = st.slider("4. أرى أن النجاح مسؤولية فردية ولا أحب التباطؤ بسبب الآخرين.", 1, 5, 3)
        q5 = st.slider("5. أنا شخص شديد التدقيق في البيانات والأرقام والتفاصيل.", 1, 5, 3)
        q6 = st.slider("6. أفضّل معالجة المهام بمرونة وعفوية دون جداول صارمة.", 1, 5, 3)
        q7 = st.slider("7. ينتابني قلق شديد وتوتر عند مواجهة فرض غير متوقع.", 1, 5, 3)
        q8 = st.slider("8. أحافظ على ثباتي الانفعالي وبرود أعصابي تحت الضغط.", 1, 5, 3)
        q9 = st.slider("9. يستهويني البحث عن أدوات تكنولوجية وبرمجيات متطورة.", 1, 5, 3)
        q10 = st.slider("10. أرتاح للأساليب الكلاسيكية الواضحة والمعتمدة مسبقاً.", 1, 5, 3)
        
        submitted = st.form_submit_button("إرسال الإجابات واستخراج التقرير 🚀")

    if submitted and (not nom or not groupe):
        st.error("❌ عذراً، يرجى إدخال الاسم والفوج أولاً قبل الإرسال.")
        
    if submitted and nom and groupe:
        score_e = float(q1 + (6 - q2)) / 2
        score_a = float(q3 + (6 - q4)) / 2
        score_c = float(q5 + (6 - q6)) / 2
        score_n = float(q7 + (6 - q8)) / 2
        score_o = float(q9 + (6 - q10)) / 2
        
        new_row = pd.DataFrame([[nom, niveau, groupe, score_e, score_a, score_c, score_n, score_o]], columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])
        new_row.to_csv(DATA_FILE, mode='a', header=False, index=False, encoding='utf-8-sig')
        
        st.balloons()
        st.success("🎉 تم تسجيل بياناتك النفسية بنجاح.")
        st.divider()
        st.markdown(f"## 📋 التقرير السيكولوجي الفردي الشامل: {nom}")
        
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.markdown("### 🔍 أولاً: التشخيص البنيوي للشخصية")
            if score_c >= 3.0:
                st.markdown("**💪 نقاط القوة:** دقة متناهية في الملاحظة، قدرة عالية على ضبط الحسابات وتفادي الأخطاء، الالتزام بالمسؤولية.")
                st.markdown("**⚠️ نقاط الضعف المحتملة:** المبالغة في التدقيق قد تقودك إلى البطء أو الوقوع في فخ المثالية المفرطة.")
            else:
                st.markdown("**💪 نقاط القوة:** مرونة عالية في التكيف مع المستجدات وسرعة البديهة في إيجاد مخارج بديلة.")
                st.markdown("**⚠️ نقاط الضعف المحتملة:** ضعف نسبي في التركيز على الجزئيات الحسابية الدقيقة وتأجيل الواجبات.")
        with col_res2:
            st.markdown("### 🎓 ثانياً: التوجيهات البيداغوجية")
            if score_c <= 2.5:
                st.info("💡 يتعين عليك استخدام 'جداول التدقيق والتحقق' (Checklists) لتنظيم المراجعة وتجنب السهو.")
            else:
                st.success("💡 أنت قادر بامتياز على التعلم الذاتي وحل دراسات الحالة المتكاملة بشكل مستقل.")

# ==========================================
# 🔐 الجزء الثاني: لوحة تحكم الأستاذ
# ==========================================
elif page == "🔐 لوحة تحكم الأستاذ (الاستراتيجيات النفسية)":
    st.title("🔐 الفضاء التربوي السري للأستاذ المكون الباحث")
    password = st.text_input("الرجاء إدخال الرمز السري للولوج:", type="password")
    
    if password == "CMC_Nador_2026":
        st.success("🔓 تم تأكيد الهوية بنجاح.")
        df = pd.read_csv(DATA_FILE, encoding='utf-8-sig')
        
        if df.empty:
            st.info("📂 لا توجد أي بيانات حالياً في الملف.")
        else:
            niveau_select = st.selectbox("اختر الفوج الدراسي المستهدف:", ["السنة الأولى - جذع مشترك", "السنة الثانية - تخصص الهندسة المالية والمحاسبة", "السنة الثالثة - تخصص الهندسة المالية والمحاسبة"])
            df_filtered = df[df["Niveau"] == niveau_select].reset_index(drop=True)
            
            if df_filtered.empty:
                st.warning("لم يقم أي متدرب من هذا الفوج بملء الاستمارة حتى الآن.")
            else:
                moy_e = df_filtered["Extraversion"].mean()
                moy_a = df_filtered["Agreeableness"].mean()
                moy_c = df_filtered["Conscientiousness"].mean()
                moy_n = df_filtered["Neuroticism"].mean()
                moy_o = df_filtered["Openness"].mean()
                
                col_m1, col_m2, col_m3, col_m4 = st.columns(4)
                with col_m1: st.metric("إجمالي المتدربين", len(df_filtered))
                with col_m2: st.metric("مؤشر الانضباط العام (C)", round(moy_c, 2))
                with col_m3: st.metric("مؤشر الاستقرار النفسي", round(6 - moy_n, 2))
                with col_m4: st.metric("مؤشر القابلية الرقمية (O)", round(moy_o, 2))
                
                st.divider()
                st.markdown("### 👤 أولاً: التشخيص النفسي الفردي والتحليل المعمق للمتدربين")
                
                for idx, row in df_filtered.iterrows():
                    with st.expander(f"👤 المتدرب(ة): {row['Nom Complet']} (الفوج الفرعي: {row['Groupe']})"):
                        col_st1, col_st2 = st.columns(2)
                        c_val, e_val, a_val, n_val, o_val = float(row['Conscientiousness']), float(row['Extraversion']), float(row['Agreeableness']), float(row['Neuroticism']), float(row['Openness'])
                        
                        with col_st1:
                            st.markdown("**💪 ملخص نقاط القوة البارزة :**")
                            if c_val >= 3.0: st.write("- دقة متناهية وحس تنظيم محاسبي صارم لضبط الدفاتر اليومية.")
                            else: st.write("- مرونة وسرعة في التكيف مع المتغيرات الإدارية غير المتوقعة.")
                            if e_val >= 3.0: st.write("- مهارات تواصلية ممتازة وقدرة على قيادة فرق العمل والمشاريع.")
                            else: st.write("- تركيز تحليلي مستقل وعميق لمعالجة المسائل الحسابية المعقدة.")
                            
                            st.markdown("**⚠️ ملخص نقاط الضعف والتحديات :**")
                            if c_val >= 3.0: st.write("- الميل لتضييع الوقت بسبب المبالغة في التدقيق والمثالية.")
                            else: st.write("- التسرع وعرضة لارتكاب أخطاء السهو في العمليات المطولة.")
                        
                        with col_st2:
                            st.markdown("**🚨 النزاعات والاضطرابات السلوكية المحتملة بالفصل :**")
                            if a_val <= 2.5 and e_val >= 3.0: st.error("🚨 **بروفايل صدامي :** يميل لفرض رأيه بحدة داخل المجموعات ويفتقر لمرونة الاستماع لزملائه.")
                            elif o_val >= 3.5 and c_val <= 2.5: st.warning("🔶 **بروفايل متمرد :** قد يتذمر من القواعد المحاسبية الصارمة والنماذج الضريبية الموحدة.")
                            elif e_val <= 2.2 and n_val >= 3.5: st.info("⚠️ **بروفايل هش :** متدرب انطوائي يعاني من قلق حاد. قد ينسحب صامتاً عند مواجهة الصعوبات.")
                            else: st.success("💚 **بروفايل متزن ومستقر سيكولوجياً:** يمتلك توازناً انفعالياً وانضباطاً معتدلاً.")

                st.divider()
                st.markdown("### 🤝 ثانياً: خوارزمية تشكيل الثنائيات الذكية (Binômes)")
                
                unpaired = list(df_filtered.index)
                binomes_count = 1
                while len(unpaired) >= 2:
                    idx1 = unpaired.pop(0)
                    best_match = None
                    min_distance = 999.0
                    for idx2 in unpaired:
                        dist = abs(float(df_filtered.loc[idx1, 'Conscientiousness']) - float(df_filtered.loc[idx2, 'Conscientiousness'])) + abs(float(df_filtered.loc[idx1, 'Extraversion']) - float(df_filtered.loc[idx2, 'Extraversion']))
                        if dist < min_distance:
                            min_distance = dist
                            best_match = idx2
                    unpaired.remove(best_match)
                    st.info(f"**🤝 الثنائي رقم {binomes_count}:** 【 {df_filtered.loc[idx1, 'Nom Complet']} 】 مَعَ 【 {df_filtered.loc[best_match, 'Nom Complet']} 】")
                    binomes_count += 1
                if len(unpaired) == 1:
                    st.warning(f"👤 **المتدرب المتبقي :** 【 {df_filtered.loc[unpaired[0], 'Nom Complet']} 】 *(ينصح بدمجه كعنصر ثالث)*")

                st.divider()
                st.markdown("### 📊 ثالثاً: التحليل الجماعي المعمق والتوجيه الإداري والبيداغوجي للفوج")
                col_an1, col_an2, col_an3 = st.columns(3)
                with col_an1:
                    st.markdown("#### 🧠 1. التشخيص النفسي الجمعي")
