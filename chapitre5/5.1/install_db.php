<?php
try {
    // connexion au serveur MySQL
    $pdo = new PDO('mysql:host=localhost', 'root', 'root');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // création de la base si elle n'existe pas
    $pdo->exec("CREATE DATABASE IF NOT EXISTS test CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci");

    // sélection de la base
    $pdo->exec("USE test");

    // creation de la table si elle n'existe pas (automatiquement)
    $pdo->exec("CREATE TABLE IF NOT EXISTS testc (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(100) NOT NULL,
        prenom VARCHAR(100) NOT NULL,
        email VARCHAR(150) NOT NULL,
        date DATETIME NOT NULL,
        commentaires TEXT NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4");

    echo "<p style='color:green;font-size:20px;'>Base et table créées avec succès !</p>";
} catch (PDOException $e) {
    echo "<p style='color:red;font-size:20px;'>Erreur : " . htmlspecialchars($e->getMessage()) . "</p>";
}
