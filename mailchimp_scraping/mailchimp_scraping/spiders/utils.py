def extract_with_xpath(response, xpath):
    """
    Extracts data from a response using the provided XPath.

    Args:
        response (obj): The response object to extract data from.
        xpath (str): The XPath expression to use for extraction.

    Returns:
        str: Extracted data from the response using the given XPath.
    """
    return response.xpath(xpath).get()


def extract_with_xpath_get_all(response, xpath):
    """
    Extracts multiple data elements from a response using the provided XPath.

    Args:
        response (obj): The response object to extract data from.
        xpath (str): The XPath expression to use for extraction.

    Returns:
        list: List of extracted data elements from the response using the given XPath.
    """
    return response.xpath(xpath).getall()


def extract_with_css(response, css):
    """
    Extracts data from a response using the provided CSS selector.

    Args:
        response (obj): The response object to extract data from.
        css (str): The CSS selector expression to use for extraction.

    Returns:
        str: Extracted data from the response using the given CSS selector.
    """
    return response.css(css).get()


def extract_with_css_get_all(response, css):
    """
    Extracts multiple data elements from a response using the provided CSS selector.

    Args:
        response (obj): The response object to extract data from.
        css (str): The CSS selector expression to use for extraction.

    Returns:
        list: List of extracted data elements from the response using the given CSS selector.
    """
    return response.css(css).getall()

