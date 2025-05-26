# use a snippet plugin or functions.php
# add everything else you need 

add_action('send_headers', function() {
    header("Content-Security-Policy-Report-Only: default-src 'self'; ... ; report-uri https://csp.example.com/csp-violation");
});

# An example from one WordPress

#add_action('send_headers', function() {
#    header("Content-Security-Policy-Report-Only: default-src 'self'; script-src 'self' https://www.youtube.com https://*.googlesyndication.com https://*.google-analytics.com https://*.gstatic.com https://*.googleapis.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data: https:; frame-src https://www.youtube.com; connect-src 'self'; report-uri https://csp.example.com/");
#});
