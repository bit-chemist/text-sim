import string

one_v_two = { "text1":"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.",
  "text2":"The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."}


one_v_three = {"text1":"The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.",
  "text2":"We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."}


def jaccard_similarity(str1, str2):
    string1 = str1.translate(str.maketrans('', '', string.punctuation))
    string2 = str2.translate(str.maketrans('', '', string.punctuation))
    set_a = set(string1.split())
    set_b = set(string2.split())
    intersect = set_a.intersection(set_b)
    union = set_a.union(set_b)
    answer = float(len(intersect))/len(union)
    print(answer)

if __name__ == "__main__":
    jaccard_similarity(one_v_two['text1'], one_v_two['text2'])
    jaccard_similarity(one_v_three['text1'], one_v_three['text2'])
