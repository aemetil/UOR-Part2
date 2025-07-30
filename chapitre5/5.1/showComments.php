<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- page responsive -->
    <meta name="author" content="Alberto EMETIL">
    <meta name="description" content="La coupe du monde 2022 est la 22e édition de ce tournoi quadriennal. Organisée par la FIFA, elle s'est deroulée au Qatar du 20 novembre au 18 decembre 2022, le jour de la fête nationale.">
    <meta name="keywords" content="coupe du monde, qatar 2022, fifa">
</head>

<body>

    <div class="comment-s">
        <?php if (isset($_GET['error'])): ?>
            <div class="alert alert-danger">
                <?php
                if ($_GET['error'] === 'empty') echo "Tous les champs sont obligatoires";
                if ($_GET['error'] === 'email') echo "Email invalide";
                ?>
            </div>
        <?php endif; ?>

        <?php if (isset($_GET['success'])): ?>
            <div class="alert alert-success">
                Commentaire publié avec succès !
            </div>
        <?php endif; ?>
        <!-- formulaire pr les champs-->
        <form method="POST" action="setComments.php" class="comment-form">
            <div class="row">
                <div class="col-label"><label for="Nomf">Nom</label></div>
                <div class="field"><input type="text" id="Nom" name="nom" placeholder="Entrez votre nom de famille"></div>
            </div>

            <div class="row">
                <div class="col-label"><label for="Prenom">Prénom</label></div>
                <div class="field"><input type="text" id="Prenom" name="prenom" placeholder="Entrez votre prénom"></div>
            </div>

            <div class="row">
                <div class="col-label"><label for="Email">Votre adresse e-mail</label></div>
                <div class="field"><input type="email" id="email" name="email" placeholder="Entrez votre adresse e-mail"></div>
            </div>

            <div class="row-com">
                <div class="col-label"><label for="datetime">Entrez la date et l'heure du jour</label></div>
                <div class="field"><input type="datetime-local" id="datime" name="date"></div>
            </div>

            <div class="row-com">
                <div class="col-label"><label for="commentaire">Commentaires</label></div>
                <div class="field"><textarea id="commentaire" name="commentaires" placeholder="Ajoutez un commentaire..."></textarea></div>
            </div><br>

            <div class="submit-btn">
                <input type="submit" value="Publier">
            </div>
        </form>
    </div>

    <?php
    # connexion à la base de données
    include 'bddConnect.php';

    # récupération de tous les commentaires
    $reponse = $conn->query("SELECT * FROM testc ORDER BY id DESC");

    # affichage
    while ($bddData = $reponse->fetch()) {
        echo "<div class='com-box'><p>";
        echo "<strong>" . strtoupper(htmlspecialchars_decode(htmlspecialchars($bddData['nom'], ENT_QUOTES))) . "</strong> ";
        echo "<strong>" . ucfirst(htmlspecialchars_decode(htmlspecialchars($bddData['prenom'], ENT_QUOTES))) . "</strong>";
        echo "<em>a publié le: " . $bddData['date'] . "</em><br><br>";
        echo "" . ucfirst(nl2br(htmlspecialchars_decode($bddData['commentaires'])));
        echo "</p></div>";
    }
    $reponse->closeCursor();
    ?>

</body>

</html>