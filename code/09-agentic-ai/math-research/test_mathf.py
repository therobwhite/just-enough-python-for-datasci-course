"""Unit tests for the mathf library."""

import pytest
from mathf import fibonacci, multiples_of


class TestFibonacci:
    """Tests for the fibonacci generator function."""

    def test_fibonacci_first_ten_numbers(self):
        """Test that fibonacci generates the correct first 10 numbers."""
        fib = fibonacci()
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        actual = [next(fib) for _ in range(10)]
        assert actual == expected

    def test_fibonacci_is_generator(self):
        """Test that fibonacci returns a generator."""
        fib = fibonacci()
        assert hasattr(fib, '__next__')
        assert hasattr(fib, '__iter__')

    def test_fibonacci_continues_correctly(self):
        """Test that fibonacci continues correctly after first few numbers."""
        fib = fibonacci()
        # Skip first 5 numbers
        for _ in range(5):
            next(fib)
        # Test the next few
        assert next(fib) == 8
        assert next(fib) == 13
        assert next(fib) == 21


class TestMultiplesOf:
    """Tests for the multiples_of function."""

    def test_multiples_of_basic_case(self):
        """Test basic functionality with multiples of 2."""
        collection = [1, 2, 3, 4, 5, 6, 7, 8]
        result = list(multiples_of(collection, 2))
        assert result == [2, 4, 6, 8]

    def test_multiples_of_three(self):
        """Test with multiples of 3."""
        collection = [1, 2, 3, 6, 9, 10, 12, 15]
        result = list(multiples_of(collection, 3))
        assert result == [3, 6, 9, 12, 15]

    def test_multiples_of_one(self):
        """Test with multiples of 1 (all numbers)."""
        collection = [1, 2, 3, 4, 5]
        result = list(multiples_of(collection, 1))
        assert result == [1, 2, 3, 4, 5]

    def test_multiples_of_empty_collection(self):
        """Test with empty collection."""
        result = list(multiples_of([], 2))
        assert result == []

    def test_multiples_of_no_matches(self):
        """Test when no numbers are multiples."""
        collection = [1, 3, 5, 7]
        result = list(multiples_of(collection, 2))
        assert result == []

    def test_multiples_of_zero_raises_error(self):
        """Test that zero raises ValueError."""
        with pytest.raises(ValueError, match='Number must be positive'):
            list(multiples_of([1, 2, 3], 0))

    def test_multiples_of_negative_raises_error(self):
        """Test that negative numbers raise ValueError."""
        with pytest.raises(ValueError, match='Number must be positive'):
            list(multiples_of([1, 2, 3], -5))

    def test_multiples_of_is_generator(self):
        """Test that multiples_of returns a generator."""
        result = multiples_of([1, 2, 3, 4], 2)
        assert hasattr(result, '__next__')
        assert hasattr(result, '__iter__')

    def test_multiples_of_with_large_numbers(self):
        """Test with larger numbers."""
        collection = [100, 150, 200, 250, 300]
        result = list(multiples_of(collection, 50))
        assert result == [100, 150, 200, 250, 300]

    def test_multiples_of_with_duplicates(self):
        """Test that duplicates in collection are preserved."""
        collection = [2, 4, 2, 6, 4]
        result = list(multiples_of(collection, 2))
        assert result == [2, 4, 2, 6, 4]
