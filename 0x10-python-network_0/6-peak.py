#!/usr/bin/python3
"""Defines a peak-finding algorithm."""

def find_peak(list_of_integers):
    """
    Finds a peak value in a list of unsorted integers.
    A peak value is defined as an element that is greater than or equal to its neighbors.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None
    
    # Initialize left and right pointers for binary search
    left = 0
    right = len(list_of_integers) - 1
    
    # Binary search for a peak
    while left < right:
        mid = (left + right) // 2  # Calculate the midpoint index
        
        # Check if the midpoint value is a peak
        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        
        # If the value to the right of the midpoint is greater, search to the right
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        
        # Otherwise, search to the left
        else:
            right = mid - 1
    
    # Check if the last remaining element is a peak
    if left == right and \
       list_of_integers[left] >= list_of_integers[left - 1] and \
       list_of_integers[left] >= list_of_integers[left + 1]:
        return list_of_integers[left]
    
    # If no peak is found, return None
    return None

