
import functools

user = {"username": "Rob", "access_level": "admin"}

def make_secure(func):
    # print(func.__code__.co_argcount)
    # @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin access for {user['username']}."
    return secure_function

@make_secure
def get_admin_passwd():
    """This is get_admin_passwd"""
    return "1234"

# get_admin_passwd = make_secure(get_admin_passwd)

print(get_admin_passwd())
print(get_admin_passwd.__name__)
print(get_admin_passwd.__doc__)

print("Hello this is for GIT")
print("Hello this is for GITDemo")

"""
def outer_function(x):
    # Hidden from the outer code
    def inner_increment(y):
        print("calling..inner func")
        return x(y)
    print("Calling...outer func")
    return inner_increment

# @outer_function
# calc = outer_function(calc)
def calc(y):
    print("I am calc....\n", y)


# calc = outer_function(calc)
# calc("GOOD")



funct_return = outer_function(calc)
funct_return("GOOD")
"""
