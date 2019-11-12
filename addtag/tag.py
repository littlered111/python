# coding:utf-8

# 添加PDF书签

from pdf_unit import MyPDFHandler,PDFHandleMode as mode
import imp
#import ConfigParser
import sys

imp.reload(sys)

def main():

    pdf_handler = MyPDFHandler('E:/ISLR Seventh Printing.pdf',mode = mode.NEWLY)

    pdf_handler.add_bookmarks_by_read_txt('E:/Python file/addatag/ISIRtag.txt', page_offset = 14)

    pdf_handler.save2file('ISLR Seventh Printing with tag.pdf')



if __name__ == '__main__':

    main()