def my_zip_gen(a_iter, b_iter):

    len_b = len(b_iter)

    return ((a_elem, b_iter[i]) if i < len_b else (a_elem, None)
            for i, a_elem in enumerate(a_iter))

import json

from myutils import my_zip_gen


def groping(
        output_pth="./out.txt",
        user_pth="./users.csv",
        hobby_pth="./hobby.csv"):

    if not (user_pth or hobby_pth):
        return -1

    user_lines = None
    hobby_lines = None

    with open(user_pth, "r", encoding="utf-8") as user_file:
        user_lines = user_file.readlines()

    with open(hobby_pth, "r", encoding="utf-8") as hobby_file:
        hobby_lines = hobby_file.readlines()

    if len(user_lines) < len(hobby_lines):
        return 1

    group = {}

    for fio, hobby in my_zip_gen(user_lines, hobby_lines):
        fio = fio.replace("\n", "").replace(",", " ")
        group[fio] = hobby.replace("\n", "") if hobby else None

    with open(output_pth, "w+", encoding="utf-8") as out_file:
        out_file.writelines(json.dumps(group))
    #print(group)


    return 0