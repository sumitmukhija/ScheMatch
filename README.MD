#### What?
Basic Python based tool to check schema of two dictionaries

#### Does it check values?
Nope.

#### Does it work if one of the keys is a dictionary itself?
It checks for nested dictionaries. So, yes.

#### What Python version is it based on?
Python 3.7

#### Dependencies?
None.

#### How to use?

1. Import
   ``` from schematch import match ```

2. Prepare input

     ```dicOne = {"name":"Sumit", "likes": "sleeping"}```
    ```dicTwo = {"name":"Shekhar", "likes": "guys"}```

3. Invoke method
    ```are_schemas_same = match.are_keys_same_in_dictionary(dicOne, dicTwo)```

4. Output
    ```(True, '')```

The output is a tuple with a boolean and a string. The boolean determines if the schemas match and the string is the error message (if any)
