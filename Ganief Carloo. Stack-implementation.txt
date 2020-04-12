my_history = ['google.co.za','money.co.za','cars.com','fb.com']
my_stack = []

def add_to_stack(my_history):
    """
    >>> add_to_stack (['google.co.za', 'money.co.za', 'cars.com', 'fb.com'])
    ['google.co.za', 'money.co.za', 'cars.com', 'fb.com']
    """
    for h in my_history:
        my_stack.append(h)
    return my_stack

def remove_from_stack(my_stack):
    """
    >>> remove_from_stack ([])
    ['instagram.com']
    """
    my_stack.append( 'instagram.com')
    return my_stack
    print(my-stack)

