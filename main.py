import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/home/alireza/Desktop/testing/UntitledFolder/chromedriver')
# URL = input("enter URL:")
driver.get('file:///home/alireza/Desktop/testing/UntitledFolder/seleniumWebDriver/example.html')


def first_task():
    image_extensions = re.compile(r"\w*.(apng|avif|gif|jpg|jpeg|jfif|pjpeg|pjp|png|svg|webp)")
    links = driver.find_elements_by_xpath("//a[@href]")
    for link in links:
        href = str(link.get_attribute("href"))
        exist = image_extensions.search(href)
        if exist is not None:
            print(href)  # first error tu sorat soal


def fourth_task():
    elements = driver.find_elements_by_xpath("//*")
    for element in elements:
        element_style = element.get_attribute("style")
        if element_style != "":
            print("element ", element.tag_name, "has style attribute with value : ", element_style)


def fifth_task():
    links = driver.find_elements_by_xpath("//a[@href]")
    for i in range(len(links)):
        print(str(i) + " : ")
        current_link = links[i]
        current_link_address = current_link.get_attribute("href")
        current_link_text = current_link.text
        for j in range(i + 1, len(links)):
            next_link = links[j]
            next_link_address = next_link.get_attribute("href")
            next_link_text = next_link.text
            if current_link_text == next_link_text:
                if current_link_address != next_link_address:
                    print("Links with identical texts should have identical targets:\ntext: ", current_link_text,
                          "\naddress 1: ", current_link_address, "\naddress 2: ", next_link_address)


fourth_task()
# first_task()

# elements = driver.find_elements_by_xpath("//*")

# deprecated = {
#     'accept': tuple(['form']),
#     'align': tuple(['caption', 'col', 'div', 'embed', 'h1-h6', 'hr', 'iframe', 'img', 'input', 'legend', 'object', 'p',
#                     'table', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr']),
#     'alink': ['body'],
#     'allowtransparency': ['iframe'],
#     'archive': ['object'],
#     'axis': ['td', 'th'],
#     'background': ['body', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th'],
#     'bgcolor': ['body', 'table', 'td', 'th', 'tr'],
#     'border': ['img', 'object'],
#     'bordercolor': ['table'],
#     'cellpadding': ['table'],
#     'cellspacing': ['table'],
#     'char': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
#     'charoff': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
#     'charset': ['a', 'link'],
#     'classid': ['object'],
#     "clear": ['br'],
#     'code': ['object'],
#     'codebase': ['object'],
#     'codetype': ['object'],
#     'color': ['hr'],
#     'compact': ['dl', 'ol', 'ul'],
#     'coords': ['a'],
#     'datafld': ['a', 'applet', 'button', 'div', 'fieldset', 'frame', 'iframe', 'img', 'input', 'label', 'legend',
#                 'marquee', 'object', 'param', 'select', 'span', 'textarea'],
#     'dataformatas': ['button', 'div', 'input', 'label', 'legend', 'marquee', 'object', 'option', 'select', 'span',
#                      'table'],
#     'datapagesize': ['table'],
#     'datasrc': ['a', 'applet', 'button', 'div', 'frame', 'iframe', 'img', 'input', 'label', 'legend', 'marquee',
#                 'object', 'option', 'select', 'span', 'table', 'textarea'],
#     'declare': ['object'],
#     'event': ['script'],
#     'for': ['script'],
#     'frame': ['table'],
#     'frameborder': ['iframe'],
#     'height': ['td', 'th'],
#     'hspace': ['embed', 'iframe', 'img', 'input', 'object'],
#     'ismap': ['input'],
#     'langauge': ['script'],
#     'link': ['body'],
#     'lowsrc': ['img'],
#     'marginbottom': ['body'],
#     'marginheight': ['body', 'iframe'],
#     'marginleft': ['body'],
#     'marginright': ['body'],
#     'margintop': [' body'],
#     'marginwidth': ['body', 'iframe'],
#     'methods': ['a', 'link'],
#     'name': ['a', 'embed', 'img', 'option'],
#     'nohref': ['area'],
#     'noshade': [' hr'],
#     'nowrap': ['td', 'th'],
#     'profile': ['head'],
#     'rules': ['table'],
#     'scheme': ['meta'],
#     'scope': [' td'],
#     'scrolling': [' iframe'],
#     'shape': ['a'],
#     'size': [' hr'],
#     'standby': [' object'],
#     'summary': [' table'],
#     'target': ['link'],
#     'text': ['body'],
#     'type': ['li', 'param', 'ul'],
#     'urn': ['a', 'link'],
#     'usemap': [' input'],
#     'valign': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
#     'valuetype': ['param'],
#     'version': ['html'],
#     'vlink': [' body'],
#     'vspace': ['embed', 'iframe', 'img', 'input', 'object'],
#     'width': ['col', 'hr', 'pre', 'table', 'td', 'th']
# }
#
# deprecated2 = {
#     'accept': tuple(['form']),
#     'align': tuple(['caption', 'col', 'div', 'embed', 'h1-h6', 'hr', 'iframe', 'img', 'input', 'legend', 'object', 'p',
#                     'table', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'])}
#
# from collections import defaultdict
# from itertools import product
#
# # result = [
# #     dict(x)
# #     for x in product(*vals(deprecated2))
# # ]
#
#
# for element in elements:
#     if element.tag_name in deprecated:
#         dep = deprecated[element.tag_name]
#         print(dep)
#     # attributes = element.get_property('attributes')[0]
#     # print(attributes)
#
# time.sleep(5)
# driver.quit()
#
# # C:\Users\nasim\Downloads\example.html
