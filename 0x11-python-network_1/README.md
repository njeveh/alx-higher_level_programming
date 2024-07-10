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
### 6-post_email.py
> A Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
>> - The email is sent in the variable email
>> - Uses the packages requests and sys
>> - Does not import packages other than requests and sys
### 7-error_code.py
> A Python script that takes in a URL, sends a request to the URL and displays the body of the response.
>> - If the HTTP status code is greater than or equal to 400, prints: Error code: followed by the value of the HTTP status code
>> - Uses the packages requests and sys
>> - Does not import packages other than requests and sys
### 8-json_api.py
> A Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
>> - The letter is sent in the variable q
>> - If no argument is given, it sets q=""
>> - If the response body is properly JSON formatted and not empty, it displays the id and name like this: [<id>] <name>
Otherwise: it Displays Not a valid JSON if the JSON is invalid
>> - Displays No result if the JSON is empty
>> - Uses the packages requests and sys
>> - Does not import packages other than requests and sys
### 10-my_github.py
> A Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
>> - Uses Basic Authentication with a personal access token as password to access to your information (only read:user permission is needed)
>> - The first argument is your username
>> - The second argument is your password (in your case, a personal access token as password)
>> - Uses the packages requests and sys
>> - Does not import packages other than requests and sys
### 100-github_commits.py
> A Python script that list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
>> - The first argument is the repository name
>> - The second argument is the owner name
>> - Uses the packages requests and sys
>> - Does not import packages other than requests and sys