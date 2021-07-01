import re
from selenium import webdriver


# QUESTION 1
def check_links_target(driver):
    print("\nQuestion 1:\n")
    image_extensions = re.compile(r"\w*.(apng|avif|gif|jpg|jpeg|jfif|pjpeg|pjp|png|svg|webp)")
    links = driver.find_elements_by_xpath("//a[@href]")
    for link in links:
        href = str(link.get_attribute("href"))
        exist = image_extensions.search(href)
        if exist is not None:
            print("link with text:", link.text, ", directly targets image file:", href)


# QUESTION 3
def check_meta_tags(driver):
    print("\nQuestion 3:\n")

    meta_tags = driver.find_elements_by_xpath("//meta")
    for meta in meta_tags:
        attribute = meta.get_attribute('http-equiv')
        if attribute == "refresh":
            print("Meta tags should not be used to refresh or redirect: meta", str(meta_tags.index(meta)))


# QUESTION 2
def check_deprecated_attribute(driver):
    print("\nQuestion 2:\n")

    deprecated_attributes = {
        'accept': ['form'],
        'align': ['caption', 'col', 'div', 'embed', 'h1', 'hr', 'iframe', 'img', 'input', 'legend', 'object', 'p',
                  'table', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
        'alink': ['body'],
        'allowtransparency': ['iframe'],
        'archive': ['object'],
        'axis': ['td', 'th'],
        'background': ['body', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'td', 'th'],
        'bgcolor': ['body', 'table', 'td', 'th', 'tr'],
        'border': ['img', 'object'],
        'bordercolor': ['table'],
        'cellpadding': ['table'],
        'cellspacing': ['table'],
        'char': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
        'charoff': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
        'charset': ['a', 'link'],
        'classid': ['object'],
        "clear": ['br'],
        'code': ['object'],
        'codebase': ['object'],
        'codetype': ['object'],
        'color': ['hr'],
        'compact': ['dl', 'ol', 'ul'],
        'coords': ['a'],
        'datafld': ['a', 'applet', 'button', 'div', 'fieldset', 'frame', 'iframe', 'img', 'input', 'label', 'legend',
                    'marquee', 'object', 'param', 'select', 'span', 'textarea'],
        'dataformatas': ['button', 'div', 'input', 'label', 'legend', 'marquee', 'object', 'option', 'select', 'span',
                         'table'],
        'datapagesize': ['table'],
        'datasrc': ['a', 'applet', 'button', 'div', 'frame', 'iframe', 'img', 'input', 'label', 'legend', 'marquee',
                    'object', 'option', 'select', 'span', 'table', 'textarea'],
        'declare': ['object'],
        'event': ['script'],
        'for': ['script'],
        'frame': ['table'],
        'frameborder': ['iframe'],
        'height': ['td', 'th'],
        'hspace': ['embed', 'iframe', 'img', 'input', 'object'],
        'ismap': ['input'],
        'langauge': ['script'],
        'link': ['body'],
        'lowsrc': ['img'],
        'marginbottom': ['body'],
        'marginheight': ['body', 'iframe'],
        'marginleft': ['body'],
        'marginright': ['body'],
        'margintop': [' body'],
        'marginwidth': ['body', 'iframe'],
        'methods': ['a', 'link'],
        'name': ['a', 'embed', 'img', 'option'],
        'nohref': ['area'],
        'noshade': [' hr'],
        'nowrap': ['td', 'th'],
        'profile': ['head'],
        'rules': ['table'],
        'scheme': ['meta'],
        'scope': [' td'],
        'scrolling': [' iframe'],
        'shape': ['a'],
        'size': [' hr'],
        'standby': [' object'],
        'summary': [' table'],
        'target': ['link'],
        'text': ['body'],
        'type': ['li', 'param', 'ul'],
        'urn': ['a', 'link'],
        'usemap': [' input'],
        'valign': ['col', 'tbody', 'thead', 'tfoot', 'td', 'th', 'tr'],
        'valuetype': ['param'],
        'version': ['html'],
        'vlink': [' body'],
        'vspace': ['embed', 'iframe', 'img', 'input', 'object'],
        'width': ['col', 'hr', 'pre', 'table', 'td', 'th']
    }
    elements = driver.find_elements_by_xpath("//*")
    for element in elements:
        tag_name = element.tag_name
        for attribute in deprecated_attributes:  # row
            if tag_name in deprecated_attributes[attribute]:
                element_attrs = driver.execute_script(  # get all attributes as a dictionary
                    'var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;',
                    element)
                if attribute in element_attrs:
                    print("attribute:", attribute, "should not used in tag:", tag_name)


# QUESTION 4
def check_style_attribute(driver):
    print("\nQuestion 4:\n")

    elements = driver.find_elements_by_xpath("//*")
    for element in elements:
        element_style = element.get_attribute("style")
        if element_style != "":
            print("element ", element.tag_name, "has style attribute with value : ", element_style)


# QUESTION 5
def check_links_text(driver):
    print("\nQuestion 5:\n")

    links = driver.find_elements_by_xpath("//a[@href]")
    for i in range(len(links)):
        current_link = links[i]
        current_link_address = current_link.get_attribute("href")
        current_link_text = current_link.text
        for j in range(i + 1, len(links)):
            next_link = links[j]
            next_link_address = next_link.get_attribute("href")
            next_link_text = next_link.text
            if current_link_text == next_link_text and current_link_text != "":
                if current_link_address != next_link_address:
                    print("Links with identical texts should have identical targets:\ntext: ", current_link_text,
                          "\naddress 1: ", current_link_address, "\naddress 2: ", next_link_address)


# Python program to check if rectangles overlap
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Returns true if two rectangles(l1, r1)
# and (l2, r2) overlap
def doOverlap(l1, r1, l2, r2):
    # To check if either rectangle is actually a line
    # For example  :  l1 ={-1,0}  r1={1,1}  l2={0,-1}  r2={0,1}

    if l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y:
        # the line cannot have positive overlap
        return False

    # If one rectangle is on left side of other
    if l1.x >= r2.x or l2.x >= r1.x:
        return False

    # If one rectangle is above other
    if l1.y >= r2.y or l2.y >= r1.y:
        return False

    return True


# QUESTION 6
def check_elements_overlap(driver):
    print("\nQuestion 6:\n")

    windows_sizes = [[800, 600], [1024, 768], [1448, 1072], [1600, 1200], [2048, 1536]]
    for i in range(len(windows_sizes)):
        driver.set_window_size(windows_sizes[i][0], windows_sizes[i][1])
        inputs = driver.find_elements_by_xpath("//input | //label | //select |  //textarea | //button | //fieldset | //legend | //datalist | //output | //option | //optgroup")
        for j in range(len(inputs)):
            current_input = inputs[j]
            current_input_location_top_left_y, current_input_location_top_left_x = current_input.location['y'], \
                                                                                   current_input.location['x']
            current_input_size_w, current_input_size_h = current_input.size['width'], current_input.size['height']
            current_input_location_bottom_right_y, current_input_location_bottom_right_x = current_input_location_top_left_y + current_input_size_h, current_input_location_top_left_x + current_input_size_w
            current_input_top_left_point = Point(current_input_location_top_left_x, current_input_location_top_left_y)

            current_input_bottom_right_point = Point(current_input_location_bottom_right_x,
                                                     current_input_location_bottom_right_y)

            for k in range(j + 1, len(inputs)):
                next_input = inputs[k]
                next_input_location_top_left_y, next_input_location_top_left_x = next_input.location['y'], \
                                                                                 next_input.location['x']
                next_input_size_w, next_input_size_h = next_input.size['width'], next_input.size['height']
                next_input_location_bottom_right_y, next_input_location_bottom_right_x = next_input_location_top_left_y + next_input_size_h, \
                                                                                         next_input_location_top_left_x + next_input_size_w

                next_input_top_left_point = Point(next_input_location_top_left_x,
                                                  next_input_location_top_left_y)

                next_input_bottom_right_point = Point(next_input_location_bottom_right_x,
                                                      next_input_location_bottom_right_y)

                if doOverlap(current_input_top_left_point, current_input_bottom_right_point, next_input_top_left_point,
                             next_input_bottom_right_point):
                    print("in size:", str(windows_sizes[i]), "input:", str(j), "do overlap with input:", str(k))


URL = input("enter URL:")
driverFirefox = webdriver.Firefox(executable_path='C:\\Users\\nasim\\Downloads\\geckodriver.exe')
driverFirefox.get(URL)
driver = webdriver.Chrome('C:/Users/nasim/Downloads/chromedriver.exe')
# driver = webdriver.Chrome('/home/alireza/Desktop/testing/UntitledFolder/seleniumWebDriver/chromedriver')
driver.get(URL)


check_links_target(driver)
check_deprecated_attribute(driver)
check_meta_tags(driver)
check_style_attribute(driver)
check_links_text(driver)
check_elements_overlap(driver)
check_elements_overlap(driverFirefox)
# https://google.com
