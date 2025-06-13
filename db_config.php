<?php
$host = 'localhost';
$db   = 'roomservice';
$user = 'root';
$pass = ''; // vaak leeg bij XAMPP/MAMP
$charset = 'utf8mb4';
 
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
];
 
try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    die("Databaseverbinding mislukt: " . $e->getMessage());
}
