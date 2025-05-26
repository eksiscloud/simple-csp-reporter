# use a snippet plugin or functions.php
# add everything else you need 

add_action('send_headers', function() {
    header("Content-Security-Policy-Report-Only: default-src 'self'; ... ; report-uri https://csp.example.com/csp-violation");
});
