import objgraph, gc

class OBJ(object):
    pass

def show_cycle_reference():
    a, b = OBJ(), OBJ()
    a.attr_b = b
    b.attr_a = a

if __name__ == '__main__':
    # 一定要先禁用gc防止误差
    gc.disable()
    for _ in range(50):
        show_cycle_reference()
    # 里面会调用gc.collect()
    # objgraph.show_growth()
    objgraph.show_most_common_types(50)