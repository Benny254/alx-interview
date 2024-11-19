#!/usr/bin/python3
"""2D matrix rotation module.
"""

def rotate_2d_matrix(matrix):
        """Rotates an n x n 2D matrix 90 degrees clockwise in place.
            """
                if not isinstance(matrix, list) or not matrix:
                            return
                            n = len(matrix)
                                if not all(isinstance(row, list) and len(row) == n for row in matrix):
                                            return

                                            for layer in range(n // 2):
                                                        first, last = layer, n - layer - 1
                                                                for i in range(first, last):
                                                                                offset = i - first
                                                                                            # Save the top element
                                                                                                        top = matrix[first][i]
                                                                                                                    # Move left element to top
                                                                                                                                matrix[first][i] = matrix[last - offset][first]
                                                                                                                                            # Move bottom element to left
                                                                                                                                                        matrix[last - offset][first] = matrix[last][last - offset]
                                                                                                                                                                    # Move right element to bottom
                                                                                                                                                                                matrix[last][last - offset] = matrix[i][last]
                                                                                                                                                                                            # Assign top element to right
                                                                                                                                                                                                        matrix[i][last] = top
                                                                                                                                                                                                        #!/usr/bin/python3
                                                                                                                                                                                                        """2D matrix rotation module.
                                                                                                                                                                                                        """

                                                                                                                                                                                                        def rotate_2d_matrix(matrix):
                                                                                                                                                                                                                """Rotates an n x n 2D matrix 90 degrees clockwise in place.
                                                                                                                                                                                                                    """
                                                                                                                                                                                                                        if not isinstance(matrix, list) or not matrix:
                                                                                                                                                                                                                                    return
                                                                                                                                                                                                                                    n = len(matrix)
                                                                                                                                                                                                                                        if not all(isinstance(row, list) and len(row) == n for row in matrix):
                                                                                                                                                                                                                                                    return

                                                                                                                                                                                                                                                    for layer in range(n // 2):
                                                                                                                                                                                                                                                                first, last = layer, n - layer - 1
                                                                                                                                                                                                                                                                        for i in range(first, last):
                                                                                                                                                                                                                                                                                        offset = i - first
                                                                                                                                                                                                                                                                                                    # Save the top element
                                                                                                                                                                                                                                                                                                                top = matrix[first][i]
                                                                                                                                                                                                                                                                                                                            # Move left element to top
                                                                                                                                                                                                                                                                                                                                        matrix[first][i] = matrix[last - offset][first]
                                                                                                                                                                                                                                                                                                                                                    # Move bottom element to left
                                                                                                                                                                                                                                                                                                                                                                matrix[last - offset][first] = matrix[last][last - offset]
                                                                                                                                                                                                                                                                                                                                                                            # Move right element to bottom
                                                                                                                                                                                                                                                                                                                                                                                        matrix[last][last - offset] = matrix[i][last]
                                                                                                                                                                                                                                                                                                                                                                                                    # Assign top element to right
                                                                                                                                                                                                                                                                                                                                                                                                                matrix[i][last] = top

