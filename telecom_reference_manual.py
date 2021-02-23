import color_pairnum_translator as translator

def createReferenceManual():
    tel_pair_num_start_index = 1
    tel_pair_num_end_index = 26
    reference_manual_list = []
    for pair_number in range(tel_pair_num_start_index, tel_pair_num_end_index):
        color_pair = translator.get_color_from_pair_number(pair_number)
        formatted_colorpair = translator.color_pair_to_string(color_pair[0], color_pair[1])
        reference_manual_list.append ("{:<10} {} ".format(pair_number, formatted_colorpair))
    return reference_manual_list

def printReferenceManual(manual_Data):
    print ("{:<10} {} ".format('PairNumber', 'ColorPair'))
    for data in manual_Data:
        print(data)