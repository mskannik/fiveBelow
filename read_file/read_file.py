def read_file(file_name):
    props = {}
    try:
        with open(file_name,mode='r') as target:
            props = {key.strip():value.strip() for (key,value) in [tuple(str(el).rstrip().split('=')) for el in [line for line in target.readlines() if line.strip()] if el[0] != '#']}     
    except IOError:
        print("+++ERROR:[ Unable to open the file {}]".format(file_name))
    return props


if __name__ == "__main__":
    get_file_content = read_file("input.txt")
    print(get_file_content)
    
