<ul class="collection with-header">
    <li class="collection-header"><h5><?php echo($_GET["account"]); $balance = getBalance($data, $_GET["account"]);?>  <span style="zoom:100%;"  data-badge-caption="€" class="new badge <?php if($balance<0){echo("red");}else{echo("green");}?>"><?php echo($balance);?></span></h5></li>

    <?php
        $entries = array_reverse(getEntries($data, $_GET["account"]));

        for($i=0; $i<sizeof($entries); $i++)
        {
    ?>

        <a href="index.php?entry=<?php echo($entries[$i]["id"]);?>" class="collection-item"><?php echo($entries[$i]["name"]);?> <span data-badge-caption="€" class="new badge <?php if($entries[$i]["amount"]<0){echo("red");}else{echo("green");}?>"><?php echo($entries[$i]["amount"]);?></span></a>
    
    <?php
        }
    ?>
</ul>

<div style="position: absolute; bottom: 1em;">
<a href="index.php?entry&new=in&account=<?php echo($entries[0]["account"]);?>" class="waves-effect waves-light btn-large" style="background-color: #4caf50; zoom:90%;"><i class="material-icons left">file_download</i>Einzahlung</a>
</div>
<div style="position: absolute; right: 1em; bottom: 1em;">
<a href="index.php?entry&new=out&account=<?php echo($entries[0]["account"]);?>" class="waves-effect waves-light btn-large" style="background-color: #e83d3d; zoom:90%;"><i class="material-icons left">file_upload</i>Auszahlung</a>
</div>