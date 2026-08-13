<?php

$idade = $_GET['idade'];

if ($idade < 18) {
    echo "Menor de idade";
} else {
    echo "Maior de idade";
}

?>