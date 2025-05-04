import streamlit as st

# Configuration générale de la page
st.set_page_config(page_title="Morphoz - Relooking", layout="wide")


# CSS pour personnaliser les boutons de la sidebar (Avec Chat GPT)
st.markdown("""
    <style>
        .sidebar-title {
            font-size: 24px;
            color: #9575CD;
            margin-bottom: 20px;
        }

        div.stButton > button {
            background-color: #9575CD;
            color: white;
            width: 100%;
            margin: 5px 0;
            border: none;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
        }

        div.stButton > button:hover {
            background-color: #7E57C2; 
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Initialiser l'etat
if 'page' not in st.session_state:
    st.session_state.page = "Accueil"

# Menu personnalisé
st.sidebar.markdown('<div class="sidebar-title">Menu</div>', unsafe_allow_html=True)

pages = [
    "Accueil", 
    "À propos de nous", 
    "Nos services", 
    "Nous rejoindre", 
    "Contact", 
]

for p in pages:
    if st.sidebar.button(p):
        st.session_state.page = p

# Page active
option = st.session_state.page

# Page d'accueil personnalisée
if option == "Accueil":
    st.title("Le sur-mesure à votre image avec Morphoz")
    st.write("Chez nous, chaque détail compte. Découvrez comment nos experts en relooking, en bien-être et en accompagnement personnalisé peuvent transformer votre quotidien. " \
    "Explorez nos services, laissez-vous inspirer par les avant/après et trouvez la version de vous-même qui vous correspond le mieux.")
    st.image("https://www.academy-inyourstyle.com/wp-content/uploads/2025/01/InYourStyleAcademy-HD-Couleurs-8888-1-scaled.jpg", width=700)
    st.markdown("### Vous voulez tenter l’expérience ?")
    st.write("Cliquez sur le questionnaire suivant pour démarrer votre transformation.")
    #On utilise un markdown plutôt qu'un bouton par soucis de taille
    st.markdown(
    """
    <a style="display:inline-block; padding:10px 20px; font-size:16px; background-color:#7E57C2; color:white; 
              border:none; border-radius:5px; text-decoration:none;">
        Remplir le questionnaire
    </a>
    """,
    unsafe_allow_html=True
)


# À propos de nous
elif option == "À propos de nous":
    st.title("À propos de nous")
    st.write("MORPHOZ est une entreprise internationale spécialisée dans le relooking sur-mesure, alliant expertise, respect des cultures et innovation. "
         "Nos équipes travaillent ensemble pour vous offrir des recommandations uniques, adaptées à vos goûts et aux tendances locales. "
         "Nous croyons que le style est avant tout une expression de soi.")
    st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YnVpbGRpbmd8ZW58MHx8MHx8fDA%3D", width=700)

# Nos services
elif option == "Nos services":
    st.title("Nos services")
    st.write("Un accompagnement complet, pensé pour vous.")
    
    # Création 4 colonnes pour mettre en parallèle
    col1, col2, col3, col4 = st.columns(4)

    # Création des 4 services
    with col1:
        st.write("Conseil vestimentaire personnalisé.")

    with col2:
        st.write("Maquillage et coiffure adaptés.")

    with col3:
        st.write("Coaching bien-être et confiance en soi.")

    with col4:
        st.write("Analyse des tendances locales.")


    # URLs des images
    img1 = "https://www.imagenouvelle.fr/wp-content/uploads/2012/03/RELOOKING-VESTIMENTAIRE-POUR-ELLE-1-e1613727850607.jpg"
    img2 = "https://www.imagenouvelle.fr/wp-content/uploads/2012/03/RELOOKING-MAQUILLAGE-1.jpg"
    img3 = "https://a.storyblok.com/f/97382/2000x1500/4c15e1224b/cover-benefits-of-yoga-and-meditation.png"
    img4 = "https://i.pinimg.com/originals/55/82/cb/5582cbac3d29448c12c3b1c934da8146.jpg"

    # Création 4 colonnes pour mettre en parallèle
    col5, col6, col7, col8 = st.columns(4)
    
    # Création des 4 images
    with col5:
        st.image(img1, width=350)

    with col6:
        st.image(img2,  width=350)

    with col7:
        st.image(img3,  width=350)

    with col8:
        st.image(img4,  width=350)


    st.write("Nos experts vous guident pas à pas pour révéler tout votre potentiel.")


# Nous rejoindre
elif option == "Nous rejoindre":
    st.title("Nous rejoindre")
    st.write("Irejoignez l’aventure MORPHOZ. " \
    "Vous êtes passionné(e) par le style, le bien-être ou l’innovation ?"
    "Devenez membre de notre équipe internationale et contribuez à révéler le style unique de nos clients partout dans le monde." 
    "Consultez nos offres ou déposez votre candidature spontanée dès aujourd’hui !")
    #On utilise un markdown plutôt qu'un bouton par soucis de taille
    st.markdown(
    """
    <a style="display:inline-block; padding:10px 20px; font-size:16px; background-color:#7E57C2; color:white; 
              border:none; border-radius:5px; text-decoration:none;">
        Candidater
    </a>
    """,
    unsafe_allow_html=True
    )
    

# Contact
elif option == "Contact":
    st.title("Contactez-nous")
    
    st.markdown("<h4><strong>Coordonnées</strong></h4>", unsafe_allow_html=True)
    st.markdown("contact@morphoz.com  \n+33 1 99 99 99 99")

    st.markdown("<h4><strong>Adresse physique</strong></h4>", unsafe_allow_html=True)
    st.markdown("1 rue Jean Jaures \n75001 Paris, France")

    #On utilise un markdown plutôt qu'un bouton par soucis de taille
    st.markdown(
    """
    <a style="display:inline-block; padding:10px 20px; font-size:16px; background-color:#7E57C2; color:white; 
              border:none; border-radius:5px; text-decoration:none;">
        Prendre Rendez-vous
    </a>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<h4><strong>Suivez-nous aussi sur les réseaux sociaux</strong></h4>", unsafe_allow_html=True)
    # Configuration des logos RS (avec Chat GPT)
    st.markdown("""
    <style>
        .social-icons {
            display: flex;
            gap: 20px;
            margin-top: 30px;
        }
        .social-icons a img {
            width: 32px;
            height: 32px;
            transition: transform 0.2s ease;
        }
        .social-icons a img:hover {
            transform: scale(1.2);
        }
    </style>

    <div class="social-icons">
        <a href="https://www.instagram.com" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e7/Instagram_logo_2016.svg" alt="Instagram">
        </a>
        <a href="https://www.facebook.com" target="_blank">
            <img src="https://get-picto.com/wp-content/uploads/2023/08/logo-facebook-blanc-420x420.webp" alt="Facebook">
        </a>
        <a href="https://twitter.com" target="_blank">
            <img src="https://static.vecteezy.com/system/resources/previews/042/148/611/non_2x/new-twitter-x-logo-twitter-icon-x-social-media-icon-free-png.png" alt="X">
        </a>
    </div>
""", unsafe_allow_html=True)
    
