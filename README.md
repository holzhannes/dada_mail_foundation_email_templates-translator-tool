# Dada Mail Template Translation Tool
Tool to translate the dada_mail_foundation_email_templates from a .csv file through a python skript


# How to use?

Place the unziped folder of [dada\_mail\_foundation\_email\_templates](https://github.com/justingit/dada_mail_foundation_email_templates/) on the same level with the `dada-mail-translation-de-formal.csv` (Formal German translation .csv you may create your own) together with the `translate.py` and run the comand: `pyhton translate.py`.

## How can I translate Dada Mail Template to my language?
1. Download the `.xlsx` or `.csv` and replace the content in the third column of the table with your translation.
2. Export the file to `dada-mail-translation-YOUR-LANGUAGE-CODE.csv`
3. Edit the value of translateCSV in `translate.py`: 
```python
translateCSV = "dada-mail-translation-YOUR-LANGUAGE-CODE.csv"
```
4. run the comand: `pyhton translate.py`.

# Note

This is just a simple search and replace tool in plaintext multiline replacing is working. In HTML-Files multiline replace including insertions is NOT working, therefore these textparts are splited in single lines.
