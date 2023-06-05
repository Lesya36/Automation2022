from BrainBucket.utils.config_reader import ConfigReader
from BrainBucket.webelements.browser import Browser


def before_all(context):
    configs = ConfigReader("BrainBucket/BDDBehave/logintests/steps/config.ini")
    context.configs = configs


def before_scenario(context, scenario):
    configs = context.configs
    browser = Browser(configs.get_url(), configs.get_browser(), configs.get_wait_time())
    context.browser = browser


def after_scenario(context, scenario):
    context.browser.shutdown()


def before_feature(context, feature):
    print("Runs Before Each Feature")


def after_feature(context, feature):
    print("Run After Each Feature")


def after_all(context):
    context.browser.shutdown()
