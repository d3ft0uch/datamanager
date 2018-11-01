import csv
from django.http import StreamingHttpResponse


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def generate_csv_response(data):
    """
    :param data: dict
    :return: StreamingHttpResponse object
    """
    response = StreamingHttpResponse(streaming_content=iter_items(data, Echo()),
                                     content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=\"openspend-dataset.csv\"'

    return response


def iter_items(data, pseudo_buffer):
    headers_list = data['cells'][0].keys()
    headers_dict = {}
    for header in headers_list:
        headers_dict[header] = header
    writer = csv.DictWriter(pseudo_buffer, fieldnames=headers_list)
    yield writer.writerow(headers_dict)
    for dict_object in data['cells']:
        yield writer.writerow(dict_object)
