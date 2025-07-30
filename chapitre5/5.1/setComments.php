<?php
session_start();
include 'bddConnect.php';

// validation des données
if (empty($_POST['nom']) || empty($_POST['prenom']) || empty($_POST['email']) || empty($_POST['commentaires'])) {
    header('Location: index.php?error=empty');
    exit();
}

// validation email
if (!filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
    header('Location: index.php?error=email');
    exit();
}

// conversion du format HTML5 en format MySQL DATETIME
$date = $_POST['date'];
if (!empty($date)) {
    $date = str_replace('T', ' ', $date);
    if (strlen($date) == 16) { // format YYYY-MM-DD HH:MM
        $date .= ':00';
    }
} else {
    $date = date('Y-m-d H:i:s');
}

// prottection contre les injections SQL
$req = $conn->prepare('INSERT INTO testc (nom, prenom, email, date, commentaires) VALUES(:nom, :prenom, :email, :date, :commentaires)');
$req->execute([
    'nom' => htmlspecialchars($_POST['nom']),
    'prenom' => htmlspecialchars($_POST['prenom']),
    'email' => htmlspecialchars($_POST['email']),
    'date' => $date,
    'commentaires' => htmlspecialchars($_POST['commentaires'])
]);

$_SESSION['success'] = "Commentaire publié avec succès !";
header('Location: index.php');
exit();
