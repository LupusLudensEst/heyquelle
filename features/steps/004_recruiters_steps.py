from behave import *

@then("Go as a Recruiter and verify all works according the steps")
def recruiter_steps(context):
    """
    Go as a Recruiter and verify all works according the steps
    """
    context.app.main_page.recruiter_steps()