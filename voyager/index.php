<?php
    include("functions.php");
?>
<!DOCTYPE html>
  <html>
    <head>
      <!--Import Google Icon Font-->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="css/materialize.min.css"  media="screen,projection"/>

      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
      <script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.4.1.min.js"></script>
    </head>

    <body>

    <nav>
        <div class="nav-wrapper" style="background-color: #039be5;">
        <a href="index.php" class="brand-logo center">Schwering Voyager</a>
        </ul>
        </div>
    </nav>

    <div  style="margin: 1em;">

    <?php
        if(isset($_GET['entry']))
        {
            include("entry.php");
        }
        else if(isset($_GET['account']))
        {
            include("account.php");
        }
        else
        {
            include('account_list.php');
        }
    ?>

    </div>

      <!--JavaScript at end of body for optimized loading-->
      <script type="text/javascript" src="js/materialize.min.js"></script>
    </body>
  </html>