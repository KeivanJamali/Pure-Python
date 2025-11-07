examples = {"5.1 largest_prime_factor": "6857",
            "5.2 largest_palindrome_product": "906609",
            "5.3 prime_number_generator": "104743",
            "5.4 sum_square_difference": "25164150",
            "7.1 summation_of_primes": "142913828922",
            "7.2 largest_product_in_a_series": "23514624000",
            "7.3 largest_product_in_a_grid": "70600674",
            "8.2 number_letter_counts": "21124",
            "10.1 change": "49",
            "11.1 1000_digit_fibonacci_number": "4782",
            "11.2 maximum_path_sum_I": "1074",
            "12.2 maximum_path_sum_II": "7273",
            "11.3 factorial_digit_sum": "648",
            "12.1 name_scores": "871198282"}

def check_answer(question: str, answer: str) -> bool:
    names = examples.keys()
    
    if question in names:
        if str(answer) == examples[question]:
            return True
        else:
            return False
    else:
        return False