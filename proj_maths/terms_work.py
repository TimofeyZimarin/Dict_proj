def get_terms_for_table():
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            a = line.count(';')
            if a > 2:
                term_1, definition_1, date_1, url_1 = line.split(";")
                terms.append([cnt, term_1, definition_1, date_1, url_1])
                cnt += 1
            else:
                term, definition, date = line.split(";")
                terms.append([cnt, term, definition, date, 'Картинки нет :('])
                cnt += 1
    return terms

def get_terms_for_table_with_pic():
    terms_with_pic = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        cnt_pic = 1
        for line in f.readlines()[1:]:
            b = line.count(';')
            if b > 2:
                term_1, definition_1, date_1, url_1 = line.split(";")
                terms_with_pic.append([cnt_pic, term_1, definition_1, date_1, url_1])
                cnt_pic += 1
            else:
                continue
    return terms_with_pic

def write_term(new_term, new_definition, date):
    new_term_line = f"{new_term};{new_definition};{date}"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

def compare(new_term):
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            a = line.count(';')
            if a > 2:
                term, defin, add_time, url = line.split(";")
            else:
                term, defin, add_time = line.split(";")
            str_1 = str(new_term)
            str_2 = str(term)
            if str_1.lower() == str_2.lower():
                return False
    return True

def add_picture_to_term(old_term, add_picture):
    new_picture = f"{old_term};{add_picture}"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
        for i in range(len(old_terms)):
            a = old_terms[i].count(';')
            if a > 2:
                term, defin, add_time, url = old_terms[i].split(";")
            else:
                term, defin, add_time = old_terms[i].split(";")
            str_1 = str(old_term)
            str_2 = str(term)
            if str_1.lower() == str_2.lower():
                a = [term, defin, add_time, add_picture]
                old_terms[i] = ";".join(a)
    new_terms = [title] + old_terms
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))

def try_to_add_picture(old_term):
    flag_to_try = False
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
        for i in range(len(old_terms)):
            a = old_terms[i].count(';')
            if a > 2:
                term, defin, add_time, url = old_terms[i].split(";")
            else:
                term, defin, add_time = old_terms[i].split(";")
            str_1 = str(old_term)
            str_2 = str(term)
            if str_1.lower() == str_2.lower():
                flag_to_try = True
    return flag_to_try

def get_terms_stats():
    words = []
    times = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            a = line.count(';')
            if a > 2:
                term, defin, add_time, url = line.split(";")
            else:
                term, defin, add_time = line.split(";")
            words.append(defin)
            times.append(add_time)
        length = len(words)
        if length!= 0:
            amount = [0]
        else:
            amount = []
        j = 0
        for i in range(0, len(times)-1):
            if times[i] == times[i+1]:
                continue
            else:
                amount.append(0)
        days = len(amount)
        avg = round(length/days)
        week = round(days / 7)
    stats = {
        "len": length,
        "days": days,
        "avg": avg,
        "week": week
        # "amount": amount
    }
    return stats
