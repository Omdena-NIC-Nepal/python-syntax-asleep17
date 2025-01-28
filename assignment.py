def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old."

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
         return "Greater"
    elif number < 10:
         return "Lesser"
    else : 
     return "Equal"
 
  

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum=0
    for i in range(1,n+1):
        sum+=i 

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    for num in range(numbers):
        sum+=num
    
    max=numbers[0]
    for num in range(numbers):
        if num > max:
            max = num
    
    min=numbers[0]
    for num in range(numbers):
        if num<min:
            min=num
    
    return (sum,max,min)

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    students_above_80=[]
    for students , score in students_dict.items():
        if score > 80:
            students_above_80.append(students)
    return students_above_80

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements=[]
    for elements in list1:
        if elements in list2:
            common_elements.add(elements)
    return common_elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    sum = a+b
    difference = a-b
    product = a*b
    if b!=0:
        quotient=a/b

    return sum,difference,product,quotient

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    And=x and y
    Or=x or y
    not_x=not x
    return And,Or,not_x

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    And= a & b
    Or = a | b
    Xor = a ^ b
    return And,Or,Xor