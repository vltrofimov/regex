from pprint import pprint
import csv
import re
with open("phonebook_raw.csv",encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pattern1 = re.compile("(\+7|8)(\s?)(\(495\)|495)(\s|\-?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})")
    pattern2 = re.compile("(\(?)(доб.)(\s)(\d{4})(\)?)")
    final_list = []
    for contact in contacts_list:
        if len(contact[0].split()) == 3:
            contact[2] = (contact[0].split())[2]
            contact[1] = (contact[0].split())[1]
            contact[0] = (contact[0].split())[0]
        elif len(contact[0].split()) == 2:
            contact[1] = (contact[0].split())[1]
            contact[0] = (contact[0].split())[0]
        else:
            if len(contact[1].split()) == 2:
                contact[2] = (contact[1].split())[1]
                contact[1] = (contact[1].split())[0]
        final_list.append(contact)

    i=1
    for record in final_list:
        current_lastname = record[0]
        for record_1 in final_list[i:len(final_list)]:
            if current_lastname == record_1[0]: #нашли дубль
                j=0
                for element_of_record_1 in record_1[0:7]:
                    if len(element_of_record_1) == 0:
                        record_1[j]=record[j]
                    j=j+1
                final_list.remove(record)
        i = i+1


    result = pattern1.findall(str(final_list))
    result2 = pattern2.findall(str(final_list))
    final_string_1 = pattern1.sub(r'+7(495)\5-\7-\9',str(final_list))
    final_string_2 = pattern2.sub(r"доб.\4",str(final_string_1))

    list_for_recording = final_string_2.split('[')
    for element in list_for_recording:
        print(element)

    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=' ')
        datawriter.writerows(list_for_recording)

