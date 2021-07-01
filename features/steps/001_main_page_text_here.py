from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then('Verify text "{txt}" is here')
def vrfy_txt_here(context, txt):
    """
    Verify text "© 2021 AutoCareParts.com Powered by Shopify" is here
    """
    context.app.main_page.vrfy_txt_here(txt)