def add_3_dict(d1, d2, d3):
    dictionary={}
    for key in d1:
        value = d1[key]
        if key in d2 and value != d2[key]:              #1!=2
            if key in d3 and value != d3[key]:          #1!=3
                if d3[key] != d2[key]:
                    dictionary[key] = (value, d2[key], d3[key])
                else:
                    dictionary[key] = (value, d2[key])
            else:
                dictionary[key] = (value, d2[key])
        else:
            if key in d3 and value != d3[key]:
                dictionary[key] = (value, d3[key])
            else:
                dictionary[key] = (value)
    for key in d2:
        if key not in dictionary:
            value = d2[key]
            if key in d3 and value != d3[key]:
                dictionary[key] = (value, d3[key])
            else:
                dictionary[key] = (value)

    for key in d3:
        if key not in dictionary:
            value = d3[key]
            dictionary[key] = (value)

    return dictionary



def main():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 3, 'c': 3, 'd': 4}
    d3 = {'c': 5, 'd': 4, 'e': 6}

    result = add_3_dict(d1, d2, d3)

    print("Merged dictionary:")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
