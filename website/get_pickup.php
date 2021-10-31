<?php 
require_once("config.php");
if((isset($_POST['your_name'])&& $_POST['your_name'] !='') && (isset($_POST['your_email'])&& $_POST['your_email'] !=''))
{
//  require_once("contact_mail.php:");
 $yourName = $conn->real_escape_string($_POST['your_name']);
 $yourEmail = $conn->real_escape_string($_POST['your_email']);
 $yourPhone = $conn->real_escape_string($_POST['your_phone']);
 $address = $conn->real_escape_string($_POST['address']);
 $gender = $conn->real_escape_string($_POST['gender']);
 //$filename = $_POST['image'];
 date_default_timezone_set('Asia/Calcutta');
 $timestamp = date('Y-m-d H:i:s');

$sql="INSERT INTO users (name, email, phone, address, gender) VALUES ('".$yourName."','".$yourEmail."', '".$yourPhone."', '".$address."','".$gender."')";
 if(!$result = $conn->query($sql)){
 die('There was an error running the query [' . $conn->error . ']');

 }
 else
 {
 echo "Thank you! We will contact you soon";
 }
 }
 else
 {
 echo "Please fill Name and Email";
 }
 ?>
