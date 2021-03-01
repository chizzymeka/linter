# PyCharm help at https://www.jetbrains.com/help/pycharm/
# Pylint: https://pypi.org/project/pylint/
# Invoking pylint Programmatically: https://stackoverflow.com/questions/2028268/invoking-pylint-programmatically
# Simple Python Script to Run Pylint Programmatically: https://gist.github.com/doedotdev/18fdba69e940975783385f7be88e2ac5
# 'pylintrc' file Generation Command: pylint --generate-rcfile > .pylintrc

import os
from pylint.lint import Run
from pylint.reporters.json_reporter import JSONReporter


def lint_snippets():

    # MAIN WORK
    # root_directory = 'E:\\snippets\\python\\python\\py\\SnippetsOutput-0'
    # candidate_code_snippet_file = 'E:\\snippets\\python\\python\\snips_sym_kw_6lines_id'

    # TEST
    root_directory = 'E:\\snippets\\python\\python\\test-folder'
    candidate_code_snippet_file = 'E:\\snippets\\python\\python\\snips_sym_kw_6lines_id'

    with open(candidate_code_snippet_file) as lines:
        candidate_code_snippet_filenames = []
        filename_counter = 0
        for line in lines:
            filename_counter += 1
            filename = line.rstrip() + '.py'
            candidate_code_snippet_filenames.append(filename)
            print('Loaded ', filename_counter, ' filenames out of 3361965.', end='\r')

    folder_counter = -1
    found_files_counter = 0
    for sub_directory, dirs, files in os.walk(root_directory):
        folder_counter += 1
        for file in files:
            if file in candidate_code_snippet_filenames:
                found_files_counter += 1
                print('Found a file: ' + file)

            # Run(['--errors-only', full_file_path])
            full_file_path = os.path.join(sub_directory, file)
            if folder_counter < 6770:
                print('Processing folder number: ', folder_counter, ' | Filepath: ' + full_file_path, end='\r')
            else:
                print('Processed final folder: ', folder_counter, ' | Filepath: ' + full_file_path, end='\r')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lint_snippets()
