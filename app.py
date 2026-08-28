import streamlit as st
import pandas as pd

# 1. Configuration
st.set_page_config(page_title="CMC Nador - Évaluation Diagnostique 2026-2027", page_icon="🧠", layout="wide")

# 2. Database Memory
if "df_data" not in st.session_state:
    st.session_state.df_data = pd.DataFrame(columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])

page = st.sidebar.radio("Navigation / التنقل:", ["📝 Espace Stagiaire (التقويم التشخيصي)", "🔐 Tableau de Bord Formateur (الاستراتيجيات)"])

# ==========================================
# 📝 Partie I : Formulaire Stagiaire
# ==========================================
if page == "📝 Espace Stagiaire (التقويم التشخيصي)":
    st.title("📊 CMC Nador - Évaluation Diagnostique (Rentrée 2026-2027)")
    st.subheader("Filière: Finance et Comptabilité (GEOCF)")
    
    with st.form("diagnostique_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            nom = st.text_input("Nom et Prénom (الاسم الكامل):")
        with col2:
            niveau = st.selectbox("Votre Niveau Actuel:", ["1ère année Tronc Commun", "2ème année TSGEOCF", "3ème année TSGEOCF"])
        with col3:
            groupe = st.text_input("Groupe / Section (الفوج):")
            
        st.divider()
        q1 = st.slider("1. Dans un groupe, je prends facilement la parole.", 1, 5, 3)
        q2 = st.slider("2. Je préfère travailler seul sur un projet complexe.", 1, 5, 3)
        q3 = st.slider("3. J'éprouve un plaisir à expliquer aux autres.", 1, 5, 3)
        q4 = st.slider("4. Je pense que chacun doit se débrouiller seul.", 1, 5, 3)
        q5 = st.slider("5. Je suis très pointilleux avec les chiffres.", 1, 5, 3)
        q6 = st.slider("6. J'improvise souvent dans mon travail.", 1, 5, 3)
        q7 = st.slider("7. Je perds mes moyens face à un exercice inconnu.", 1, 5, 3)
        q8 = st.slider("8. Je garde mon calme quand le temps presse.", 1, 5, 3)
        q9 = st.slider("9. J'adore explorer de nouveaux outils numériques.", 1, 5, 3)
        q10 = st.slider("10. Je préfère les méthodes traditionnelles.", 1, 5, 3)

        submitted = st.form_submit_button("Envoyer 🚀")
        
        if submitted:
            if not nom or not groupe:
                st.error("❌ Veuillez remplir les champs Nom et Groupe.")
            else:
                score_e = (q1 + (6 - q2)) / 2
                score_a = (q3 + (6 - q4)) / 2
                score_c = (q5 + (6 - q6)) / 2
                score_n = (q7 + (6 - q8)) / 2
                score_o = (q9 + (6 - q10)) / 2
                
                new_row = pd.DataFrame([[nom, niveau, groupe, score_e, score_a, score_c, score_n, score_o]], columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])
                st.session_state.df_data = pd.concat([st.session_state.df_data, new_row], ignore_index=True)
                
                st.balloons()
                st.success("🎉 Vos réponses ont été transmises avec succès !")
                st.divider()
                st.markdown(f"## 📋 Votre Profil d'Apprentissage, {nom}")
                
                if score_c <= 2.5:
                    st.info("💡 **Organisation :** La comptabilité exige de la rigueur. Utilisez des checklists.")
                else:
                    st.success("💡 **Rigueur :** Excellente capacité de concentration naturelle.")
                if score_e <= 2.5:
                    st.info("💡 **Style :** Vous êtes calme. Privilégiez la réflexion individuelle.")
                else:
                    st.success("💡 **Style :** Vous êtes dynamique. Participez aux simulations.")

# ==========================================
# 🔐 Partie II : Tableau de Bord Formateur
# ==========================================
elif page == "🔐 Tableau de Bord Formateur (الاستراتيجيات)":
    st.title("🔐 Espace d'Ingénierie Pédagogique - Rentrée 2026-2027")
    password = st.text_input("Code d'accès secret :", type="password")
    
    if password == "CMC_Nador_2026":
        st.success("🔓 Accès autorisé.")
        df = st.session_state.df_data
        
        if df.empty:
            st.info("📂 Aucune donnée disponible pour le moment.")
        else:
            niveau_select = st.selectbox("Sélectionnez le groupe:", ["1ère année Tronc Commun", "2ème année TSGEOCF", "3ème année TSGEOCF"])
            df_filtered = df[df["Niveau"] == niveau_select]
            
            if df_filtered.empty:
                st.warning("Aucun stagiaire dans ce niveau.")
            else:
                moy_e = df_filtered["Extraversion"].mean()
                moy_c = df_filtered["Conscientiousness"].mean()
                moy_n = df_filtered["Neuroticism"].mean()
                moy_o = df_filtered["Openness"].mean()
                
                st.metric("Effectif diagnostiqué", len(df_filtered))
                st.divider()
                
                st.markdown("### 🚨 Système d'Alerte Précoce : Profils à Risque")
                for idx, row in df_filtered.iterrows():
                    if row['Agreeableness'] <= 2.5 and row['Extraversion'] >= 3.5:
                        st.error(f"🔴 **Risque de conflit direct :** {row['Nom Complet']} ({row['Groupe']})")
                    if row['Openness'] >= 4.0 and row['Conscientiousness'] <= 2.2:
                        st.warning(f"🔶 **Risque d'indiscipline :** {row['Nom Complet']} ({row['Groupe']})")
                    if row['Extraversion'] <= 2.0 and row['Neuroticism'] >= 4.0:
                        st.info(f"⚠️ **Risque de décrochage :** {row['Nom Complet']} ({row['Groupe']})")
                
                st.divider()
                st.markdown("### 🎯 Stratégie Pédagogique Globale")
                if "2ème année" in niveau_select:
                    st.write("• **Pratique de la paie & Comptabilité Approfondie :** Utilisez le *Micro-learning* si la rigueur globale est faible.")
                    st.write("• **Bureautique Avancée :** Intégrez la *Gamification* (Défis Excel).")
                elif "3ème année" in niveau_select:
                    st.write("• **Audit & Télédéclarations :** Appliquez l'*Erreur Apprenante* sur plateforme sandbox.")
                    st.write("• **Normes IAS/IFRS :** Utilisez la *Classe Inversée*.")
                
                st.divider()
                st.dataframe(df_filtered)
                csv_data = df_filtered.to_csv(index=False).encode('utf-8-sig')
                st.download_button(label="📥 Télécharger la base", data=csv_data, file_name="Diagnostique.csv")
