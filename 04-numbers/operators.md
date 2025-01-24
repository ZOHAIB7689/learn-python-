# Number Operators in Python

## Arithmetic Operators
Arithmetic operators are used to perform mathematical operations such as addition, subtraction, multiplication, and division.

- **Addition (`+`)**: Adds two operands.
    ```python
    result = 10 + 5  # result is 15
    ```

- **Subtraction (`-`)**: Subtracts the second operand from the first.
    ```python
    result = 10 - 5  # result is 5
    ```

- **Multiplication (`*`)**: Multiplies two operands.
    ```python
    result = 10 * 5  # result is 50
    ```

- **Division (`/`)**: Divides the first operand by the second. The result is a float.
    ```python
    result = 10 / 5  # result is 2.0
    ```

- **Floor Division (`//`)**: Divides the first operand by the second and truncates the result to an integer.
    ```python
    result = 10 // 3  # result is 3
    ```

- **Modulus (`%`)**: Returns the remainder when the first operand is divided by the second.
    ```python
    result = 10 % 3  # result is 1
    ```

- **Exponentiation (`**`)**: Raises the first operand to the power of the second.
    ```python
    result = 2 ** 3  # result is 8
    ```

## Comparison Operators
Comparison operators compare two values and return a boolean result.

- **Equal (`==`)**: Checks if two operands are equal.
    ```python
    result = (10 == 5)  # result is False
    ```

- **Not Equal (`!=`)**: Checks if two operands are not equal.
    ```python
    result = (10 != 5)  # result is True
    ```

- **Greater Than (`>`)**: Checks if the first operand is greater than the second.
    ```python
    result = (10 > 5)  # result is True
    ```

- **Less Than (`<`)**: Checks if the first operand is less than the second.
    ```python
    result = (10 < 5)  # result is False
    ```

- **Greater Than or Equal To (`>=`)**: Checks if the first operand is greater than or equal to the second.
    ```python
    result = (10 >= 5)  # result is True
    ```

- **Less Than or Equal To (`<=`)**: Checks if the first operand is less than or equal to the second.
    ```python
    result = (10 <= 5)  # result is False
    ```

## Complex Numbers
Python supports complex numbers, which are written with a "j" as the imaginary part.

- **Creating Complex Numbers**:
    ```python
    complex_num = 3 + 4j
    ```

- **Accessing Real and Imaginary Parts**:
    ```python
    real_part = complex_num.real  # real_part is 3.0
    imag_part = complex_num.imag  # imag_part is 4.0
    ```

- **Complex Number Operations**:
    - **Addition**:
        ```python
        result = (3 + 4j) + (1 + 2j)  # result is (4 + 6j)
        ```

    - **Subtraction**:
        ```python
        result = (3 + 4j) - (1 + 2j)  # result is (2 + 2j)
        ```

    - **Multiplication**:
        ```python
        result = (3 + 4j) * (1 + 2j)  # result is (-5 + 10j)
        ```

    - **Division**:
        ```python
        result = (3 + 4j) / (1 + 2j)  # result is (2.2 - 0.4j)
        ```

## Complex Number Game
A complex number game can be a fun way to understand operations with complex numbers. Here is a simple example:

### Game Rules
1. Each player chooses a complex number.
2. Players take turns performing operations (addition, subtraction, multiplication, division) on their complex numbers.
3. The goal is to reach a target complex number or to get as close as possible within a set number of turns.

### Example Game
- **Player 1** chooses `3 + 4j`
- **Player 2** chooses `1 + 2j`
- **Target** is `5 + 6j`

**Turn 1**:
- Player 1 adds `1 + 2j` to their number: `(3 + 4j) + (1 + 2j) = 4 + 6j`
- Player 2 multiplies their number by `2`: `(1 + 2j) * 2 = 2 + 4j`

**Turn 2**:
- Player 1 is already at the target `5 + 6j` and wins the game.

This game helps players practice complex number operations in a fun and engaging way.
