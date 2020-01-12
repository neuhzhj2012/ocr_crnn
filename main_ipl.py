#encoding: utf-8
import os
import random
from load_ttf import MYFONT
from get_content import CONT

if __name__ == '__main__':
    ttf_folder = 'data'
    dst_folder = 'rst'
    fontObj = MYFONT(ttf_folder) #字库
    contObj = CONT() #省份对应的字母集
    imgwh = [100, 32]

    provinces = contObj.get_province()
    alphas = contObj.get_alpha()
    nums = contObj.get_num()
    fonts = fontObj.get_fonts()

    for province in provinces: #当前省份内数据扩大10倍
        for alpha in contObj.get_province_altha(province) * 50: #每个城市字母下生成500个
            nums_3 = ''.join(random.sample(nums, 3)) #3个数字
            alpha_2 = ''.join(random.sample(alphas, 2)) #2个字母
            tmp = nums_3 + alpha_2
            combs_1 = ''.join(random.sample(tmp,len(tmp)))

            nums_4 = ''.join(random.sample(nums, 4)) #4个数字
            alpha_1 = ''.join(random.sample(alphas, 1)) #2个字母 #1个字母
            tmp = nums_4 + alpha_1
            combs_2 = ''.join(random.sample(tmp,len(tmp)))

            nums_5 = ''.join(random.sample(nums, 5)) #全数字
            tmp = nums_5 + alpha_1
            combs_3 = ''.join(random.sample(tmp,len(tmp)))
            nums_6 = ''.join(random.sample(nums, 6)) #新能源
            combs_4 = nums_5
            combs_5 = nums_6
            txts = [province + alpha + combs_1,province + alpha + combs_2,
                    province + alpha + combs_3,province + alpha + combs_4,
                    province + alpha + combs_5]
            for txt in txts:
                print (txt)
                txt_font = random.sample(fonts, 1)[0]
                if len(txt) == 8:
                    txt_font = txt_font.font_variant(size=20, encoding='unic')
                    # print (txt_font.size)
                txt_cord = fontObj.get_txt_cord(txt, txt_font)
                img_pil = fontObj.get_txt_part_base(imgwh, txt, txt_cord, txt_font)
                # img_pil.show()
                img_pil.save(os.path.join(dst_folder, txt + '.jpg'))
