<?php
    if(isset($_GET["new"]))
    {
        $entry = array("name"=>"", "account"=>$_GET["account"], "amount"=>"", "date"=>"", "comment"=>"", "id"=>getNewID($data));
        $new = $_GET["new"];
    }
    else
    {
        $entry = getEntry($data, $_GET['entry']);
        $new = "";
    }
?>

<div class="row">
    <form class="col s12" id="form" method="POST" action="saveEntry.php">
    <input name="id" hidden value="<?php echo($entry["id"]);?>" />
        <div class="row">
            <div class="input-field col s12">
                <input id="name" type="text" class="validate" name="name" value="<?php echo($entry["name"]);?>">
                <label for="name">Name</label>
            </div>
        </div>

        <div class="row">
            <div class="input-field col s12">
                <input type="text" id="autocomplete-input" class="autocomplete" name="account" value="<?php echo($entry["account"]);?>">
                <label for="autocomplete-input">Konto</label>
            </div>
        </div>

        <div class="row">
            <div class="input-field col s6">
                <select name="type">
                    <option value="" disabled>Umsatzart wählen</option>
                    <option value="in" <?php if($entry["amount"]>0||$new=="in"){echo("selected");}?>>Einzahlung</option>
                    <option value="out" <?php if($entry["amount"]<0||$new=="out"){echo("selected");}?>>Auszahlung</option>
                </select>
                <label>Umsatzart</label>
            </div>
            <div class="input-field col s6">
                <input id="amount" type="number" class="validate" name="amount" value="<?php echo(abs($entry["amount"]));?>">
                <label for="amount">Betrag</label>
            </div>
        </div>

        <div class="row">
            <div class="input-field col s12">
                <input type="text" id="date" class="datepicker" name="date" value="<?php echo($entry["date"]);?>">
                <label for="date">Datum</label>
            </div>
        </div>

        <div class="row">
            <div class="input-field col s12">
                <textarea id="textarea1" class="materialize-textarea" name="comment"><?php echo($entry["comment"]);?></textarea>
                <label for="textarea1">Kommentar</label>
            </div>
        </div>

    </form>
  </div>

<div style="position: absolute; bottom: 1em;">
<a href="javascript:history.back()" class="waves-effect waves-light btn-large" style="background-color: #e83d3d; zoom:90%;"><i class="material-icons left">backspace</i>Abbrechen</a>
</div>
<div style="position: absolute; right: 1em; bottom: 1em;">
<a href='deleteEntry.php?id=<?php echo($entry["id"]);?>' class="waves-effect waves-light btn-small" style="background-color: #f00; zoom:90%;"><i class="material-icons">delete</i></a>
<a onclick='document.getElementById("form").submit();' class="waves-effect waves-light btn-large" style="background-color: #4caf50; zoom:90%;"><i class="material-icons left">save</i>Speichern</a>
</div>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('select');
        var instances = M.FormSelect.init(elems, {});
    });

    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('.datepicker');
        var instances = M.Datepicker.init(elems, {"format": "dd.mm.yyyy"});
    });

    $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        <?php
            $allAccounts = getAllAccounts($data);
            for($i=0; $i<sizeof($allAccounts); $i++)
        {
        ?>
            "<?php echo($allAccounts[$i]);?>": null,
        <?php
        }
        ?>
      },
    });
  });

  </script>