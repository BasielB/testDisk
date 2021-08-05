def extract_dict_from_body(request):
    body = request.body.decode('utf-8').split('&')
    return{i.split('=')[0]: i.split('=')[1] for i in body}
