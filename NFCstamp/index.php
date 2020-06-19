<?php
    $dir = '/home/pi/NAS/Public/Daten/Christoph/NFC_Stempelsystem/';
    $file = $dir.date('Y-m-d').'.csv';

    file_put_contents($file, date('H:i').';'.$_GET['name'], FILE_APPEND);
?>