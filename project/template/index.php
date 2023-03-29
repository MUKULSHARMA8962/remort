<?php

$data = array('key1' => 'value1', 'key2' => 'value2');
$url = 'http://localhost:8000/process_data/';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
$response = curl_exec($ch);
curl_close($ch);

if ($response) {
    $response_data = json_decode($response, true);
    if ($response_data['status'] == 'success') {
        echo $response_data['message'];
    } else {
        echo 'Error: ' . $response_data['message'];
    }
} else {
    echo 'Error connecting to API.';
}
