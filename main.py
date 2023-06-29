def generate_sql_insertion_from_bad_words(file_path, output_file):
    with open(file_path, 'r') as file:
        with open(output_file, 'w') as output:
            for line in file:
                bad_word = line.strip()
                sql_insertion = f"INSERT INTO chat_filter_rule (word, filter, warn, ban) VALUES ('{bad_word}', True, True, False );\n"
                output.write(sql_insertion)

bad_word_file_path = 'bad_words.txt'
output_file_path = 'sql_insertions.sql'
generate_sql_insertion_from_bad_words(bad_word_file_path, output_file_path)
