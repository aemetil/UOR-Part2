      
    // Exercice 6.1 : Bouton retour en haut de la page 
     // afficher/masquer le bouton retour en haut
        window.onscroll = function() {
            var btn = document.querySelector('.retour-haut');
            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                btn.style.display = "block";
            } else {
                btn.style.display = "none";
            }
        };