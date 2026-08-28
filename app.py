import streamlit as st
import pandas as pd

# 1. Configuration de la page
st.set_page_config(page_title="CMC Nador - Évaluation Diagnostique 2026-2027", page_icon="🧠", layout="wide")

# 2. Gestion de la base de données en mémoire vive (Session State) pour le Cloud
if "df_data" not in st.session_state:
    st.session_state.df_data = pd.DataFrame(columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])

# System de navigation
page = st.sidebar.radio("Navigation / التنقل:", ["📝 Espace Stagiaire (التقويم التشخيصي)", "🔐 Tableau de Bord Formateur (الاستراتيجيات)"])

# ==========================================
# 📝 Partie I : Formulaire Stagiaire
# ==========================================
if page == "📝 Espace Stagiaire (التقويم التشخيصي)":
    st.title("📊 CMC Nador - Évaluation Diagnostique (Rentrée 2026-2027)")
    st.subheader("Filière: Finance et Comptabilité (GEOCF)")
    st.write("Bienvenue cher(e) stagiaire. Ce test scientifique évalue votre style de réflexion afin de vous proposer des conseils pédagogiques.")
    
    with st.form("diagnostique_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            nom = st.text_input("Nom et Prénom (الاسم الكامل):")
        with col2:
            niveau = st.selectbox("Votre Niveau Actuel (مستواك الحالي):", ["1ère année Tronc Commun", "2ème année TSGEOCF", "3ème année TSGEOCF"])
        with col3:
            groupe = st.text_input("Groupe / Section (الفوج):")
            
        st.divider()
        q1 = st.slider("1. Dans un groupe, je prends facilement la parole.", 1, 5, 3)
        q2 = st.slider("2. Je préfère travailler seul sur un projet complexe.", 1, 5, 3)
        q3 = st.slider("3. J'éprouve un réel plaisir à expliquer une notion difficile.", 1, 5, 3)
        q4 = st.slider("4. Je pense que chacun doit se débrouiller seul pour réussir.", 1, 5, 3)
        q5 = st.slider("5. Je suis très pointilleux avec les chiffres et les détails.", 1, 5, 3)
        q6 = st.slider("6. J'improvise souvent في عملي وتخطيطي.", 1, 5, 3)
        q7 = st.slider("7. Je perds facilement mes moyens face à un exercice inconnu.", 1, 5, 3)
        q8 = st.slider("8. Je garde mon calme ومستعد للعمل تحت الضغط.", 1, 5, 3)
        q9 = st.slider("9. J'adore explorer de nouveaux outils numériques (Logiciels, IA).", 1, 5, 3)
        q10 = st.slider("10. Je préfère les méthodes d'apprentissage traditionnelles.", 1, 5, 3)

        submitted = st.form_submit_button("Envoyer et Voir mes Résultats 🚀")
        
        if submitted:
            if not nom or not groupe:
                st.error("❌ Veuillez remplir impérativement les champs Nom et Groupe.")
            else:
                score_e = float(q1 + (6 - q2)) / 2
                score_a = float(q3 + (6 - q4)) / 2
                score_c = float(q5 + (6 - q6)) / 2
                score_n = float(q7 + (6 - q8)) / 2
                score_o = float(q9 + (6 - q10)) / 2
                
                new_row = pd.DataFrame([[nom, niveau, groupe, score_e, score_a, score_c, score_n, score_o]], columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])
                st.session_state.df_data = pd.concat([st.session_state.df_data, new_row], ignore_index=True)
                
                st.balloons()
                st.success("🎉 Vos réponses ont été transmises avec succès !")
                st.divider()
                st.markdown(f"## 📋 Votre Profil d'Apprentissage, {nom}")
                
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    st.markdown("### 🎓 Conseils Pédagogiques :")
                    if score_c <= 2.5:
                        st.info("💡 **Organisation :** Utilisez des checklists pour valider vos bilans.")
                    else:
                        st.success("💡 **Rigueur :** Excellente capacité de concentration naturelle.")
                with col_res2:
                    st.markdown("### 💼 Conseils Professionnels :")
                    if score_o >= 3.5:
                        st.success("🎯 **Atout Métier :** Profil idéal pour l'Audit comptable ou le Conseil fiscal.")
                    else:
                        st.info("🎯 **Atout Métier :** Profil idéal pour la Gestion de la Paie ou la Comptabilité pure.")

# ==========================================
# 🔐 Partie II : Tableau de Bord Formateur
# ==========================================
elif page == "🔐 Tableau de Bord Formateur (الاستراتيجيات)":
    st.title("🔐 Espace d'Ingنيerie Pédagogique - Rentrée 2026-2027")
    password = st.text_input("Code d'accès secret :", type="password")
    
    if password == "CMC_Nador_2026":
        st.success("🔓 Accès autorisé.")
        df = st.session_state.df_data
        
        if df.empty:
            st.info("📂 Aucune donnée disponible pour le moment. En attente des réponses des stagiaires.")
        else:
            niveau_select = st.selectbox("Sélectionnez le groupe à analyser:", ["1ère année Tronc Commun", "2ème année TSGEOCF", "3ème année TSGEOCF"])
            df_filtered = df[df["Niveau"] == niveau_select]
            
            if df_filtered.empty:
                st.warning("Aucun stagiaire enregistré dans ce niveau pour le moment.")
            else:
                st.subheader(f"📊 Analyse Globale du Groupe : {niveau_select}")
                moy_e = df_filtered["Extraversion"].mean()
                moy_c = df_filtered["Conscientiousness"].mean()
                moy_n = df_filtered["Neuroticism"].mean()
                moy_o = df_filtered["Openness"].mean()
                
                col_m1, col_m2, col_m3, col_m4 = st.columns(4)
                with col_m1: st.metric("Effectif diagnostiqué", len(df_filtered))
                with col_m2: st.metric("Rigueur Globale (C)", round(moy_c, 2))
                with col_m3: st.metric("Résistance au Stress", round(6 - moy_n, 2))
                with col_m4: st.metric("Agilité Numérique (O)", round(moy_o, 2))
                
                st.divider()
                st.markdown("### 🎯 Stratégie Pédagogique Globale pour le Groupe (Tendances Mondiales 2026)")
                if "2ème année" in niveau_select:
                    st.write("• **Pratique de la paie & Comptabilité Approfondie :** Utilisez le *Micro-learning* si la rigueur globale est faible.")
                    st.write("• **Bureautique Avancée :** Intégrez la *Gamification* (Défis Excel).")
                elif "3ème année" in niveau_select:
                    st.write("• **Audit & Télédéclarations :** Appliquez l'*Erreur Apprenante* sur plateforme sandbox.")
                    st.write("• **Normes IAS/IFRS :** Utilisez la *Classe Inversée*.")
                
                st.divider()
                st.markdown("### 📋 Liste des Profils Diagnostiqués")
                st.dataframe(df_filtered)
                
                csv_data = df_filtered.to_csv(index=False).encode('utf-8-sig')
                st.download_button(label="📥 Télécharger la base", data=csv_data, file_name="Diagnostique.csv")
                
    elif password != "":
        st.error("❌ Code d'accès secret incorrect.")
