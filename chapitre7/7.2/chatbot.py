# =============================================================================
# Nom ......... : chatbot.py
# Rôle ........ : Mini-chatbot interactif capable de dialoguer avec un utilisateur
#                  et de répondre aux salutations et questions simples du quotidien
# Auteur ...... : Alberto, EMETIL
# Version ..... : V1.0 du 20/07/2024
# Licence ..... : Réalisé dans le cadre de l'exercice 7.2 "Mini-Projet Chatbot"
#                 du cours de l'"IF"
# Langage ..... : Python 3.11
# Framework ... : Streamlit pour l'interface web
# Exécution ... : streamlit run chatbot.py
# Dépendances . : pip install streamlit
# ================================================================================

import streamlit as st
import random
from datetime import datetime
import time

# configuration de la page Streamlit
st.set_page_config(
    page_title="Mini-Chatbot",
    page_icon="🤖",
    layout="centered"
)

# classe principale du chatbot qui gère les réponses aux différentes questions
class MiniChatbot:
    def __init__(self):
        #dictionnaire des salutations
        self.salutations = {
            'bonjour': [
                "Bonjour! Comment allez-vous aujourd'hui?",
                "Salut! Que puis-je faire pour vous?",
                "Bonjour! Ravi de vous parler!"
            ],
            'bonsoir': [
                "Bonsoir! J'espère que vous avez passé une bonne journée!",
                "Bonsoir! Comment puis-je vous aider ?",
                "Bonne soirée! Que voulez-vous savoir ?"
            ],
            'salut': [
                "Salut! Ça va bien?",
                "Hey! Comment ça se passe?",
                "Salut! Ravi de vous voir!"
            ]
        }
        
        # dictionnaire des questions & réponses
        self.questions_reponses = {
            'nom': [
                "Je m'appelle ChatBot! Et vous?",
                "Mon nom est ChatBot, votre assistant virtuel!"
            ],
            'age': [
                "Je suis né il y a quelques lignes de code!",
                "Je n'ai pas d'âge, je suis un petit programme informatique!"
            ],
            'heure': [
                f"Il est actuellement {datetime.now().strftime('%H:%M:%S')}!"
            ],
            'temps': [
                "Je ne peux pas voir dehors, mais j'espère qu'il fait beau!",
                "Désolé, je n'ai pas accès aux données météo!"
            ],
            'faire': [
                "Je peux répondre à vos questions simples et bavarder avec vous!",
                "Je suis là pour discuter et répondre à des questions simple!"
            ],
            'va': [
                "Ça va très bien, merci! Et vous?",
                "Tout va bien de mon côté! Comment allez-vous?"
            ],
            'revoir': [
                "Au revoir! À bientôt!",
                "Bye! Passez une excellente journée!"
            ]
        }
        
        # réponses par défaut
        self.reponses_defaut = [
            "Je ne comprends pas très bien. Essayez 'bonjour' ou 'comment tu t'appelles'!",
            "Désolé, je ne sais pas répondre à cela. Posez-moi une question simple!",
            "Je n'ai pas de réponse à cela. Que diriez-vous de me dire bonjour?"
        ]
    
    def obtenir_reponse(self, message):
        """
        Obtient une réponse selon le message de l'utilisateur
        """
        # convertir en minuscules pr faciliter la comparaison
        message_bas = message.lower().strip()
        
        # vérifier les salutations
        if 'bonjour' in message_bas:
            return random.choice(self.salutations['bonjour'])
        elif 'bonsoir' in message_bas:
            return random.choice(self.salutations['bonsoir'])
        elif 'salut' in message_bas or 'hello' in message_bas:
            return random.choice(self.salutations['salut'])
        
        # vérifier les questions
        elif 'appelles' in message_bas or 'nom' in message_bas:
            return random.choice(self.questions_reponses['nom'])
        elif 'âge' in message_bas or 'age' in message_bas:
            return random.choice(self.questions_reponses['age'])
        elif 'heure' in message_bas:
            return f"Il est actuellement {datetime.now().strftime('%H:%M:%S')} !"
        elif 'temps' in message_bas or 'météo' in message_bas:
            return random.choice(self.questions_reponses['temps'])
        elif 'faire' in message_bas or 'peux' in message_bas:
            return random.choice(self.questions_reponses['faire'])
        elif 'va' in message_bas and ('comment' in message_bas or 'ça' in message_bas):
            return random.choice(self.questions_reponses['va'])
        elif 'revoir' in message_bas or 'bye' in message_bas:
            return random.choice(self.questions_reponses['revoir'])
        
        # si aucune correspondance
        else:
            return random.choice(self.reponses_defaut)

def main():
    """
    Fonction principale de l'application
    """
    
    # titre
    st.title("Mini-Chatbot")
    st.markdown("### Bienvenue! Dites-moi bonjour pour commencer!")
    
    # initialiser le chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = MiniChatbot()
    
    # initialiser l'historique
    if 'historique' not in st.session_state:
        st.session_state.historique = []
    
   # affichage des exemples de questions
    with st.expander("Exemples de questions que vous pouvez poser"):
        st.markdown("""
        **Salutations :**
        - Bonjour
        - Bonsoir  
        - Salut
        
        **Questions :**
        - Comment tu t'appelles?
        - Quel âge as-tu?
        - Quelle heure est-il?
        - Quel temps fait-il?
        - Que peux-tu faire?
        - Comment ça va?
        - Au revoir
        """)
    
    st.markdown("---")
    
    # zone de saisie
    message = st.text_input("Votre message :", key="message_input")
    
    # traitement du message
    if st.button("Envoyer"):
        if message.strip() != "" :
            # obtenir la réponse
            reponse = st.session_state.chatbot.obtenir_reponse(message)
            #ajouter à l'historique
            st.session_state.historique.append({
                'user': message,
                'bot': reponse,
                'time': datetime.now().strftime('%H:%M:%S')
        })
        else:
            st.warning("Vous devez écrire quelque chose avant d'envoyer.")
    
    # afficher l'historique
    if st.session_state.historique:
        st.markdown("####Conversation")
        
        for chat in reversed(st.session_state.historique):
            # message utilisateur
            st.markdown(f"**Vous ({chat['time']}) :** {chat['user']}")
            # réponse bot
            # un petit delai de la bot
            #time.sleep(1)
            st.markdown(f"**ChatBot :** {chat['bot']}")
            st.markdown("---")
    
    # bouton pr effacer l'historique
    if st.session_state.historique:
        if st.button("Effacer la conversation"):
            st.session_state.historique = []
            st.rerun()
            
            
    # informations sur le projet
    st.markdown("---")
    with st.expander("À propos de ce projet"):
        st.markdown("""
        **Mini-Chatbot - Exercice 7.2(Bonus)**
        
        Ce chatbot simple peut :
        - Répondre aux salutations comme: bonjour, bonsoir, salut
        - Répondre à 7 questions simple prédéfinies
        - Gérer les variations dans les formulations
        - Maintenir un historique des conversations
        
        **Technologies utilisées :**
        - Python 3.11
        - Streamlit pour l'interface web
        """)

# lancement de l'application
if __name__ == "__main__":
    main()
