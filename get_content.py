#encoding: utf-8
class CONT():
    def __init__(self):
        self.num = [str(i) for i in range(9)]
        # self.alpha = [chr(i) for i in range(65,91)]
        self.car_plate = {'京':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,82)] + ['V', 'Y'],
                          '津':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + ['Q', 'R'],
                          '沪':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + ['R'],
                          '渝':[chr(i) for i in range(65,68)] + [chr(i) for i in range(70, 73)],
                          '冀':[chr(i) for i in range(65, 73)] + ['J', 'R', 'S', 'T'],
                          '豫':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 84)] + ['U'],
                          '云':['A'] + [chr(i) for i in range(67, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 84)] + ['V'],
                          '辽':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + ['P'],
                          '黑':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + ['P', 'R'],
                          '湘':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + ['U'],
                          '皖':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 84)],
                          '鲁':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 84)] + ['U', 'V'],
                          '新':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 83)],
                          '苏':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)],
                          '浙':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,77)],
                          '赣':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,78)],
                          '鄂':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 84)],
                          '桂':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 82)],
                          '粤':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + [chr(i) for i in range(80, 91)],
                          '甘':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,79)] + ['P'],
                          '晋':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,78)],
                          '蒙':[chr(i) for i in range(65, 73)] + [chr(i) for i in range(74,78)],
                          '陕':[chr(i) for i in range(65, 73)] + ['J','K','V'],
                          '吉':[chr(i) for i in range(65, 73)] + ['J'],
                          '闽': [chr(i) for i in range(65, 73)] + ['J', 'K'],
                          '贵':[chr(i) for i in range(65, 73)] + ['J'],
                          '川':[chr(i) for i in range(65, 71)] + ['H'] + [chr(i) for i in range(74,78)] + [chr(i) for i in range(81, 91)],
                          '青':[chr(i) for i in range(65, 73)],
                          '藏':[chr(i) for i in range(65, 73)] + ['J'],
                          '琼':[chr(i) for i in range(65, 70)],
                          '宁':[chr(i) for i in range(65, 70)]}
    def get_province_altha(self, province):
        return self.car_plate[province]
    def get_province(self):
        return list(self.car_plate.keys())
    def get_num(self):
        return self.num
    def get_alpha(self):
        alpha = list()
        for k, v in self.car_plate.items():
            alpha +=v
        return sorted(set(alpha))

