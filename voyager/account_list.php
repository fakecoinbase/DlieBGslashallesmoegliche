<div class="collection">
    <?php
    $allAccounts = getAllAccounts($data);
    for($i=0; $i<sizeof($allAccounts); $i++)
    {
    ?>
    <a href="index.php?account=<?php echo($allAccounts[$i]);?>" class="collection-item"><?php echo($allAccounts[$i]);?></a>
    <?php
    }
    ?>
</div>

<div style="position: absolute; bottom: 1em;">
<a href="index.php?entry&new=in" class="waves-effect waves-light btn-large" style="background-color: #4caf50; zoom:90%;"><i class="material-icons left">file_download</i>Einzahlung</a>
</div>
<div style="position: absolute; right: 1em; bottom: 1em;">
<a href="index.php?entry&new=out" class="waves-effect waves-light btn-large" style="background-color: #e83d3d; zoom:90%;"><i class="material-icons left">file_upload</i>Auszahlung</a>
</div>