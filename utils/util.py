from school_management_system.settings import DEBUG


def decide_the_message(x, y):
    """
    :param x:
        > anything
    :param y:
        > anything
    :return:
        > return x value if DEBUG=True / return y value if DEBUG=False
    """
    if DEBUG:
        return x
    else:
        return y


def compose_into_a_single_decorator(*decs):
    """
    :param decs:
        > decorator
    :return:
        > combined decorator
    """
    def decor(f):
        for dec in decs:
            f = dec(f)
        return f
    return decor
