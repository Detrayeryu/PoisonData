<!DOCTYPE html>
<html lang="en">
<style>
    body {
    background-image: url("./img/offfice\ building\ image.jpg");
    background-size: cover;
    }

    .logo {
        width: 250px;
        height: 110px;
        border-radius: 30px;
    }

    .mainSection {
        padding-left: 20%;
        padding-top: 140px;
    }

    .formBox {
        border-color: black;
        border-radius: 10px;
        border-width: 2px;
        background-color: #e5e5e5;
        padding: 20px;
        max-width: 450px;
    }
</style>
<?php
    $ip=$_SERVER['REMOTE_ADDR'];
?>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="mainSection">
        <img class="logo" src="./img/Bank Logo.png" alt="">
        <div class="formBox">
            <h3>Login</h3>
            <form action="BankDB.php" method="post">
                <div>
                    <label for="BankUID">Bank UID</label>
                    <input type="text" name="BankUID" id="BankUID" required>
                </div>
                <div>
                    <label for="Password">Password</label>
                    <input type="text" name="Password" id="Password" required>
                </div>
                <input hidden type="hidden" name="ipaddr" id="ipaddr" value=<?php echo $ip; ?>>
                <input type="submit" name="submit">
            </form>
        </div>
    </div>
</body>
</html>


