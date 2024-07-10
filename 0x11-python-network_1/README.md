## 0x11-python-network_1
### 0-hbtn_status.py
> A Python script that fetches https://alx-intranet.hbtn.io/status
>> - Uses the package urllib
>> - Does not import any packages other than urllib
>> - Uses a with statement
### 1-hbtn_header.py
> A Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
>> - Uses the packages urllib and sys
>> - Does not import any packages other than urllib and sys
>> - Uses a with statement
>> - The value of this variable is different for each request
>> - Arguments passed to the script are not checked (number or type)
### 2-post_email.py
> A Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
>> - The email is sent in the email variable
>> - Uses the packages urllib and sys
>> - Does not import any packages other than urllib and sys
>> - Arguments passed to the script are not checked (number or type)
>> - Uses a with statement
### 3-error_code.py
> A Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
>> - Manages urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
>> - Uses the packages urllib and sys
>> - Does not import any packages other than urllib and sys
>> - Arguments passed to the script are not checked (number or type)
>> - Uses a with statement
### 4-hbtn_status.py
> A Python script that fetches https://alx-intranet.hbtn.io/status

>> - Uses the package requests
>> - Does not import any packages other than requests
### 5-hbtn_header.py
> A Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
>> - Uses the packages requests and sys
>> - Does not import other packages than requests and sys