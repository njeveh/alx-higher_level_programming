## 0x10-python-network_0
### 0-body_size.sh
> A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
>> - The size is displayed in bytes
>> - Uses curl
### 1-body.sh
> A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
>> - Displays only body of a 200 status code response
>> - Uses curl
### 2-delete.sh
> A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
>> - Uses curl
### 3-methods.sh
> A Bash script that takes in a URL as an argument, and displays all HTTP methods the server will accept.
>> - Uses curl
### 4-header.sh
> A Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
>> - A header variable X-School-User-Id must is sent with the value 98
>> - Uses curl
### 5-post_params.sh
> A Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

>> - A variable email is sent with the value test@gmail.com
>> - A variable subject is sent with the value I will always be here for PLD
>> - Uses curl
### 6-peak.py and 6-peak.txt
> A function that finds a peak in a list of unsorted integers.

>> - Prototype: def find_peak(list_of_integers):
>> no modules are imported
>> - Uses an algorithm with the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
>> - 6-peak.py contains the function
>> - 6-peak.txt contains the complexity of the algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
> Note: there may be more than one peak in the list

### 100-status_code.sh
>  A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
>> - Does not use any pipe, redirection, etc.
>> - Does not use ; and &&
>> - Uses curl
### 101-post_json.sh
> A Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
>> - Sends a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
>> - Uses curl
### 102-catch_me.sh
> Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

>> - Uses curl
>> - Does not use echo, cat, etc. to display the final result