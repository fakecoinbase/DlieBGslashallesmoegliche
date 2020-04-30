<?php
include("functions.php");
saveEntry($data, $_POST["id"], $_POST["name"], $_POST["amount"], $_POST["account"], $_POST["date"], $_POST["comment"], $_POST["type"],);
?>

<meta http-equiv="refresh" content="0; URL=index.php?account=<?php echo($_POST['account']);?>">