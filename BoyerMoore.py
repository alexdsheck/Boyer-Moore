import time
import random


def boyer_moore_approximate(text, pattern, max_mismatches):
    m = len(pattern)
    n = len(text)
    if m > n:
        return []

    skip = []
    for _ in range(256):  # Initialize skip table with default value
        skip.append(m)

    for i in range(m - 1):
        skip[ord(pattern[i])] = m - 1 - i

    matches = []
    matched_positions = []  # Keep track of positions of matched patterns
    i = 0
    while i <= n - m:
        mismatches = 0  # Reset mismatches for each potential match
        j = m - 1
        while j >= 0:
            if pattern[j] != text[i + j]:
                mismatches += 1
                if mismatches > max_mismatches:
                    break
            j -= 1
        if j < 0:
            matches.append(i)
            matched_positions.append(i)  # Add position of matched pattern
        i += max(1, skip[ord(text[i + m - 1])])  # Use max to ensure progress even with bad characters

    # Extract matched patterns and their positions from the text
    matched_info = [(text[pos:pos + m], pos) for pos in matched_positions]

    return matched_info


def filter_dna_sequence(sequence):
    valid_chars = set('ACTGU')  # Valid nucleotide characters
    return ''.join([char for char in sequence.upper() if char in valid_chars])  # Filter and combine valid characters


def generate_random_genome(length):
    return ''.join(random.choices('ACTG', k=length))  # Generate a random DNA sequence of specified length


if __name__ == '__main__':
    file_path = 'sequence.fasta'
    with open(file_path, 'r') as file:
        original_text = file.read(100000000)

    # Filter out newline characters from the text
    original_text = filter_dna_sequence(original_text)

    # Experiment #1: Boyer-Moore
    #
    # base_pattern = generate_random_genome(1)
    #
    # print("Pattern Length \t Runtime (seconds)")
    # for pattern_length in range(1, 102, 10):  # Example pattern lengths to test
    #     pattern = base_pattern + generate_random_genome(pattern_length - len(base_pattern))  # Add random genome
    #
    #     max_mismatches = 0
    #
    #     # Timer for runtime measurement
    #     start_time = time.time()
    #     boyer_moore_approximate(original_text, pattern, max_mismatches)
    #     end_time = time.time()
    #     runtime = end_time - start_time
    #
    #     print(f"{len(pattern)} \t {runtime:.4f}")

    # # Experiment #1: Boyer-Moore-Approximate
    #
    # base_pattern = generate_random_genome(1)
    #
    # print("Pattern Length \t Runtime (seconds)")
    # for pattern_length in range(1, 102, 10):  # Example pattern lengths to test
    #     pattern = base_pattern + generate_random_genome(pattern_length - len(base_pattern))  # Add random genome
    #
    #     # 1/5 of sequence can be a mismatch and still be considered a match
    #     max_mismatches = len(pattern) // 5
    #
    #     # Timer for runtime measurement
    #     start_time = time.time()
    #     boyer_moore_approximate(original_text, pattern, max_mismatches)
    #     end_time = time.time()
    #     runtime = end_time - start_time
    #
    #     print(f"{len(pattern)} \t {runtime:.4f}")

    # Experiment #2: Boyer-Moore
    #
    # base_pattern = generate_random_genome(10)
    #
    # print("Dataset Size \t Runtime (seconds)")
    # for dataset_size in range(10000, 10000000, 100000):
    #     text = original_text[:dataset_size]  # Use a portion of the original text for testing
    #
    #     pattern = base_pattern + generate_random_genome(len(base_pattern))
    #     max_mismatches = 0
    #
    #     # Timer for runtime measurement with max_mismatches = 0
    #     start_time = time.time()
    #     boyer_moore_approximate(text, pattern, max_mismatches)
    #     end_time = time.time()
    #     runtime = end_time - start_time
    #
    #     print(f"{dataset_size} \t {runtime:.4f}")
    #
    # Experiment #2: Boyer-Moore-Approximate

    # Experiment #3: Boyer-Moore-Approximate max_mismatch comparison
    #
    # base_pattern = generate_random_genome(10)
    #
    # print("max_mismatches \t Runtime (seconds)")
    # pattern = generate_random_genome(30)
    # for mismatches in range(1, 6):
    #     text = original_text  # Use a portion of the original text for testing
    #
    #     max_mismatches = mismatches
    #
    #     # Timer for runtime measurement with max_mismatches = 0
    #     start_time = time.time()
    #     boyer_moore_approximate(text, pattern, max_mismatches)
    #     end_time = time.time()
    #     runtime = end_time - start_time
    #
    #     print(f"{max_mismatches} \t {runtime:.4f}")
