
<?php
# connection à la base de données
try {
  $conn = new PDO('mysql:host=localhost;dbname=test', 'root', 'root');
}
catch (Exception $e){
  die('Erreur : ' .$e->getMessage());
}
?>