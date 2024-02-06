Data Jester

Run app.py in /google_extension before starting
import google esxtension file into google chrome refer to this on how to -> https://support.google.com/chrome/a/answer/2714278?hl=en


Current COnfiguration works only for localhost and doesnt create auto report
for auto report, change from spamV3.py to spamV4.py in line 14 in app.py
  >>> subprocess.run(['python', 'spamV4.py', url] + list(map(str, selected_options)))

To test report writing, run /hide/reportWriter.py

Edit data base and extracting of credentials in /google_extension/fakeCred.py
Proxy is now using free proxy which can be outdated, update /google_extension/scrapProxies.py
