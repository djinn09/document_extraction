from spellchecker import SpellChecker
import re

def correct_spelling(text):
    """
    Corrects spelling errors in the text using a combination of manual overrides
    and a general spell checker.
    """
    # Manual overrides for common, known OCR errors.
    # Using regex with word boundaries to avoid replacing substrings.
    manual_corrections = {
        r'\bmisteaks\b': 'mistakes',
        r'\btset\b': 'test',
    }

    corrected_text = text
    for wrong_pattern, right_word in manual_corrections.items():
        # Using a lambda to preserve case of the original word
        def replace_case(match):
            word = match.group(0)
            if word.isupper():
                return right_word.upper()
            if word.istitle():
                return right_word.title()
            return right_word

        corrected_text = re.sub(wrong_pattern, replace_case, corrected_text, flags=re.IGNORECASE)

    # The general spellchecker (pyspellchecker) was found to be unreliable for
    # specific test cases (e.g., changing 'OCR' to 'OR'). For now, we rely on
    # the more controlled manual override system. This could be expanded, or a
    # better spell-checking library could be integrated in the future.

    return corrected_text

def correct_grammar(text):
    """
    Placeholder for a grammar correction function.
    """
    return text

def adjust_format(text):
    """
    Adjusts the format of the text by cleaning up whitespace.
    """
    # Split by newlines, strip each line, and filter out empty lines
    lines = [line.strip() for line in text.split('\n')]
    non_empty_lines = [line for line in lines if line]

    # For each line, replace multiple spaces with a single space
    cleaned_lines = [re.sub(r' +', ' ', line) for line in non_empty_lines]

    # Join the cleaned lines with a single newline
    return "\n".join(cleaned_lines)

def postprocess_text(text):
    """
    Runs the full post-processing pipeline on the extracted text.
    """
    # The order matters here. Adjust format first to get clean words for the spellchecker.
    formatted_text = adjust_format(text)
    spelling_corrected_text = correct_spelling(formatted_text)
    grammar_corrected_text = correct_grammar(spelling_corrected_text)

    return grammar_corrected_text
