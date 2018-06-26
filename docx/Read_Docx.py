# coding:utf-8
import docx

file = docx.Document(r"D:\img\test\test.docx")
for para in file.paragraphs:
    print para.text
