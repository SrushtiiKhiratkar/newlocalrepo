from behave import *

use_step_matcher("re")


@given("I am on a search page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I am on a search page')