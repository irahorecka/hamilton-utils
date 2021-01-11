def parse(filepath):
    return_list = parse_lay(filepath)
    return clean_labware_list(return_list)

def open_lay(filepath):
    with open(filepath, "r", encoding='latin-1') as file:
        return file.readlines()


def parse_lay(filepath):
    mother_labware_coord_list = []
    labware = [line for line in open_lay(filepath) if line.startswith("Labware")]
    labware_split = [line.split("Labware") for line in labware]

    for labware in labware_split:
        labware_tform3 = [
            line.strip()
            for line in labware
            if "TForm.3.X" in line
            or "TForm.3.Y" in line
            or "ZTrans" in line
            and "ZTransValue" not in line
        ]
        if not labware_tform3:
            continue
        # get rid of persistent "Id" string in labware[1]
        coord_list = [labware[1][4:].strip("Id")]

        for i in labware_tform3:
            if labware[1][:4] == i[:4]:  # make sure labware id's match
                coord_list.append(i[4:])  # append content, not id's

        if len(coord_list) == 4:  # we want name, x, y, and z
            mother_labware_coord_list.append(coord_list)

    return mother_labware_coord_list


def clean_labware_list(list_):
    # get rid of that Tform and crap
    clean_list_ = []
    for sub_list in list_:
        sub_clean_list_ = []
        for item in sub_list:
            if "TForm.3.X" in item:
                item = item.strip("TForm.3.X")
            elif "TForm.3.Y" in item:
                item = item.strip("TForm.3.Y")
            elif "ZTrans" in item:
                item = item.strip("ZTrans")
            sub_clean_list_.append(item)
        clean_list_.append(sub_clean_list_)
    return clean_list_
