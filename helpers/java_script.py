def page_width(driver):
    return driver.execute_script("return Math.max(document.body.scrollWidth, document.body.offsetWidth, "
                                 "document.documentElement.clientWidth, document.documentElement.scrollWidth, "
                                 "document.documentElement.offsetWidth);")

def page_height(driver):
    return driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, "
                                 "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
                                 "document.documentElement.offsetHeight);")
