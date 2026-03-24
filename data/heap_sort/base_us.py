def heap_sort(array: list[int], ascending: bool = True) -> list[int]:
    """
    Sort a list of integers using the Heap Sort algorithm.

    This function does not modify the original list; instead, it returns
    a new sorted list.

    Args:
        array (list[int]): The list of integers to be sorted.
        ascending (bool, optional): If True, sort in ascending order.
            If False, sort in descending order. Defaults to True.

    Returns:
        list[int]: A new list containing the sorted elements.
    """

    # Create a copy of the array to avoid modifying the original
    arr = array.copy()
    n = len(arr)

    def heapify(n: int, i: int):
        """
        Ensure the subtree rooted at index i satisfies the heap property.

        For ascending order, we build a max-heap.
        For descending order, we build a min-heap.
        """
        extreme = i  # Initialize largest or smallest as root

        left = 2 * i + 1   # Left child index
        right = 2 * i + 2  # Right child index

        # Depending on sorting order, choose comparison
        if ascending:
            # Build max-heap
            if left < n and arr[left] > arr[extreme]:
                extreme = left
            if right < n and arr[right] > arr[extreme]:
                extreme = right
        else:
            # Build min-heap
            if left < n and arr[left] < arr[extreme]:
                extreme = left
            if right < n and arr[right] < arr[extreme]:
                extreme = right

        # If root is not the extreme, swap and continue heapifying
        if extreme != i:
            arr[i], arr[extreme] = arr[extreme], arr[i]
            heapify(n, extreme)

    # Step 1: Build the heap (max-heap or min-heap)
    # Start from the last non-leaf node and heapify each node
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]

        # Call heapify on the reduced heap
        heapify(i, 0)

    return arr