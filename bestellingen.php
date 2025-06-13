<?php
require_once('../db_config.php');
$stmt = $pdo->query("SELECT * FROM bestellingen ORDER BY besteld_op DESC");
$bestellingen = $stmt->fetchAll();
?>
 
<!DOCTYPE html>
<html>
<head>
<title>Bestellingen Overzicht</title>
<style>
        body { font-family: sans-serif; margin: 2rem; }
        table { border-collapse: collapse; width: 100%; }
        th, td { padding: 8px 12px; border: 1px solid #ddd; }
        th { background-color: #f4f4f4; }
</style>
</head>
<body>
<h1>Overzicht van Bestellingen</h1>
<table>
<tr>
<th>Kamer</th>
<th>Gerecht</th>
<th>Aantal</th>
<th>Opmerkingen</th>
<th>Besteld op</th>
</tr>
<?php foreach ($bestellingen as $b): ?>
<tr>
<td><?= htmlspecialchars($b['kamer_nummer']) ?></td>
<td><?= htmlspecialchars($b['gerecht']) ?></td>
<td><?= $b['aantal'] ?></td>
<td><?= htmlspecialchars($b['opmerkingen']) ?></td>
<td><?= $b['besteld_op'] ?></td>
</tr>
<?php endforeach; ?>
</table>
</body>
</html>
