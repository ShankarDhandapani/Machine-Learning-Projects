# linear_algebra

---

The project has already deployed automated tests, and you can see the following test code below each function that you need to complete:% run -i -e test.py LinearRegressionTestCase.test _... Ctrl Enter to run.

If your implementation has a problem, there will be an assertion that the AssertionError is thrown. Please re-check your implementation and fix bugs until you pass the test.

Here are some assertions with specific feedback:

    AssertionError: Matrix A should not be modified
        You modified the matrix A when implementing augmentMatrix
    AssertionError: Matrix A is singular
        Your gj_Solve implementation does not return None when matrix A is a singular matrix
    AssertionError: Matrix A is not singular
        Your gj_Solve implementation returns None if Matrix A is not a singular matrix
    AssertionError: x have to be two-dimensional Python List
        Your gj_Solve returns the data structure is incorrect, x must be a two-dimensional list, and is the Nx1 column vector
    AssertionError: Regression result is not good enough
        Your gj_Solve returns the result of the calculation, but the deviation is too large
