import math
import re
from concurrent.futures import ThreadPoolExecutor
from Read_Docx_and_generate_Txt__Docx import Read_Doc_and_generate_Txt as Read_Doc_and_generate
import matplotlib.colors as mcolors
from PyQt5.QtWidgets import QMessageBox

import os


class AL_CODON_Counter:

    def __init__(self):
        self.Conteneur = Read_Doc_and_generate()

    # Define the strings to search for
    search_strings = ["ATTCA", "TTCAA", "TCAAG", "CAAGA", "AAGAT", "AGATG", "GATGA", "ATGAA", "TGAAT"]

    # Map each search string to a specific color
    color_mapping = {
        "ATTCA": mcolors.CSS4_COLORS['red'],
        "TTCAA": mcolors.CSS4_COLORS['blue'],
        "TCAAG": mcolors.CSS4_COLORS['green'],
        "CAAGA": mcolors.CSS4_COLORS['purple'],
        "AAGAT": mcolors.CSS4_COLORS['orange'],
        "AGATG": mcolors.CSS4_COLORS['magenta'],
        "GATGA": mcolors.CSS4_COLORS['brown'],
        "ATGAA": mcolors.CSS4_COLORS['teal'],
        "TGAAT": mcolors.CSS4_COLORS['darkviolet']
    }

    def read_sequence_file(self):
        with open("dna_sequence.txt", "r") as file:
            text_input = file.read().replace('\n', '').replace(' ', '')
        return text_input

    # Read ANY Chosen text from a file, ensuring it's a continuous string
    def read_ANY_file(self, file_path):
        # Get the file extension
        _, file_extension = os.path.splitext(file_path)

        count_greater_than = 0

        # Check if it's either a .docx or FASTA file
        # or file_extension in {'.fasta', '.fa', '.fas', '.fna'}
        if file_extension.lower() == '.docx':

            # Extract titles and sequences for .docx files

            titles, sequences = self.Conteneur.extract_titles_and_sequences(file_path)

            doc_exit = True

            # Count nucleotide sequences and clean data
            cleaned_sequences = []
            additional_text_ALL = []

            # -------------------------------------------

            # Use multiprocessing to process the sequences
            cleaned_sequences, additional_text_ALL = self.Conteneur.process_sequences_multiprocessing_DOC(sequences)

            # -------------------------------------------------
            # Prepare the output variables

            text_input = cleaned_sequences[0] if cleaned_sequences else ""

            file_new_title = titles[0] if titles else "Unnamed Sequence"


        else:
            # Handle non-docx files
            with open(file_path, "r") as file:
                additional_text_ALL = []
                # Read and clean the text content
                text_input = file.read().replace('\n', '').replace(' ', '')
                # Count the occurrences of ">" to verify if it is a UNIQUE Sequence or Not
                count_greater_than = text_input.count('>')

                # Process the sequence to find nucleotide sequences
                text_input, file_new_title = self.Conteneur.count_nucleotide_sequences(text_input)
                additional_text_ALL.append("No additional information.")
                titles = [file_new_title]  # Use the title extracted from processing
                cleaned_sequences = [text_input]  # Wrap the result in a list
                doc_exit = False

        return text_input, file_new_title, additional_text_ALL, titles, cleaned_sequences, doc_exit, count_greater_than

    # ---------------------Adding SOME MODULE TO MAKE IT SPEEDY !!-----
    # Process the text and Color the Searched 9 Pentamers
    # To improve the performance of THIS function "find_and_count_with_coloring",
    # It seems I can use Python's "concurrent.futures module"
    # This module supports both multithreading and multiprocessing.
    # Given that My function "find_and_count_with_coloring" performs a lot of string operations,
    # it might benefit more from multithreading
    # because Python's Global Interpreter Lock (GIL) can sometimes allow I/O-bound operations and certain CPU-bound
    # operations to run in parallel.

    def count_occurrences(self, filtered_text, search_string):
        return filtered_text.count(search_string)

    def replace_with_coloring(self, colored_text, search_string, color):

        return colored_text.replace(search_string, f"<span style='color: {color};'>{search_string}</span>")

    def find_and_count_with_coloring(self, text, search_strings, color_mapping):
        global Df_TTCAA
        global Df_ATTCA, Df_TTCAA, Df_TCAAG, Df_CAAGA, Df_AAGAT, Df_AGATG, Df_GATGA, Df_ATGAA, Df_TGAAT

        # Filter the text to only include 'A', 'C', 'T', 'G', 'N'
        filtered_text = ''.join([char for char in text.upper() if char in 'ACTGNRYSWKMBDHV'])

        total_characters = len(filtered_text)
        occurrences = {string: 0 for string in search_strings}
        total_occurrences = 0

        # Use ThreadPoolExecutor to count occurrences of each search string
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.count_occurrences, filtered_text, string): string for string in
                       search_strings}
            for future in futures:
                string = futures[future]
                count = future.result()
                occurrences[string] = count
                total_occurrences += count

        # Replace with colored version after counting
        colored_text = filtered_text
        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(self.replace_with_coloring, colored_text, string,
                                color_mapping.get(string, "black")): string for string in search_strings}

            for future in futures:
                string = futures[future]
                color = color_mapping.get(string, "black")
                colored_text = colored_text.replace(string, f"<span style='color: {color};'>{string}</span>")
                if string == 'ATTCA':
                    Df_ATTCA = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'TTCAA':
                    Df_TTCAA = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'TCAAG':
                    Df_TCAAG = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'CAAGA':
                    Df_CAAGA = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'AAGAT':
                    Df_AAGAT = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'AGATG':
                    Df_AGATG = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'GATGA':
                    Df_GATGA = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'ATGAA':
                    Df_ATGAA = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'TGAAT':
                    Df_TGAAT = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")

        # Perform the mathematical model calculations
        first_result = (total_characters * 9) / 1024
        sqrt_of_first_result = math.sqrt(first_result)
        final_result = (total_occurrences - first_result) / sqrt_of_first_result

        return occurrences, total_occurrences, total_characters, colored_text, first_result, sqrt_of_first_result, final_result, filtered_text, Df_ATTCA, Df_TTCAA, Df_TCAAG, Df_CAAGA, Df_AAGAT, Df_AGATG, Df_GATGA, Df_ATGAA, Df_TGAAT

    # ---------------END------Adding SOME MODULE TO MAKE IT SPEEDY !!-----

    # Display the results
    def Display_results(self, results):

        messages = []

        for string, count in results[0].items():
            message = f"The pentamer '{string}' occurred {count} times."
            messages.append(message)

        # Add other results messages
        messages.append(f"The total occurrences of all specified strings is {results[1]}.")
        messages.append(f"The total number of characters in the text is {results[2] - 4}.")
        messages.append(f"First result (Total characters *9 /1024): {results[4]}")
        messages.append(f"Square root of the first result: {results[5]}")
        messages.append(f"Final result: {results[6]}")

        # Join all messages into a single string with line breaks
        results_summary = "\n".join(messages)

        return results_summary

    # GET a RED Sequence
    def find_and_count_to_RED(self, text):
        # Define the strings to search for
        search_strings = ["ATTCA", "TTCAA", "TCAAG", "CAAGA", "AAGAT", "AGATG", "GATGA", "ATGAA", "TGAAT"]

        # Filter the text to only include 'A', 'C', 'T', 'G', 'N'
        filtered_text = ''.join([char for char in text.upper() if char in 'ACTGNRYSWKMBDHV'])
        red_text = filtered_text

        # Function to replace a string with its colored span tag
        def replace_string(string):
            nonlocal red_text
            red_text = re.sub(rf"({string})", rf"<span style='color: red;'>\1</span>", red_text)

        # Use ThreadPoolExecutor to replace strings concurrently
        with ThreadPoolExecutor() as executor:
            executor.map(replace_string, search_strings)

        # Return the HTML-styled red text
        return red_text

    # GET a Colored Sequence

    def find_and_count_to_Colored(self, text):
        # Define the strings to search for
        search_strings = ["ATTCA", "TTCAA", "TCAAG", "CAAGA", "AAGAT", "AGATG", "GATGA", "ATGAA", "TGAAT"]
        # Map each search string to a specific color.
        color_mapping = {
            "ATTCA": "red",
            "TTCAA": "blue",
            "TCAAG": "green",
            "CAAGA": "purple",
            "AAGAT": "orange",
            "AGATG": "pink",
            "GATGA": "brown",
            "ATGAA": "teal",
            "TGAAT": "gray"
        }
        # Pre-generate the HTML span tags for each string with their respective colors.
        span_tags = {string: rf"<span style='color: {color};'>{string}</span>" for string, color in
                     color_mapping.items()}

        # Filter the text to only include'ACTGNRYSWKMBDHV'
        filtered_text = ''.join([char for char in text.upper() if char in 'ACTGNRYSWKMBDHV'])
        Colored_text = filtered_text

        # Function to replace a string with its colored span tag
        def replace_string(string):
            nonlocal Colored_text
            span_tag = span_tags[string]
            Colored_text = re.sub(rf"({string})", span_tag, Colored_text)

        # Use ThreadPoolExecutor to replace strings concurrently
        with ThreadPoolExecutor() as executor:
            executor.map(replace_string, search_strings)

        # Return the HTML-styled red text
        return Colored_text

    # GET a RED Sequence_ For The TAIL 5 Pentamers
    def find_and_count_to_RED_TAIL(self, text):
        # Define the strings to search for
        search_strings = ["AGATG", "GATGA", "GTGGC", "TGGCC", "GGCCT"]

        # Filter the text to only include 'A', 'C', 'T', 'G', 'N'
        filtered_text = ''.join([char for char in text.upper() if char in 'ACTGNRYSWKMBDHV'])
        red_text_TAIL = filtered_text

        # Function to replace a string with its colored span tag
        def replace_string(string):
            nonlocal red_text_TAIL
            red_text_TAIL = re.sub(rf"({string})", rf"<span style='color: red;'>\1</span>", red_text_TAIL)

        # Use ThreadPoolExecutor to replace strings concurrently
        with ThreadPoolExecutor() as executor:
            executor.map(replace_string, search_strings)
        # Return the HTML-styled red text
        return red_text_TAIL

    # GET a COLORED Sequence_ For The TAIL 5 Pentamers
    def find_and_count_to_Colored_TAIL(self, text):
        # Define the strings to search for
        search_strings = ["AGATG", "GATGA", "GTGGC", "TGGCC", "GGCCT"]
        # Map each search string to a specific color.
        color_mapping = {
            "AGATG": "red",
            "GATGA": "blue",
            "GTGGC": "green",
            "TGGCC": "purple",
            "GGCCT": "orange",
        }
        # Pre-generate the HTML span tags for each string with their respective colors.
        span_tags = {string: rf"<span style='color: {color};'>{string}</span>" for string, color in
                     color_mapping.items()}

        # Filter the text to only include 'A', 'C', 'T', 'G', 'N'
        filtered_text = ''.join([char for char in text.upper() if char in 'ACTGNRYSWKMBDHV'])
        Colored_text_TAIL = filtered_text

        # Function to replace a string with its colored span tag
        def replace_string(string):
            nonlocal Colored_text_TAIL
            span_tag = span_tags[string]
            Colored_text_TAIL = re.sub(rf"({string})", span_tag, Colored_text_TAIL)

        # Use ThreadPoolExecutor to replace strings concurrently
        with ThreadPoolExecutor() as executor:
            executor.map(replace_string, search_strings)

        # Return the HTML-styled red text
        return Colored_text_TAIL

    # Find and count with coloring For The TAIL 5 Pentamers
    def find_and_count_with_coloring_TAIL(self, text):
        # Define the strings to search for
        search_strings = ["AGATG", "GATGA", "GTGGC", "TGGCC", "GGCCT"]
        # Map each search string to a specific color.
        color_mapping = {
            "AGATG": "red",
            "GATGA": "blue",
            "GTGGC": "green",
            "TGGCC": "purple",
            "GGCCT": "orange",
        }

        # Filter the text to only include 'A', 'C', 'T', 'G', 'N'
        filtered_text = ''.join([char for char in text.upper() if char in 'ACTGNRYSWKMBDHV'])

        total_characters = len(filtered_text)
        occurrences = {string: 0 for string in search_strings}
        total_occurrences = 0

        # Use ThreadPoolExecutor to count occurrences of each search string
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(self.count_occurrences, filtered_text, string): string for string in
                       search_strings}
            for future in futures:
                string = futures[future]
                count = future.result()
                occurrences[string] = count
                total_occurrences += count

        # Replace with colored version after counting
        colored_text = filtered_text
        with ThreadPoolExecutor() as executor:
            futures = {
                executor.submit(self.replace_with_coloring, colored_text, string,
                                color_mapping.get(string, "black")): string for string in search_strings}

            for future in futures:
                string = futures[future]
                color = color_mapping.get(string, "black")
                colored_text = colored_text.replace(string, f"<span style='color: {color};'>{string}</span>")
                if string == 'AGATG':
                    Df_AGATG = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'GATGA':
                    Df_GATGA = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'GTGGC':
                    Df_GTGGC = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'TGGCC':
                    Df_TGGCC = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")
                if string == 'GGCCT':
                    Df_GGCCT = filtered_text.replace(string, f"<span style='color: red;'>{string}</span>")

        # Perform the mathematical model calculations
        first_result = (total_characters * 5) / 1024
        sqrt_of_first_result = math.sqrt(first_result)
        final_result = (total_occurrences - first_result) / sqrt_of_first_result
        '''
        # Print the staggered lines of the sequence
        for i in range(total_characters):
            line = colored_text[i:]
            # print(line)
            if len(line) <= 1:  # Stop when we get to the last character
                break
        '''
        return occurrences, total_occurrences, total_characters, colored_text, first_result, sqrt_of_first_result, \
               final_result, filtered_text, Df_AGATG, Df_GATGA, Df_GTGGC, Df_TGGCC, Df_GGCCT

    # Display the results For The TAIL 5 Pentamers
    def Display_results_TAIL(self, results):

        messages = []

        for string, count in results[0].items():
            message = f"The pentamer '{string}' occurred {count} times."
            messages.append(message)

        # Add other results messages
        messages.append(f"The total occurrences of all specified strings is {results[1]}.")
        messages.append(f"The total number of characters in the text is {results[2] - 4}.")
        messages.append(f"First result (Total characters *5 /1024): {results[4]}")
        messages.append(f"Square root of the first result: {results[5]}")
        messages.append(f"Final result: {results[6]}")

        # Join all messages into a single string with line breaks
        results_summary = "\n".join(messages)

        return results_summary
