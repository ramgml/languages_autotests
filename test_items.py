

def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_element_by_css_selector('form#add_to_basket_form button[type=submit]')
    assert button is not None
