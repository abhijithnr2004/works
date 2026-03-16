num = {1,2,3,4,5,6}

frozen_num = frozenset(num)

frozen_num.remove(2) # error - frozen_num is immutable set
