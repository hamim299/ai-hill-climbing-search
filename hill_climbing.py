def hill_climbing(function, start, step=0.01, max_iterations=1000):
    current = start

    for _ in range(max_iterations):
        current_value = function(current)

        left = current - step
        right = current + step

        left_value = function(left)
        right_value = function(right)

        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break

    return current, function(current)


def objective_function(x):
    return -(x - 3) ** 2 + 9


start_point = 0

best_position, best_value = hill_climbing(
    objective_function,
    start_point
)

print("Best Position:", best_position)
print("Maximum Value:", best_value)