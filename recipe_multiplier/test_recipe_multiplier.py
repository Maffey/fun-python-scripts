import pytest

from recipe_multiplier.recipe_multiplier import process_fraction


@pytest.mark.parametrize(
    "input_fraction,multiplier,expected",
    [
        # Simple fractions
        ("1/2", 2, "1"),  # 1/2 * 2 = 1
        ("1/2", 0.5, "1/4"),  # 1/2 * 0.5 = 1/4
        ("1/4", 2, "1/2"),  # 1/4 * 2 = 1/2
        ("3/4", 2, "1 1/2"),  # 3/4 * 2 = 1 1/2
        
        # Mixed numbers
        ("1 1/2", 2, "3"),  # 1 1/2 * 2 = 3
        ("2 1/4", 2, "4 1/2"),  # 2 1/4 * 2 = 4 1/2
        ("1 3/4", 0.5, "7/8"),  # 1 3/4 * 0.5 = 7/8
        
        # Edge cases
        ("0", 2, "0"),  # 0 * 2 = 0
        ("1/1", 2, "2"),  # 1/1 * 2 = 2
        ("2/2", 2, "2"),  # 2/2 * 2 = 2
        ("1 0/4", 2, "2"),  # 1 0/4 * 2 = 2
        
        # Complex cases
        ("1 1/3", 3, "4"),  # 1 1/3 * 3 = 4
        ("2 2/3", 1.5, "4"),  # 2 2/3 * 1.5 = 4
        ("1 1/8", 2, "2 1/4"),  # 1 1/8 * 2 = 2 1/4
        
        # Reducing fractions
        ("2/4", 2, "1"),  # 2/4 * 2 = 1
        ("3/6", 2, "1"),  # 3/6 * 2 = 1
        ("4/8", 2, "1"),  # 4/8 * 2 = 1
    ],
    ids=[
        "simple_1_2_times_2",
        "simple_1_2_times_0_5",
        "simple_1_4_times_2",
        "simple_3_4_times_2",
        "mixed_1_1_2_times_2",
        "mixed_2_1_4_times_2",
        "mixed_1_3_4_times_0_5",
        "edge_zero",
        "edge_one_over_one",
        "edge_two_over_two",
        "edge_mixed_with_zero",
        "complex_1_1_3_times_3",
        "complex_2_2_3_times_1_5",
        "complex_1_1_8_times_2",
        "reduce_2_4_times_2",
        "reduce_3_6_times_2",
        "reduce_4_8_times_2",
    ]
)
def test_process_fraction(input_fraction, multiplier, expected):
    """Test the process_fraction function with various inputs and multipliers."""
    result = process_fraction(input_fraction, multiplier)
    assert result == expected, f"Expected {expected} but got {result} for {input_fraction} * {multiplier}" 