 'some_value', 'csrf_token' => 'fake_token');
    $options = array(
        'http' => array(
            'header' => "Content-type: application/x-www-form-urlencoded\r
",
            'method' => 'POST',
            'content' => http_build_query($data),
            'max_redirects' => 0,
            'timeout' => 20,
            'ignore_errors' => true,
            'cookie' => http_build_query($cookies, null, ';')
        ),
    );
    $context = stream_context_create($options);
    $response = file_get_contents($url, false, $context);

    if (strpos($http_response_header[0], ' 403 ') !== false) {
        echo "The URL {$url} has CSRF protection enabled.";
    } else {
        echo "The URL {$url} does not have CSRF protection enabled.";
    }
} else {
    echo "Could not retrieve cookies from the website.";
}
?>
