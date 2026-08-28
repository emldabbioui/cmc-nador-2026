import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="CMC Nador - Évaluation Diagnostique 2026-2027", page_icon="🧠", layout="wide")

DATA_FILE = "cmc_diagnostique_2026.csv"
if not os.path.exists(DATA_FILE):
    df_empty = pd.DataFrame(columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])
    df_empty.to_csv(DATA_FILE, index=False, encoding='utf-8-sig')

page = st.sidebar.radio("Navigation / التنقل:", ["📝 Espace Stagiaire (التقويم التشخيصي)", "🔐 Tableau de Bord Formateur (الاستراتيجيات)"])

if page == "📝 Espace Stagiaire (التقويم التشخيصي)":
    st.title("📊 CMC Nador - Évaluation Diagnostique (Rentrée 2026-2027)")
    st.subheader("Filière: Finance et Comptabilité (GEOCF)")
    st.write("Bienvenue cher(e) stagiaire. Ce test scientifique évalue votre style de réflexion afin de vous proposer des conseils pédagogiques et professionnels personnalisés.")
    
    with st.form("diagnostique_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            nom = st.text_input("Nom et Prénom (الاسم الكامل):")
        with col2:
            niveau = st.selectbox("Votre Niveau Actuel (مستواك الحالي):", 
                                  ["1ère année Tronc Commun", "2ème année TSGEOCF", "3ème année TSGEOCF"])
        with col3:
            groupe = st.text_input("Groupe / Section (الفوج):")
            
        st.divider()
        st.write("📌 Évaluez de 1 (Pas du tout d'accord) à 5 (Tout à fait d'accord) :")
        
        st.markdown("### 🗣️ Extraversion (التفاعل والتواصل)")
        q1 = st.slider("1. Dans un groupe, je prends facilement la parole et j'aime débattre à voix haute pour résoudre un problème.", 1, 5, 3)
        q2 = st.slider("2. Je préfère travailler seul sur un projet complexe et je me sens vite fatigué par les discussions collectives prolongées.", 1, 5, 3)
        
        st.markdown("### 🤝 Agreeableness (التعاون والانسجام)")
        q3 = st.slider("3. J'éprouve un réel plaisir à expliquer une notion difficile à un camarade qui ne l'a pas comprise.", 1, 5, 3)
        q4 = st.slider("4. Je pense que chacun doit se débrouiller seul pour réussir, et je n'aime pas que les autres freinent mon rythme.", 1, 5, 3)
        
        st.markdown("### 🎯 Conscientiousness (الدقة، التنظيم والمسؤولية)")
        q5 = st.slider("5. Je suis très pointilleux avec les chiffres et les détails ; une simple erreur d'inattention me dérange beaucoup.", 1, 5, 3)
        q6 = st.slider("6. J'improvise souvent et je préfère commencer à travailler directement plutôt que de perdre du temps à planifier.", 1, 5, 3)
        
        st.markdown("### ⚖️ Neuroticism (الاستجابة للضغوط والمواقف المفاجئة)")
        q7 = st.slider("7. Je perds facilement mes moyens ou je stresse énormément face à un exercice inconnu ou une consigne floue.", 1, 5, 3)
        q8 = st.slider("8. Je garde mon calme et mon sang-froid même lorsque la situation devient confuse ou que le temps presse.", 1, 5, 3)
        
        st.markdown("### 💡 Openness (الفضول الفكري والابتكار)")
        q9 = st.slider("9. J'adore explorer de nouveaux outils numériques (Logiciels, IA, Applications) et chercher des solutions originales.", 1, 5, 3)
        q10 = st.slider("10. Je préfère les méthodes d'apprentissage traditionnelles et claires, et je me méfie des changements trop rapides.", 1, 5, 3)

        submitted = st.form_submit_button("Envoyer et Voir mes Résultats 🚀")
        
        if submitted:
            if not nom or not groupe:
                st.error("❌ Veuillez remplir impérativement les champs Nom et Groupe.")
            else:
                score_e = (q1 + (6 - q2)) / 2
                score_a = (q3 + (6 - q4)) / 2
                score_c = (q5 + (6 - q6)) / 2
                score_n = (q7 + (6 - q8)) / 2
                score_o = (q9 + (6 - q10)) / 2
                
                new_row = pd.DataFrame([[nom, niveau, groupe, score_e, score_a, score_c, score_n, score_o]], 
                                        columns=["Nom Complet", "Niveau", "Groupe", "Extraversion", "Agreeableness", "Conscientiousness", "Neuroticism", "Openness"])
                new_row.to_csv(DATA_FILE, mode='a', header=False, index=False, encoding='utf-8-sig')
                
                st.balloons()
                st.success(f"🎉 Vos réponses ont été transmises avec succès !")
                
                st.divider()
                st.markdown(f"## 📋 Votre Profil d'Apprentissage, {nom}")
                
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    st.markdown("### 🎓 Conseils Pédagogiques (Comment étudier efficacement) :")
                    if score_c <= 2.5:
                        st.info("💡 **Organisation :** Vous préférez la flexibilité, mais la comptabilité exige de la rigueur. Pour réussir vos modules, apprenez à utiliser des checklists étape par étape pour réviser et valider vos bilans.")
                    else:
                        st.success("💡 **Rigueur :** Vous avez une excellente capacité de concentration naturelle. Profitez-en pour aborder des études de cas complexes de manière autonome.")
                    
                    if score_e <= 2.5:
                        st.info("💡 **Style d'apprentissage :** Vous êtes de nature calme et analytique. Privilégiez d'abord la compréhension individuelle des exercices avant de participer aux travaux de groupe.")
                    else:
                        st.success("💡 **Style d'apprentissage :** Vous êtes dynamique et communicatif. Boostez votre apprentissage en participant activement aux simulations d'entreprise et aux débats en classe.")
                        
                with col_res2:
                    st.markdown("### 💼 Conseils Professionnels (Pour votre avenir en Finance) :")
                    if score_o >= 3.5:
                        st.success("🎯 **Atout Métier :** Votre grande curiosité intellectuelle est parfaite pour les métiers stratégiques comme l'**Audit comptable** ou le **Conseil fiscal**, où l'innovation et l'analyse globale sont clés.")
                    else:
                        st.info("🎯 **Atout Métier :** Vous préférez la clarté et la stabilité. Vous excellerez dans les rôles de **Gestion de la Paie** ou de **Comptabilité pure (PCM)**, où le respect des procédures strictes est indispensable.")
                        
                    if score_n >= 3.5:
                        st.warning("⚠️ **Gestion du Stress :** Le monde de la finance connaît des périodes intenses (périodes d'inventaire, clôtures fiscales). Entraînez-vous dès maintenant à gérer les délais courts pour ne pas perdre vos moyens lors de votre future insertion professionnelle.")

elif page == "🔐 Tableau de Bord Formateur (الاستراتيجيات)":
    st.title("🔐 Espace d'Ingénierie Pédagogique - Rentrée 2026-2027")
    
    password = st.text_input("Code d'accès secret :", type="password")
    
    if password == "CMC_Nador_2026":
        st.success("🔓 Accès autorisé. Modèles de prédiction comportementale actifs.")
        df = pd.read_csv(DATA_FILE, encoding='utf-8-sig')
        
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
                moy_a = df_filtered["Agreeableness"].mean()
                moy_c = df_filtered["Conscientiousness"].mean()
                moy_n = df_filtered["Neuroticism"].mean()
                moy_o = df_filtered["Openness"].mean()
                
                col_m1, col_m2, col_m3, col_m4 = st.columns(4)
                with col_m1: st.metric("Effectif diagnostiqué", len(df_filtered))
                with col_m2: st.metric("Rigueur Globale (C)", round(moy_c, 2))
                with col_m3: st.metric("Résistance au Stress", round(6 - moy_n, 2))
                with col_m4: st.metric("Agilité Numérique / Ouverture (O)", round(moy_o, 2))
                
                st.divider()
                st.markdown("### 🚨 Système d'Alerte Précoce : Profils à Risque de Conflit ou de Blocage")
                
                alerts_found = False
                for idx, row in df_filtered.iterrows():
                    reasons = []
                    if row['Agreeableness'] <= 2.5 and row['Extraversion'] >= 3.5:
                        reasons.append("🔴 **Risque de conflit direct :** Forte extraversion combinée à une faible amabilité. Ce stagiaire peut chercher à imposer ses idées de manière agressive lors des travaux d'équipe (ex: Simulations, Audit) et créer des tensions.")
                    if row['Openness'] >= 4.0 and row['Conscientiousness'] <= 2.2:
                        reasons.append("🔶 **Risque d'indiscipline / Non-respect des règles :** Esprit très libre mais très désorganisé. Risque de refuser de suivre les règles rigides du Plan Comptable Marocain ou des téléprocédures.")
                    if row['Extraversion'] <= 2.0 and row['Neuroticism'] >= 4.0:
                        reasons.append("⚠️ **Risque de décrochage caché (Vulnerability) :** Très introverti et extrêmement sensible au stress. Risque de s'effondrer psychologiquement face aux évaluations complexes sans oser demander de l'aide.")
                    
                    if reasons:
                        alerts_found = True
