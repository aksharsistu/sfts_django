def start(request):
    """
    Logging function for Start Module
    :param request: HTTPRequest
    :return: HttpResponse
    """
    if not checks(request):
        return


def end(request):
    """
    Logging function for End Module
    :param request: HTTPRequest
    :return: HttpResponse
    """
    if not checks(request):
        return


def qa(request):
    """
    Logging function for QA Module
    :param request: HTTPRequest
    :return: HttpResponse
    """
    if not checks(request):
        return


def rework(request):
    """
    Logging function for Rework Module
    :param request: HTTPRequest
    :return: HttpResponse
    """
    if not checks(request):
        return


def checks(request):
    """
    List of checks to be implemented:
    1. Check for multiple scans at the same stage.
    2. Product Barcode range check for validity.
    3. Check for successful completion of previous stage.
    4. Check for scan at the start of the stage.
    :param request: HTTPRequest
    :return: boolean
    """
    return False
