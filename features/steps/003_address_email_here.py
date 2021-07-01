from behave import *

@then('Verify address 1 "{addrss_1}" is here')
def vrfy_addrss_1_here(context, addrss_1):
    """
    Verify address "640 Ellicott Street" is here
    """
    context.app.main_page.vrfy_addrss_1_here(addrss_1)


@step('Verify address 2 "{addrss_2}" is here')
def vrfy_addrss_2_here(context, addrss_2):
    """
    Verify address "640 Ellicott Street" is here
    """
    context.app.main_page.vrfy_addrss_2_here(addrss_2)


@step('Verify email "{email}" is here')
def vrfy_email_here(context, email):
    """
    Verify address "640 Ellicott Street" is here
    """
    context.app.main_page.vrfy_email_here(email)


@then('Verify logo "{logo}" is here')
def vrfy_logo_here(context, logo):
    """
    Verify address "640 Ellicott Street" is here
    """
    context.app.main_page.vrfy_logo_here(logo)