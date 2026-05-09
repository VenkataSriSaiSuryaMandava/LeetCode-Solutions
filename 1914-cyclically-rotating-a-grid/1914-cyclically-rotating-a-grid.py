class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def rotate_layer(layer_index, rotation_count):
            layer_elements = []

            for col in range(layer_index, num_cols - layer_index - 1):
                layer_elements.append(grid[layer_index][col])

            for row in range(layer_index, num_rows - layer_index - 1):
                layer_elements.append(grid[row][num_cols - layer_index - 1])

            for col in range(num_cols - layer_index - 1, layer_index, -1):
                layer_elements.append(grid[num_rows - layer_index - 1][col])

            for row in range(num_rows - layer_index - 1, layer_index, -1):
                layer_elements.append(grid[row][layer_index])

            effective_rotation = rotation_count % len(layer_elements)

            if effective_rotation == 0:
                return

            layer_elements = (
                layer_elements[effective_rotation:] +
                layer_elements[:effective_rotation]
            )

            element_index = 0

            for col in range(layer_index, num_cols - layer_index - 1):
                grid[layer_index][col] = layer_elements[element_index]
                element_index += 1

            for row in range(layer_index, num_rows - layer_index - 1):
                grid[row][num_cols - layer_index - 1] = layer_elements[element_index]
                element_index += 1

            for col in range(num_cols - layer_index - 1, layer_index, -1):
                grid[num_rows - layer_index - 1][col] = layer_elements[element_index]
                element_index += 1

            for row in range(num_rows - layer_index - 1, layer_index, -1):
                grid[row][layer_index] = layer_elements[element_index]
                element_index += 1

        num_rows, num_cols = len(grid), len(grid[0])

        num_layers = min(num_rows, num_cols) // 2

        for layer in range(num_layers):
            rotate_layer(layer, k)

        return grid