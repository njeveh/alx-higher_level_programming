## 0x13-javascript_objects_scopes_closures project files
### 0-rectangle.js
> An empty class Rectangle that defines a rectangle.
### 1-rectangle.js
> A class Rectangle that defines a rectangle:

>> - The constructor takes 2 arguments w and h,
>> - Initializes the instance attribute width with the value of w,
>> - Initializes the instance attribute height with the value of h.
### 2-rectangle.js
> A class Rectangle that defines a rectangle.
>> - The constructor takes 2 arguments w and h,
>> - Initializes the instance attribute width with the value of w,
>> - Initialize the instance attribute height with the value of h,
>> - If w or h is equal to 0 or not a positive integer, it creates an empty object.
### 3-rectangle.js
> A class Rectangle that defines a rectangle.
>> - The constructor takes 2 arguments w and h,
>> - Initializes the instance attribute width with the value of w,
>> - Initialize the instance attribute height with the value of h,
>> - If w or h is equal to 0 or not a positive integer, it creates an empty object,
>> - Has an instance method called print() that prints the rectangle using the character X.
### 4-rectangle.js
> A class Rectangle that defines a rectangle.
>> - The constructor takes 2 arguments w and h,
>> - Initializes the instance attribute width with the value of w,
>> - Initialize the instance attribute height with the value of h,
>> - If w or h is equal to 0 or not a positive integer, it creates an empty object,
>> - Has an instance method called print() that prints the rectangle using the character X,
>> - Has an instance method called rotate() that exchanges the width and the height of the rectangle,
>> - Has an instance method called double() that multiples the width and the height of the rectangle by 2.
### 5-square.js
> A class Square that defines a square and inherits from Rectangle of 4-rectangle.js
>> - The constructor takes 1 argument: size,
>> - The constructor of Rectangle is called (by using super()).
### 6-square.js
> A class Square that defines a square and inherits from Square of 5-square.js.
>> - Has an instance method called charPrint(c) that prints the rectangle using the character c,
>>> - If c is undefined, the character X is used.
### 7-occurrences.js
> A function that returns the number of occurrences in a list:
>> Prototype: exports.nbOccurences = function (list, searchElement).
### 8-esrever.js
> A function that returns the reversed version of a list:
>> Prototype: exports.esrever = function (list).
>> - Does not use the built-in method reverse.
### 9-logme.js
> A function that prints the number of arguments already printed and the new argument value.
>> Prototype: exports.logMe = function (item).
>> Output format: <number arguments already printed>: <current argument value>.