import http.client
import json

conn = http.client.HTTPSConnection("google.serper.dev")
payload = json.dumps({
  "q": "linux min",
  "gl": "cl"
})
headers = {
  'X-API-KEY': 'b188de1fd3fba0cec09d2bac0fecfe2df122b0a0',
  'Content-Type': 'application/json'
}

conn.request("POST", "/search", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))