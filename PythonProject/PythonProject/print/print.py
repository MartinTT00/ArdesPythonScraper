def print_func(links):
    number_of_links = input("Choose number of links to show (number/all): ")
    if number_of_links == "all":
        for key, value in links.items():
            print(key + " - " + value)
    else:
        last_index = int(number_of_links)
        array_of_links = []
        for key, value in links.items():
            array_of_links.append(key + " - " + value)
        for index in range(0, last_index):
            print(array_of_links[index])