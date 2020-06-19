<?php
    $dir = '/home/pi/NAS/Public/Daten/Christoph/NFC_Stempelsystem/';
    $file = $dir.'Stempeldatei.csv';

    file_put_contents($file, date('Y-m-d H:i:s').';'.$_GET['name'].'
', FILE_APPEND);
?>
