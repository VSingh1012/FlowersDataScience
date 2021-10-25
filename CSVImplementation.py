df = r"CSV Files\plants.csv"

#csv appending function

def append_to_csv(path, plant_name, plant_height, plant_type):

    from csv import writer
    with open(path, 'a') as f_object:
        writer_object = writer(f_object)

        ls = [str(plant_height), plant_name, plant_type]

        writer_object.writerow(ls)




#Area where implementation and writing to the file occurs



