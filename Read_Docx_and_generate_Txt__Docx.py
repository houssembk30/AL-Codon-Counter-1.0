import pandas as pd
import re

from PyQt5.QtWidgets import QMessageBox
from docx import Document
import os
from multiprocessing import Pool


class Read_Doc_and_generate_Txt:
    # Read text from a file, ensuring it's a continuous string
    def write_titles_and_sequences_to_file(titles, sequences):

        # Write all titles and their corresponding sequences to a file.

        # param titles: List of titles
        # param sequences: List of sequences corresponding to the titles

        output_file = "Extracted_Titles_and_Sequences.txt"
        with open(output_file, "w") as file:
            for title, reste in zip(titles, sequences):
                # Write the title and sequence pairs to the output file
                file.write(f"Title: {title}\n")
                file.write(f"Reste: {reste}\n\n")

    def extract_titles_and_sequences(self, file_path):

        # Extracts all titles and their subsequent sequences with commentaries
        # from a `.docx` or '.fasta', '.fa', '.fas', '.fna' file.

        doc = Document(file_path)
        titles = []
        sequences = []

        current_title = None
        current_sequence = []
        collecting_commentary = False

        def is_nucleotide_sequence(text):
            # Helper function to identify nucleotide sequences."""
            return bool(re.fullmatch(r'[ACTGNRYSWKMBDHV]+', text.replace(' ', '')))

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()

            if text.startswith('>'):
                # Save the previous title and its associated sequence + commentary
                if current_title:
                    # Apply the replacements to clean up the sequence
                    cleaned_sequence = ''.join(current_sequence).replace('\n', '').replace(' ', '')
                    sequences.append(cleaned_sequence)
                    titles.append(current_title)

                # Start with a new title and reset the sequence/commentary collection
                current_title = text
                current_sequence = []
                collecting_commentary = False

            elif is_nucleotide_sequence(text):
                # Collect the nucleotide sequence
                current_sequence.append(text.replace('\n', '').replace(' ', ''))
                collecting_commentary = True  # Start collecting commentary afterward

            elif collecting_commentary:
                # Append the commentary that comes after the sequence
                current_sequence.append(' ' + text)

        # Add the final title and sequence with commentary
        if current_title and current_sequence:
            # Apply the replacements to clean up the last sequence
            joined_sequence = ''.join(current_sequence).replace('\n', '').replace(' ', '')
            sequences.append(joined_sequence)
            titles.append(current_title)

        return titles, sequences

    def count_nucleotide_sequences_Docx(self, input_sequence):
        # This regex attempts to capture only the nucleotide sequence until it hits a pattern that indicates
        # commentary or statistical data. (?=...) is a positive lookahead assertion, which means it checks for the
        # presence of certain patterns immediately following the current matching point without including those
        # patterns in the main match.
        # "The string" is a searched literal text that,if found immediately after a nucleotide sequence, indicates
        # the end of that sequence.
        # \s\d+ looks for a whitespace character (\s) followed by one
        # or more digits (\d+). This is used to catch scenarios where the sequence might be directly followed by a
        # number that has a space separator, indicating statistical or other numerical data that follows. \d+
        # directly looks for one or more digits. This addition handles cases where numbers may appear right after the
        # nucleotide sequence without a preceding space, which can be common in concatenated data or in certain data
        # formats.

        pattern = re.compile(r"([ACTGNRYSWKMBDHV]+)(?=Thestring|Thepentamer|\s\d+|\d+)")

        match = pattern.search(input_sequence)
        if match:
            nucleotide_sequence = match.group(1)
            # Everything after the match
            additional_text = input_sequence[match.end():]
        else:

            nucleotide_sequence = ""
            # Assume entire input might be non-nucleotide if no match is found
            additional_text = input_sequence

        return nucleotide_sequence, additional_text

    def create_dataframe(self, nucleotide_sequence, additional_text):
        # Create a DataFrame
        df = pd.DataFrame({
            "Nucleotide Sequence": [nucleotide_sequence],
            "Additional Text": [additional_text]
        })
        return df

    # count_nucleotide_sequences(input_sequence)
    def count_nucleotide_sequences(self, input_sequence):

        valid_nucleotides = {'A', 'T', 'G', 'C', 'G', 'N', 'R', 'Y', 'S', 'W', 'K', 'M', 'B', 'D', 'H', 'V'}
        sequence_count = 0
        deleted_characters = []

        # Loop through the string, stopping 10 characters before the end to avoid index errors
        for i in range(len(input_sequence) - 9):
            # Extract a substring of 10 characters starting from the current position
            substring = input_sequence[i:i + 10]
            remaining_input_sequence = input_sequence[i:len(input_sequence)]

            # Check if all characters in the substring are valid nucleotides
            if set(substring).issubset(valid_nucleotides):
                # Combine all characters in deleted_characters into a single string
                deleted_characters_str = ''.join(deleted_characters)

                break
            else:
                # If the current character is not part of a valid sequence, append it to the list
                # Ensure not to include characters that are part of the last 10 characters
                if i < len(input_sequence) - 10:
                    deleted_characters.append(input_sequence[i])
        else:
            # This part is executed if the loop completes without finding a valid sequence
            QMessageBox.warning(self, "Warning", "No valid sequence found HOUSSEM.")

        return remaining_input_sequence, deleted_characters_str

    # Special Trait in ERRRRROOOOOOOOOOOOOOOOOOOOOr
    def count_nucleotide_sequences_Docx_RECTIF(self, input_sequence):

        # Simplified pattern just to check for sequences of A, T, G, C,N
        pattern = re.compile(r"([ACTGNRYSWKMBDHV]+)")

        match = pattern.search(input_sequence)
        if match:
            nucleotide_sequence = match.group(1)
            # Everything after the match
            additional_text = input_sequence[match.end():]

        else:
            QMessageBox.warning(self, "Warning", "No valid sequence found. Check if the input sequence contains "
                                                 "nucleotides.")
            nucleotide_sequence = ""
            # Assume the entire input might be non-nucleotide if no match is found
            additional_text = input_sequence

        return nucleotide_sequence, additional_text

    # Process Multiple Files to Dataframe
    def process_files_to_dataframe(self, files):
        # Create a list to hold data from all files
        data = []

        # Process each file in the list
        for file in files:
            # Check if file ends with any of the specified extensions
            if file.endswith('.txt') or file.endswith('.fasta') or file.endswith('.fas') or file.endswith(
                    '.fa') or file.endswith('.fna'):
                # Extract the filename without the extension
                file_name = os.path.splitext(os.path.basename(file))[0]

                # Read the content of the file
                with open(file, 'r') as f:
                    content = f.read().splitlines()

                # Insert the new header line which starts by ">name of te file"
                # at the beginning for txt files
                if file.endswith('.txt'):
                    # Open the file to read its content
                    with open(file, 'r') as f:
                        # Read the first character or line
                        first_char = f.read(1)
                        # Check if the first character is not '>'
                        if first_char != '>':
                            # Your action here if it doesn't start with '>'
                            content.insert(0, f">{file_name}")

                # Create a DataFrame for the current file's content
                df = pd.DataFrame(content, columns=['Content'])
                df['Filename'] = file_name  # Add a column for the filename

                # Append the DataFrame of the current file to the list
                data.append(df)

        # Concatenate all DataFrames into one DataFrame
        combined_df = pd.concat(data, ignore_index=True)

        return combined_df

    # Process Counter Entry USED By Wrapper (process_entry_wrapper)
    def process_counter_entry(self, entry):

        entry_join = entry.replace('\n', '').replace(' ', '')
        text_input, file_new_title = self.count_nucleotide_sequences(entry_join)
        process_id = os.getpid()
        return text_input, file_new_title, process_id

    # THe Wrapper Function to help with the issues of the Previous Lambda function
    # not being PICKABLE by "multiprocessing" Module
    def process_entry_wrapper(self, entry):

        return self.process_counter_entry(entry)

    # extract_titles_and_sequences From Multiple Files (.txt/.Fasta or combined) Selection You Must HOUSSEM that you
    # forgot that the "input_text" is not a <class 'list'> but ------------->combined_content--TYPE-- <class 'str'>
    def extract_titles_and_sequences_Multi_files(self, input_text):
        # Ensure uniform newlines and split on '>' while removing the first empty split if the text starts with '>'
        entries = input_text.replace('..>', '..').replace('\r\n', '\n').replace('\r', '\n').split('>')
        entries = [e for e in entries if e.strip()]  # Remove any empty entries

        # Use multiprocessing to process entries
        with Pool(processes=6) as pool:  # Adjust the number of processes as needed
            results = pool.map(self.process_entry_wrapper, entries)

        titles = []
        sequences = []
        cleaned_sequences = []
        additional_text_ALL = []

        for result in results:
            text_input, file_new_title, process_id = result

            if "Thepentamer" in text_input:
                nucleotide_sequence, additional_text = self.count_nucleotide_sequences_Docx(text_input)
                text_input = nucleotide_sequence
            else:
                additional_text = "No additional information."
            additional_text_ALL.append(additional_text)
            cleaned_sequences.append(text_input)
            titles.append(''.join(['>', file_new_title]))

        return text_input, file_new_title, additional_text_ALL, titles, cleaned_sequences

    # Multi Process Doc File With Mutli Sequences /
    # I know it's a kind of repeated function But I'm Still Learning Multiprocessing ;)
    # So the error you're getting here is due to the type of "sequences_DOC" is <class 'list'> !!!!!
    def process_sequences_multiprocessing_DOC(self, sequences_DOC):
        # Assuming sequences_DOC is <class 'list'>
        # Convert list to string with each sequence on a new line
        sequences = '\n'.join(sequences_DOC)

        # Ensure uniform newlines and split each sequence into an entry
        entries = sequences.split('\n')
        # Remove any empty entries
        entries = [e for e in entries if e.strip()]

        # Use multiprocessing to process entries
        with Pool(processes=6) as pool:  # Adjust the number of processes as needed
            try:
                results = pool.map(self.process_entry_wrapper, entries)

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error during multiprocessing: {e}")

        titles = []
        cleaned_sequences = []
        additional_text_ALL = []

        for result in results:
            text_input, file_new_title, process_id = result

            # List of substrings to check for "Thepentamer"or "Thestring"
            substrings = ["Thepentamer", "Thestring"]
            # Check for the presence of any of the substrings or any number
            if any(substring in text_input for substring in substrings) or re.search(r'\d', text_input):
                nucleotide_sequence, additional_text = self.count_nucleotide_sequences_Docx(text_input)
                text_input = nucleotide_sequence
            else:
                additional_text = "No additional information."
            additional_text_ALL.append(additional_text)
            cleaned_sequences.append(text_input)
            titles.append(''.join(['>', file_new_title]))

        return cleaned_sequences, additional_text_ALL
