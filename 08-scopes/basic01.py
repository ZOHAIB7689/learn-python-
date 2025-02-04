# Global scope
global_var = "I'm a global variable"

def outer_function():
    # Enclosing scope
    outer_var = "I'm in the outer function"
    
    def inner_function():
        # Local scope
        local_var = "I'm a local variable"
        print(local_var)  # Can access local
        print(outer_var)  # Can access enclosing
        print(global_var) # Can access global
    
    inner_function()

# Call the function
outer_function()