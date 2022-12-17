<html>

<head>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <title>Diagonal</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <div class="container-form">
    <div class="container-fluid">
      <h3>Enter your size</h3>
      <form action="index.php" method="POST">
        <div class="form-group">
          <input name="size" type="text" class="form__input" pattern="[0-9]+" required>
          <span class="icon"></span>
        </div>
      </form>
      <p>Size must be integer</p>
    </div>
    <br><br>
    <div class="container-fluid">
      <div class="table-wrapper">
        <div class="table-title">
          <div class="row">
            <div class="col-sm-6">
              <h2>Given<b> Array</b></h2>
            </div>
          </div>
        </div>
        <table class="table table-striped">
          <tbody>
            <?php
              if (isset($_POST['size'])) {
                $connection = curl_init();
                curl_setopt_array($connection, array(
                CURLOPT_URL => 'http://nginxserver/api/?size=' . $_POST['size'],
                CURLOPT_RETURNTRANSFER => true,
                CURLOPT_HEADER => false,
                )
                );
                $response = curl_exec($connection);
                curl_close($connection);
                $json = json_decode($response);
                $array = $json->massiv;
                $diagonal1 = $json->diagonal;
                foreach ($array as $value) {
                  echo "<tr>";
                  $numbers = explode(" ", $value, $_POST['size']);
                  foreach ($numbers as $number) {
                    echo "<td>" . $number . "</td>";
                  }
                  echo "</tr>";
                }
              }
              ?>
          </tbody>
        </table>
      </div>
      <div class="table-wrapper">
        <div class="table-title">
          <div class="row">
            <div class="col-sm-6">
              <h2>Result</h2>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-6">
            <?php
            echo "<h2>" . $diagonal1 . "</h2>";
            ?>
          </div>
        </div>
      </div>
    </div>
  </div>
</body>

</html>