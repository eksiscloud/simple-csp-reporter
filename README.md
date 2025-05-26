# simple-csp-reporter
CSP reports will be sended from a site. Flask acts as listening server and publish reports in JSON form to log.

You can test it using this:
```
curl -X POST -H "Content-Type: application/json" \
     -d '{"csp-report": {"document-uri": "https://test", "violated-directive": "script-src", "blocked-uri": "https://evil"}}' \
     https://csp.example.com/csp-violation
```
and then
```
cat /var/log/csp-violation.log
```
