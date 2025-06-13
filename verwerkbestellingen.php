<?php
require_once('../db_config.php');
 
$kamer = $_POST['kamer'] ?? '';
$gerecht = $_POST['gerecht'] ?? '';
$aantal = $_POST['aantal'] ?? 1;
$opmerkingen = $_POST['opmerkingen'] ?? '';
 
$sql = "INSERT INTO bestellingen (kamer_nummer, gerecht, aantal, opmerkingen)
        VALUES (:kamer, :gerecht, :aantal, :opmerkingen)";
$stmt = $pdo->prepare($sql);
$stmt->execute([
    ':kamer' => $kamer,
    ':gerecht' => $gerecht,
    ':aantal' => $aantal,
    ':opmerkingen' => $opmerkingen
]);
 
echo "<h2>Bestelling ontvangen!</h2><a href='../index.html'>Terug naar formulier</a>";
