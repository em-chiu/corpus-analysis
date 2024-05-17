#!/usr/bin/env python
"""Runs queries for HW6."""

import sqlite3


DB_PATH = "hw6.db"


def main() -> None:
    with sqlite3.connect(DB_PATH) as connection:
        cursor = connection.cursor()
        # TODO: put your query here, then remove this TODO.

        # determines the frequency threshold for "1 per million words". 
        #SUM up the frequencies in the frequency corpus and then divide to obtain the threshold, 
        #and retrieve the result using .fetchone()[0].
        hundred_pmw = cursor.execute(
            """
            SELECT SUM(frequency) / 10000 
            FROM frequencies;
            """
        ).fetchone()[0]
        # TODO: put your query here, then remove this TODO. Use f-string
        # interpolation to insert `hundred_pwm` into the query.

        #The WHERE filter in (2) should use LIKE to "parse" the features column: 
        #nouns have a features string that begins with the string N;
        for row in cursor.execute(
            f"""
            SELECT DISTINCT frequencies.word --p18 https://wellformedness.com/courses/LING78000/PDFs/debarros-2022-ch7.pdf
            --Write SELECT portion of the query in (2) so that it only returns the one field you need.
            FROM frequencies
            JOIN morphology
            ON frequencies.word = morphology.word
            --p2 subquery https://wellformedness.com/courses/LING78000/PDFs/debarros-2022-ch13.pdf
            WHERE morphology <> 'N' AND frequency <= (LIKE hundred_pwm #SUBQUERY?? 
                SELECT frequency FROM frequencies
                ) -- iterate over the results within subquery? or after closed parenthesis??
                --https://stackoverflow.com/questions/28702149/looping-through-select-result-set-in-sql
            ORDER BY frequencies.word; --For string values ORDER BY keyword will order alphabetically
            """
        ):
            print(f"{word}:\t{count:,}")
            # TODO: add appropriate print statement, then remove this TODO
            # and ellipsis.
            ...


if __name__ == "__main__":
    main()
