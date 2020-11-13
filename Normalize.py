# import re

# hamze = u'\u0621'

a_kolah = u'\u0622'  # to ا
alef_hamze_above = u'\u0623'  # to ا
alef_hamze_below = u'\u0625'  # to ا
yeh_hamze = u'\u0626'  # to ی
heh_hamze = u'\u06c2'  # to ه
vav_hamze = u'\u0624'  # to و

# to ''
comma = u'\u060C'
fathe = u'\u064e'
zamme = u'\u064f'
kasre = u'\u0650'
tashdid = u'\u0651'
nim_fasele = u'\u200c'
fathe_n = u'\u064b'
# zamme_n = u'\u064c'
# kasre_n = u'\u064d'

grouping = dict({a_kolah: 'ا', alef_hamze_below: 'ا', alef_hamze_above: 'ا', yeh_hamze: 'ی', vav_hamze: 'و',
                 heh_hamze: 'ه', comma: '', fathe: '', zamme: '', kasre: '', tashdid: '', nim_fasele: '', fathe_n: ''})

#
# all_pat = re.compile(u"[" + u"".join(grouping.keys()) + u"]")
# # print(all_pat)
# harekat = re.compile(u"[" + u"".join([fathe, zamme, kasre, nim_fasele,
#                                       tashdid, comma, fathe_n]) + u"]")
# # print(harekat)
# vav_hamze_pat = re.compile(u"[" + u"".join([vav_hamze]) + u"]")
# yeh_hamze_pat = re.compile(u"[" + u"".join([yeh_hamze]) + u"]")
# alef = re.compile(u"[" + u"".join([a_kolah, alef_hamze_above, alef_hamze_below]) + u"]")
# heh_hamze_pat = re.compile(u"[" + u"".join([heh_hamze]) + u"]")
# lower_latin = re.compile("[A-Z]")
