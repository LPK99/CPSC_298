import random

# Lambda calculus components
depth_limit = 3  # Limiting depth to control complexity of generated expressions
max_variables = 3  # Maximum index for de Bruijn indices

def generate_variable():
    # Generate a variable as a de Bruijn index, e.g., v1, v2, v3
    return f"v{random.randint(1, max_variables)}"

def generate_abstraction(depth):
    # Generate an abstraction, ensuring it doesn't exceed the depth limit
    if depth < depth_limit:
        body = generate_expression(depth + 1)
        return f"(λ{generate_variable()}.{body})"
    else:
        return generate_expression(depth)

def generate_application(depth):
    # Generate an application, also considering the depth limit
    if depth < depth_limit:
        left = generate_expression(depth + 1)
        right = generate_expression(depth + 1)
        return f"({left} {right})"
    else:
        return generate_expression(depth)

def generate_expression(depth=0):
    # Choose randomly to generate a variable, abstraction, or application
    if depth >= depth_limit:
        # Prevent too deep recursion by choosing a variable at the limit
        return generate_variable()
    choices = ['variable', 'abstraction', 'application']
    choice = random.choice(choices)
    if choice == 'variable':
        return generate_variable()
    elif choice == 'abstraction':
        return generate_abstraction(depth)
    elif choice == 'application':
        return generate_application(depth)

# Generate and print a random lambda calculus expression
random_lambda_expr = generate_expression()
print(f"Random Lambda Calculus Expression: {random_lambda_expr}")
