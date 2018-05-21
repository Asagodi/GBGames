import copy as cp


def check_giasmus(n_elem):
    if len(n_elem) % 2:
        head = n_elem[:int((len(n_elem)-1)/2)]
        tail = n_elem[int((len(n_elem)+1)/2):]
        tail.reverse()
        return head == tail
    else:
        head = n_elem[:int(len(n_elem)/2)]
        tail = n_elem[int(len(n_elem)/2):]
        tail.reverse()
        return head == tail


def generate_giasmus(scheme, center_elem=[]):
    if not isinstance(center_elem, list):
        center_elem = [center_elem]
    head = scheme
    tail = cp.copy(scheme)
    tail.reverse()
    return head + center_elem + tail
